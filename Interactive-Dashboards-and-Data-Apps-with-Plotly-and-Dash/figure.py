import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output,Input
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import re
import os
import plotly.express as px
from dash.exceptions import PreventUpdate
poverty_data = pd.read_csv('data\PovStatsData.csv')
regions = ['East Asia & Pacific', 'Europe & Central Asia', 'Fragile and conflict affected situations', 'High income',
'IDA countries classified as fragile situations', 'IDA total', 'Latin America & Caribbean', 'Low & middle income', 'Low income', 'Lower middle income', 'Middle East & North Africa', 'Middle income', 'South Asia',
'Sub-Saharan Africa', 'Upper middle income', 'World']
pop_df = poverty_data[(~poverty_data['Country Name'].isin(regions)) & (poverty_data['Indicator Name']=='Population, total')].copy()
poverty = pd.read_csv('data/poverty.csv',index_col=False,low_memory=False)
poverty.drop('Unnamed: 0',axis=1,inplace=True)
countries = poverty['Country Name'].values
gini = 'GINI index (World Bank estimate)'
gini_df = poverty[poverty[gini].notna()]
# poverty_data.head(3)
income_df = pd.read_csv("data/income_df.csv")
income_df.columns = [re.sub('Income share held by ', '', col).title() for col in income_df.columns]
income_df_cols = income_df.columns[:-2]
countries = income_df['Country Name'].unique()
perc_pov_cols =\
poverty.filter(regex='Poverty gap').columns
poverty1 = poverty.dropna(subset=['is_country'])
perc_pov_df = poverty1[poverty1['is_country'].dropna()].dropna(subset=perc_pov_cols)
perc_pov_year_col = sorted(set(perc_pov_df['year']))
cividis0 = px.colors.sequential.Cividis[0]

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.COSMO])
server = app.server
##################################
def make_empty_figure():
    fig = go.Figure()
    fig.layout.paper_bgcolor =  '#E5ECF6'
    fig.layout.plot_bgcolor = '#E5ECF6'
    return fig
def multiline_indic(indicator):
    final = []
    splits = indicator.split()
    for i in range(0,len(splits),3):
        final.append(' '.join(splits[i:i+3]))
    return '<br>'.join(final)

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
####################################################################################################################
#     dcc.Dropdown(id='country',
#                 options=[{'label':country,'value':country} for country in poverty_data['Country Name'].unique()]),
#     html.Br(),
#     html.Div(id='naming'),
#     html.Br(),
#     html.Div(id='report'),
######################################################################################################################
    html.Br(),
    dcc.Dropdown(id='dropy',value='2010',options=[{'label':year,'value':str(year)} for year in range(1974,2019)]),
    dcc.Graph(id='pop_graph',figure=make_empty_figure()),
    dbc.Row([
        dbc.Col([
        dbc.Label('Year'),   
        dcc.Dropdown(id='fig1',placeholder='select a year',options=[{'label':year,'value':year} for year in gini_df['year'].drop_duplicates().sort_values()]),
        dcc.Graph(id='fig01',figure=make_empty_figure())
            ]),
        dbc.Col([
            dbc.Label('Countries'),
            dcc.Dropdown(id='fig2',multi=True,placeholder='select one or multiple countries',options=[{'label':country,'value':country} for country in sorted(set(countries))]),
            dcc.Graph(id='fig02',figure=make_empty_figure())
            ]),
        dbc.Col([
            dbc.Label('Country'),
            dcc.Dropdown(id = 'input',placeholder='select a country',options=[{'label' : country,'value' : country} for country in countries ],value='Rwanda'),
            dcc.Graph(id='output',figure=make_empty_figure())
            ])
        ]),
    dbc.Row([
        dbc.Col(lg=1),
        dbc.Col([
            html.Br(),
            dbc.Label('select poverty level:'),
            dcc.Slider(id = 'perc_pov_p_slider',
               min=0,
               max = 2,
               step = 1,
               value=0,
               marks={0:{'label':'$1.9','style':{'color':cividis0,
                                                 'fontWeight':'bold'}},
                      1:{'label':'$3.2','style':{'color':cividis0,
                                                 'fontWeight':'bold'}},
                      2:{'label':'$5.5','style':{'color':cividis0,
                                                 'fontWeight':'bold'}}},
               included = False)],lg=2),
        dbc.Col([
            html.Br(),
            dbc.Label('select year:'),
            dcc.Slider(id = 'perc_pov_year_slider',
                       min=perc_pov_year_col[0],
                       max = perc_pov_year_col[-1],
                       step = 1,
                       value=2010,
                       marks={year:{'label':str(year),'style':{'color':cividis0}} for year in perc_pov_year_col[::5]},
                       included = False)],lg=5)
    ]),
    dcc.Graph(id='graph_slider',figure=make_empty_figure()),    
    dbc.Label("trial"),
    dcc.Dropdown(id = 'mapin',options=[{'label':indicator,'value':indicator} for indicator in poverty.columns[3:54]]),
    dcc.Graph(id='mapout',figure=make_empty_figure()),

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
    ],style={'backgroundColor':'#E5ECF6'})
