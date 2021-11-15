import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SUPERHERO])

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
   
if __name__ == '__main__':
    app.run_server(debug=True)
            
                