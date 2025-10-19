import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the dataset
df = pd.read_csv("blood_reports_dataset.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Blood Report Analytics Dashboard"),

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

# Callback for Infection Trends
@app.callback(
    Output('infection-trends', 'figure'),
    Input('infection-trends', 'relayoutData') # Dummy input to trigger initial load
)
def update_infection_trends(relayoutData):
    infection_df = df[df['Diagnosis'].isin(['Bacterial infection', 'Viral infection'])]
    infection_counts = infection_df.groupby('Date').size().reset_index(name='count')
    fig = px.line(infection_counts, x='Date', y='count', title='Daily Infection Cases')
    return fig

# Callback for Anemia Distribution
@app.callback(
    Output('anemia-distribution', 'figure'),
    Input('anemia-distribution', 'relayoutData') # Dummy input
)
def update_anemia_distribution(relayoutData):
    anemia_df = df[df['Diagnosis'] == 'Anemia']
    anemia_age_gender = anemia_df.groupby(['Age', 'Gender']).size().reset_index(name='count')
    fig = px.bar(anemia_age_gender, x='Age', y='count', color='Gender', title='Anemia Cases by Age and Gender')
    return fig

# Callback for CRP Trends
@app.callback(
    Output('crp-trends', 'figure'),
    Input('crp-trends', 'relayoutData') # Dummy input
)
def update_crp_trends(relayoutData):
    crp_df = df.sort_values('Date')
    fig = px.line(crp_df, x='Date', y='CRP_mg_L', title='CRP Levels Over Time')
    return fig


if __name__ == '__main__':
    app.run(debug=True, port=8050)