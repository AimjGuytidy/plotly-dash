import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output,Input
import pandas as pd
import plotly.graph_objects as go
import numpy as np

poverty_data = pd.read_csv('data\PovStatsData.csv')
regions = ['East Asia & Pacific', 'Europe & Central Asia', 'Fragile and conflict affected situations', 'High income',
'IDA countries classified as fragile situations', 'IDA total', 'Latin America & Caribbean', 'Low & middle income', 'Low income', 'Lower middle income', 'Middle East & North Africa', 'Middle income', 'South Asia',
'Sub-Saharan Africa', 'Upper middle income', 'World']
pop_df = poverty_data[(~poverty_data['Country Name'].isin(regions)) & (poverty_data['Indicator Name']=='Population, total')].copy()

# poverty_data.head(3)
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.MINTY])
# app = JupyterDash(__name__)
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1("Poverty and Equity Database",
                    style={'color':'magenta',
                           'fonSize':'40px'})],
            lg = 12,md=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("The World Bank",
                    style={'fontSize':'30px'})],
            lg = {'size':6,
                  'offset':3},
            md=12)
    ]),
    dcc.Dropdown(id='country',
                options=[{'label':country,'value':country} for country in poverty_data['Country Name'].unique()]),
    html.Br(),
    html.Div(id='naming'),
    html.Br(),
    html.Div(id='report'),
    html.Br(),
    dcc.Dropdown(id='dropy',value='2010',options=[{'label':year,'value':str(year)} for year in range(1974,2019)]),
    dcc.Graph(id='pop_graph'),
    dbc.Tabs([
        dbc.Tab([
            dbc.Col([
                html.Ol([
                    html.Li(["Number of Economies:",html.B("170")]),
                    html.Li("Temporal Coverage: 1974-2019"),
                    html.Li("Update Frequency: Quarterly"),
                    html.Li("Last Updated: March 18, 2020"),
                    html.Li(["Source:",
                            html.A(">>Check this link<<",href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database",target="_blank")])
                ])],lg={'size':5},md=12)],label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book:Intro to plotly'),
                html.Li(['Source:',
                       html.A("Book's github repo",href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash",target="_blank")])])],
            label='Project Info')
        ])
    ])
@app.callback(Output(component_id='naming',component_property='children'),
              Input(component_id='country',component_property='value'))
def show_name(country):
    if country is None:
        country = "No country was selected"
    return html.B(country)
@app.callback(Output(component_id='report',component_property='children'),
              Input(component_id='country',component_property='value'))
def show_info(country):
    if country is None:
        country = 'Not Yet'
        return 'the country is not selected'
    filt = poverty_data[(poverty_data['Country Name']==country)&(poverty_data['Indicator Name']=='Population, total')]
    population = filt['2010'].values[0]
    return f"The population of {country} in 2010 is {population:.0f}."    
@app.callback(Output(component_id='pop_graph',component_property='figure'),
             Input(component_id='dropy',component_property='value'))
def plot_countries_by_pop(year):
    year_dfy = pop_df[['Country Name',year]].sort_values(year,ascending=False)[:20]
    fig = go.Figure()
    fig.update_layout(template='ggplot2')
    fig.add_bar(x=year_dfy['Country Name'],y=year_dfy[year])
    fig.layout.title = f'Top twenty countries by population-{year}'
    fig.layout.title.pad = {'b' : 90, 'l' : 300, 'r' : 50}
    
#     fig.show()
    return fig 
if __name__ == '__main__':
    app.run_server(debug=True,port=8060)
            
                