###########################################################################################################################
# @app.callback(Output(component_id='naming',component_property='children'),
#               Input(component_id='country',component_property='value'))
# def show_name(country):
#     if country is None:
#         country = "No country was selected"
#     return html.B(country)
# @app.callback(Output(component_id='report',component_property='children'),
#               Input(component_id='country',component_property='value'))
# def show_info(country):
#     if country is None:
#         country = 'Not Yet'
#         return 'the country is not selected'
#     filt = poverty_data[(poverty_data['Country Name']==country)&(poverty_data['Indicator Name']=='Population, total')]
#     population = filt['2010'].values[0]
#     return f"The population of {country} in 2010 is {population:.0f}."   
#############################################################################################################################
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
    fig.layout.paper_bgcolor = '#E5ECF6'
    return fig 
@app.callback(Output(component_id='fig01',component_property='figure'),
             Input(component_id='fig1',component_property='value'))
def gini_year(year):
    if not year:
        raise PreventUpdate
    df = gini_df[gini_df['year'].eq(year)].sort_values(gini).dropna(subset=[gini])
    n_countries = len(df['Country Name'])
    fig = px.bar(df,x=gini,y='Country Name',
           title = ' '.join([gini,'-',str(year)]),
           height = 200 + (20*n_countries),
           orientation='h')
    fig.layout.paper_bgcolor = '#E5ECF6'
    return fig
@app.callback(Output(component_id='fig02',component_property='figure'),
             Input(component_id='fig2',component_property='value'))
def gini_c(country):
    if not country:
        raise PreventUpdate
    df = gini_df[gini_df['Country Name'].isin(country)].\
        dropna(subset=[gini])
    fig = px.bar(data_frame=df,y=gini,
                x='year',
                facet_row='Country Name',
                color='Country Name',
                title = '<br>'.join([gini,','.join(country)]),
                facet_row_spacing=0.12,
                labels = {gini:'GINI Index'},
                height = 100+250*len(country))
    fig.layout.paper_bgcolor = '#E5ECF6'
    return fig
@app.callback(Output('output','figure'),
             Input('input','value'))
def plota(country):
    if not country:
        raise PreventUpdate
    fig = px.bar(data_frame=income_df[income_df['Country Name']==country].dropna(),x = income_df_cols,y='Year',hover_name="Country Name",
             orientation='h',height=600,
             barmode='stack',
            title=f'Income Shares Quintiles - {country}')
    fig.layout.legend.orientation = 'h'
    fig.layout.legend.title = None
    fig.layout.legend.x = 0.35
    fig.layout.xaxis.title = 'Percent of Total Income'
    fig.layout.paper_bgcolor = '#E5ECF6'
    return fig
@app.callback(Output(component_id='graph_slider',component_property='figure'),
              Input(component_id='perc_pov_year_slider',component_property='value'),
              Input(component_id='perc_pov_p_slider',component_property='value'))
def plot_perv_pov(year,indicator):
    indicator = perc_pov_cols[indicator]
    df = (perc_pov_df[perc_pov_df['year'].eq(year)]
          .dropna(subset=[indicator])
          .sort_values(indicator))
    if df.empty:
        raise PreventUpdate
    fig = px.scatter(df,x = indicator,
                     y = 'Country Name',
                     color = 'Population, total',
                     size =[30]*len(df),
                     size_max=15,
                     hover_name='Country Name',
                     height=250+(20*len(df)),
                     color_continuous_scale='cividis',
                     title= indicator + '<b>: '+ f'{year}'+'</b>')
    fig.layout.paper_bgcolor = '#E5ECF6'
    fig.layout.xaxis.ticksuffix = '%'
    return fig
@app.callback(Output(component_id='mapout',component_property='figure'),
             Input(component_id='mapin',component_property='value'))
def mapping(indicator):
    if indicator == None:
        raise PreventUpdate
    df = poverty[poverty['is_country']==True]
    fig = px.choropleth(data_frame=df,
              locations="Country Code",
              hover_name='Country Name',
              title = indicator,
              color=indicator,
              color_continuous_scale='cividis',
              animation_frame='year',
              height=700)
    fig.layout.geo.showframe = False
    fig.layout.geo.showcountries = True
    fig.layout.geo.projection.type = 'natural earth'
    fig.layout.geo.lataxis.range = [-53,76]
    fig.layout.geo.lonaxis.range = [-137,168]
    fig.layout.geo.landcolor = 'white'
    fig.layout.geo.bgcolor = '#E5ECF6'
    fig.layout.paper_bgcolor = '#E5ECF6'
    fig.layout.geo.countrycolor = 'gray'
    fig.layout.geo.coastlinecolor = 'gray'
    fig.layout.coloraxis.colorbar.title = multiline_indic(indicator)
    return fig
if __name__ == '__main__':
    app.run_server(debug=True,port=8060)
            
                