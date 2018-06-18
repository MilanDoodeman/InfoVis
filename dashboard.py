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

app.layout = html.Div(children=[
    html.H1(children='Informatie Visualisatie'),

    html.Div(children='''
        Groep A5 met Jop Rijksbaron, Milan Doodeman, Julien Coudron en Mark.
    '''),
    dcc.Graph(
        id='Nationality of terrorists in the given country',
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
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
