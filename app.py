# Path: app.py
import dash
from dash import dcc, html
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
# app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
