"""Module for the interactive Dash dashboard for blood report analytics.

This module creates a Dash web application that visualizes key insights
from the blood reports dataset, including infection trends, anemia distribution,
and CRP levels over time.
"""

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def create_dashboard(file_path: str = "data/blood_reports_dataset.csv") -> dash.Dash:
    """Creates and configures the Dash dashboard for blood report analytics.

    Args:
        file_path (str): The path to the blood reports CSV file.

    Returns:
        dash.Dash: The configured Dash application instance.
    """
    # Load the dataset
    df = pd.read_csv(file_path)

    # Initialize the Dash app
    app = dash.Dash(__name__, assets_folder='dash_app/assets')

    # Layout of the dashboard
    app.layout = html.Div([
        html.H1("Blood Report Analytics Dashboard"),

        html.Div([
            html.Div([
                html.Label("Select Gender:"),
                dcc.Dropdown(
                    id='gender-filter',
                    options=[{'label': i, 'value': i} for i in ['All'] + df['Gender'].unique().tolist()],
                    value='All',  # Default value
                    clearable=False
                ),
            ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Select Diagnosis:"),
                dcc.Dropdown(
                    id='diagnosis-filter',
                    options=[{'label': i, 'value': i} for i in ['All'] + df['Diagnosis'].unique().tolist()],
                    value='All',  # Default value
                    clearable=False
                ),
            ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        ], style={'padding': '20px'}),

        dcc.Store(id='filtered-data'), # Hidden component to store filtered data

        # Infection Trends over Time
        html.H2("Infection Trends Over Time"),
        dcc.Graph(id='infection-trends'),

        # Anemia Distribution by Age/Gender
        html.H2("Anemia Distribution by Age and Gender"),
        dcc.Graph(id='anemia-distribution'),

        # CRP Trends to monitor inflammation spikes
        html.H2("CRP Trends (Inflammation Spikes)"),
        dcc.Graph(id='crp-trends'),

        # Branch Performance (Placeholder for now)
        html.H2("Branch Performance (Data Not Available in Current Dataset)"),
        html.Div("This section requires 'Lab_ID' or similar branch-specific data.")
    ])

    # Callback to filter data and store it
    @app.callback(
        Output('filtered-data', 'data'),
        Input('gender-filter', 'value'),
        Input('diagnosis-filter', 'value')
    )
    def filter_data(selected_gender, selected_diagnosis):
        filtered_df = df.copy()
        if selected_gender != 'All':
            filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
        if selected_diagnosis != 'All':
            filtered_df = filtered_df[filtered_df['Diagnosis'] == selected_diagnosis]
        return filtered_df.to_json(date_format='iso', orient='split')

    # Callback for Infection Trends
    @app.callback(
        Output('infection-trends', 'figure'),
        Input('filtered-data', 'data')
    )
    def update_infection_trends(jsonified_filtered_data):
        """Updates the infection trends graph based on the dataset and filters.

        Args:
            jsonified_filtered_data (str): JSON string of the filtered dataframe.

        Returns:
            plotly.graph_objects.Figure: The updated infection trends line plot.
        """
        filtered_df = pd.read_json(jsonified_filtered_data, orient='split')
        filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

        infection_df = filtered_df[filtered_df['Diagnosis'].isin(['Bacterial infection', 'Viral infection'])]
        infection_counts = infection_df.groupby('Date').size().reset_index(name='count')
        fig = px.line(infection_counts, x='Date', y='count', title='Daily Infection Cases')
        return fig

    # Callback for Anemia Distribution
    @app.callback(
        Output('anemia-distribution', 'figure'),
        Input('filtered-data', 'data')
    )
    def update_anemia_distribution(jsonified_filtered_data):
        """Updates the anemia distribution graph based on the dataset and filters.

        Args:
            jsonified_filtered_data (str): JSON string of the filtered dataframe.

        Returns:
            plotly.graph_objects.Figure: The updated anemia distribution bar chart.
        """
        filtered_df = pd.read_json(jsonified_filtered_data, orient='split')

        anemia_df = filtered_df[filtered_df['Diagnosis'] == 'Anemia']
        anemia_age_gender = anemia_df.groupby(['Age', 'Gender']).size().reset_index(name='count')
        fig = px.bar(anemia_age_gender, x='Age', y='count', color='Gender', title='Anemia Cases by Age and Gender')
        return fig

    # Callback for CRP Trends
    @app.callback(
        Output('crp-trends', 'figure'),
        Input('filtered-data', 'data')
    )
    def update_crp_trends(jsonified_filtered_data):
        """Updates the CRP trends graph based on the dataset and filters.

        Args:
            jsonified_filtered_data (str): JSON string of the filtered dataframe.

        Returns:
            plotly.graph_objects.Figure: The updated CRP levels line plot.
        """
        filtered_df = pd.read_json(jsonified_filtered_data, orient='split')
        filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

        crp_df = filtered_df.sort_values('Date')
        fig = px.line(crp_df, x='Date', y='CRP_mg_L', title='CRP Levels Over Time')
        return fig
    
    return app


app = create_dashboard()