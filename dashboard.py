# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from datafuncties import *

app = dash.Dash()

df = pd.read_csv('globalterrorismdb_0616dist.csv', encoding = "cp1252")

app.layout = html.Div([
    html.H1(children='Informatie Visualisatie'),

    html.Div(children='''
        Groep A5 met Jop Rijksbaron, Milan Doodeman, Julien Coudron en Mark Muller.
    '''),

    dcc.Input(id='input-box1', value="Afghanistan", type='text'),
    dcc.Graph(id='output1'),
    dcc.Graph(id='output2'),
    html.Label('Slider'),
    dcc.Slider(
        id='slider',
        min=1970,
        max=2015,
        marks={i:str(i) for i in range(1970, 2015)},
        value=2002,
    ),
    dcc.Graph(id='worldmap')
])


@app.callback(
    Output('output1', 'figure'),
    [Input('input-box1', 'value')]
)
def update_output_1(input_value):
    dataternat = terroristnationality(str(input_value), df)
    return {
            'data': [
                go.Pie(
                    labels=dataternat[0],
                    values=dataternat[1]
                )
            ],
            "layout": {
                'title': "Nationality of terrorists in {}" .format(input_value)
            }
        }
@app.callback(
    Output('output2', 'figure'),
    [Input('input-box1', 'value')]
)
def update_output_2(input_value):
    predata = attacktype(df, str(input_value))
    return {
            'data': [
                {'x': predata[0], 'y': predata[1][0], 'type': 'bar', 'name': predata[2][0]},
                {'x': predata[0], 'y': predata[1][1], 'type': 'bar', 'name': predata[2][1]},
                {'x': predata[0], 'y': predata[1][2], 'type': 'bar', 'name': predata[2][2]},
                {'x': predata[0], 'y': predata[1][3], 'type': 'bar', 'name': predata[2][3]},
                {'x': predata[0], 'y': predata[1][4], 'type': 'bar', 'name': predata[2][4]},
                {'x': predata[0], 'y': predata[1][5], 'type': 'bar', 'name': predata[2][5]},
                {'x': predata[0], 'y': predata[1][6], 'type': 'bar', 'name': predata[2][6]},
                {'x': predata[0], 'y': predata[1][7], 'type': 'bar', 'name': predata[2][7]},
                {'x': predata[0], 'y': predata[1][8], 'type': 'bar', 'name': predata[2][8]}
            ],
            'layout': {
                'title': 'Attack Type through the years in kills per attack type in {}' .format(input_value),
                'barmode': "stack"
                }
          }

@app.callback(
    Output('worldmap', 'figure'),
    [Input('slider', 'value')]
)
def update_worldmap(input_value):
    worldmapdata = worldmap(df, int(input_value))
    return {'data': worldmapdata[1], 'laytout': worldmapdata[1]}

if __name__ == '__main__':
    app.run_server(debug=True)
