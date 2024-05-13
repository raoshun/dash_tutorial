# Path: app.py
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv('data/data_sample.csv')
vars_cat = [var for var in df.columns if var.startswith('cat')]
vars_cont = [var for var in df.columns if var.startswith('cont')]

pie = df.groupby('target').count()['id'] / len(df)

fig_pie = go.Figure(
    data=[go.Pie(labels=list(pie.index),
                 values=pie.values,
                 hole=.3,
                 marker=dict(colors=['#bad6eb', '#2b7bba']))])

fig_pie.update_layout(
    width=320,
    height=250,
    margin=dict(l=30, r=10, t=10, b=10),
    paper_bgcolor='rgba(0,0,0,0)',
)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Settings',
                        style={'margin-top': '12px', 'margin-left': '24px'})
                ],
            style={"height": "5vh"},
            className='bg-primary text-white font-italic'
            ),
        dbc.Row(
            [
                html.Div([
                    html.P('Categorical Variable',
                        style={'margin-top': '8px', 'margin-bottom': '4px'},
                        className='font-weight-bold'),
                    dcc.Dropdown(id='my-cat-picker', multi=False, value='cat0',
                                options=[{'label': x, 'value': x}
                                        for x in vars_cat],
                                style={'width': '320px'}
                                ),
                    html.P('Continuous Variable',
                        style={'margin-top': '16px', 'margin-bottom': '4px'},
                        className='font-weight-bold'),
                    dcc.Dropdown(id='my-cont-picker', multi=False, value='cont0',
                                options=[{'label': x, 'value': x}
                                        for x in vars_cont],
                                style={'width': '320px'}
                                ),
                    html.P('Continuous Variables for Correlation Matrix',
                        style={'margin-top': '16px', 'margin-bottom': '4px'},
                        className='font-weight-bold'),
                    dcc.Dropdown(id='my-corr-picker', multi=True,
                                value=vars_cont + ['target'],
                                options=[{'label': x, 'value': x}
                                        for x in vars_cont + ['target']],
                                style={'width': '320px'}
                                ),
                    html.Button(id='my-button', n_clicks=0, children='apply',
                                style={'margin-top': '16px'},
                                className='bg-dark text-white'),
                    html.Hr()
                    ]
                    )
                ],
            style={'height': '50vh', 'margin': '8px'}),
        dbc.Row(
            [
                html.P('Target Variables', className='font-weight-bold'),
                dcc.Graph(figure=fig_pie)
                ],
            style={"height": "45vh", 'margin': '8px'}
            )
        ]
    )

content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Distribution of Categorical Variable'),
                        ],
                    className='bg-white'
                    ),
                dbc.Col(
                    [
                        html.P('Distribution of Continuous Variable')
                    ],
                    className='bg-dark text-white'
                    )
            ],
            style={"height": "50vh"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Correlation Matrix Heatmap')
                    ],
                    className='bg-light'
                    )
            ],
            style={"height": "50vh"}
            )
        ]
)

app.layout = app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
                ],
            style={"height": "100vh"}
            ),
        ],
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
