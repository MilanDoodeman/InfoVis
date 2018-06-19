# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from datafuncties import *

app = dash.Dash()

df = pd.read_csv('globalterrorismdb_0616dist.csv', encoding = "cp1252")
dataternat = terroristnationality("Afghanistan", df)
predata = attacktype(df, "Afghanistan")

app.layout = html.Div(children=[
    html.H1(children='Informatie Visualisatie'),

    html.Div(children='''
        Groep A5 met Jop Rijksbaron, Milan Doodeman, Julien Coudron en Mark Muller.
    '''),

    dcc.Graph(
        id='terrorist nationality',
        figure={
            'data': [
                go.Pie(
                    labels=dataternat[0],
                    values=dataternat[1]
                )
            ],
            "layout": {
                'title': "Nationality of terrorists in the given country"
            }
        }
    ),
    dcc.Graph(
        id='kills against type of attack',
        figure={
            'data': [
                {'x': predata[0], 'y': predata[1][0], 'type': 'bar', 'name': predata[2][0]},
                {'x': predata[0], 'y': predata[1][1], 'type': 'bar', 'name': predata[2][1]},
                {'x': predata[0], 'y': predata[1][2], 'type': 'bar', 'name': predata[2][2]},
                {'x': predata[0], 'y': predata[1][3], 'type': 'bar', 'name': predata[2][3]},
                {'x': predata[0], 'y': predata[1][4], 'type': 'bar', 'name': predata[2][4]},
                {'x': predata[0], 'y': predata[1][5], 'type': 'bar', 'name': predata[2][5]},
                {'x': predata[0], 'y': predata[1][6], 'type': 'bar', 'name': predata[2][6]},
                {'x': predata[0], 'y': predata[1][7], 'type': 'bar', 'name': predata[2][7]},
                {'x': predata[0], 'y': predata[1][8], 'type': 'bar', 'name': predata[2][8]},
                
            ],
            'layout': {
                'title': 'Attack Type through the years in kills per attack type',
                'barmode': "stack"
                }
          })
])

if __name__ == '__main__':
    app.run_server(debug=True)
