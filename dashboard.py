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

# predata = attacktype(df, "Afghanistan")

app.layout = html.Div([
    html.H1(children='Informatie Visualisatie'),

    html.Div(children='''
        Groep A5 met Jop Rijksbaron, Milan Doodeman, Julien Coudron en Mark Muller.
    '''),

    dcc.Input(id='input-box1', value="Afghanistan", type='text'),
    dcc.Graph(id='output1'),
])


@app.callback(
    Output('output1', 'figure'),
    [Input('input-box1', 'value')]
)
def update_output_div(input_value):
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

if __name__ == '__main__':
    app.run_server(debug=True)
