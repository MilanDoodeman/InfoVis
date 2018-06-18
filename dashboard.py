# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

df = df = pd.read_csv('globalterrorismdb_0616dist.csv', encoding = "cp1252")

app.layout = html.Div(children=[
    html.H1(children='Informatie Visualisatie'),

    html.Div(children='''
        Groep A5 met Jop RIjksbaron, Milan Doodeman, Julien Coudron en Mark.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 3, 5], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 3, 5], 'y': [2, 4, 5], 'type': 'bar'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
