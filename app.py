import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, Input, Output

# Load dataset
df = pd.read_csv("blood_reports_dataset.csv", parse_dates=['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Derive anemia flag
def anemia_flag(row):
    if row['Gender']=='M' and row['Haemoglobin_g_dl'] < 13: return 'Anemic'
    if row['Gender']=='F' and row['Haemoglobin_g_dl'] < 12: return 'Anemic'
    return 'Normal'
df['Anemia_Status'] = df.apply(anemia_flag, axis=1)

app = Dash(__name__)
app.title = "Corporate Blood Report Analytics Dashboard"

app.layout = html.Div([
    html.H1("Palkhade Diagnostics – Corporate Analytics", style={'textAlign':'center'}),

    html.Div([
        html.Label("Filter by Gender:"),
        dcc.Dropdown(
            ['All'] + sorted(df['Gender'].unique().tolist()), 'All',
            id='gender-filter', clearable=False, style={'width':'200px'}
        ),
        html.Label("Filter by Diagnosis:"),
        dcc.Dropdown(
            ['All'] + sorted(df['Diagnosis'].unique().tolist()), 'All',
            id='diagnosis-filter', clearable=False, style={'width':'250px'}
        )
    ], style={'display':'flex','justifyContent':'center','gap':'20px'}),

    dcc.Graph(id='crp-trend'),
    dcc.Graph(id='anemia-bar'),
    dcc.Graph(id='diagnosis-pie'),
    dcc.Graph(id='corr-heatmap'),

    html.H3("Filtered Data Table"),
    dash_table.DataTable(
        id='data-table',
        page_size=15,
        style_table={'overflowX': 'auto'},
        filter_action="native",
        sort_action="native"
    )
])

@app.callback(
    [Output('crp-trend','figure'),
     Output('anemia-bar','figure'),
     Output('diagnosis-pie','figure'),
     Output('corr-heatmap','figure'),
     Output('data-table','data'),
     Output('data-table','columns')],
    [Input('gender-filter','value'),
     Input('diagnosis-filter','value')]
)
def update_dashboard(gender_val, diagnosis_val):
    dff = df.copy()
    if gender_val != 'All':
        dff = dff[dff['Gender']==gender_val]
    if diagnosis_val != 'All':
        dff = dff[dff['Diagnosis']==diagnosis_val]

    # CRP trend
    crp_ts = dff.groupby('Date')['CRP_mg_L'].mean().reset_index()
    fig1 = px.line(crp_ts, x='Date', y='CRP_mg_L',
                   title="Average Daily CRP (mg/L) Trend")

    # Anemia prevalence
    anemia = dff.groupby(['Gender','Age']).Anemia_Status.value_counts(normalize=True).rename('prop').reset_index()
    anemia = anemia[anemia['Anemia_Status']=='Anemic']
    anemia['Age_Group'] = pd.cut(anemia['Age'], bins=[0,12,18,30,45,60,120],
                                 labels=['0-12','13-18','19-30','31-45','46-60','60+'])
    anemia_sum = anemia.groupby(['Age_Group','Gender'])['prop'].mean().reset_index()
    fig2 = px.bar(anemia_sum, x='Age_Group', y='prop', color='Gender', barmode='group',
                  title="Anemia Prevalence by Age Group & Gender", labels={'prop':'Proportion'})

    # Diagnosis distribution
    diag_counts = dff['Diagnosis'].value_counts().reset_index()
    diag_counts.columns = ['Diagnosis','Count']
    fig3 = px.pie(diag_counts, names='Diagnosis', values='Count', title="Diagnosis Distribution")

    # Correlation heatmap
    numeric_cols = dff.select_dtypes(include='number').columns
    corr = dff[numeric_cols].corr()
    fig4 = px.imshow(corr, text_auto=False, aspect='auto', title="Correlation Heatmap (Numeric Fields)")

    # Data table
    columns=[{"name": i, "id": i} for i in dff.columns]
    data=dff.to_dict('records')

    return fig1, fig2, fig3, fig4, data, columns

if __name__ == "__main__":
    app.run(debug=True)
