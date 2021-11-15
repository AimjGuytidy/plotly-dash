import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets = [dbc.themes.MINTY])

app.layout = html.Div(children=[
    dbc.Row([
        dbc.Col([
            html.H1("Poverty and Equity Database",
                   style={'color': 'magenta',
                         'fontSize':'40px'})],lg={'size':6,'offset':3},md=12),#end of column
        dbc.Col([
            html.H2("The World Bank")],lg=5,md=12),#end of column
        dbc.Col([
            html.P("Key Facts:")],lg={'size':5,'offset':5},md=12),#end of column
        dbc.Col([
            html.Ol([
                html.Li(["Number of Economies:",html.B("170")]),
                html.Li("Temporal Coverage: 1974-2019"),
                html.Li("Update Frequency: Quarterly"),
                html.Li("Last Updated: March 18, 2020"),
                html.Li(["Source:",
                         html.A(">>Check this link<<",href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database",target="_blank")])
            ])],lg={'size':5,'offset':6},md=12)#end of column
    ]),#end of row
    dbc.Row([
        dbc.Col([
            html.P("This is a demonstration of how columns and rows work")],
            lg={'size':5,'offset':3},
            md=12),
        dbc.Col([
            html.P("This is the partition of our row in different column")],
            lg=4,md=12)
    ])
    ])

if __name__=='__main__':
    app.run_server(debug=True)