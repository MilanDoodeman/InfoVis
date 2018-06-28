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
# app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.layout = html.Div([
    html.H1(children='Dashboard Terrorism Database', style={'margin-left': '32%'}),

    html.Div([
            'Choose country (donut & bar chart):'
    ], style={'margin-left': '35%', 'display': "inline-block", 'font-family': 'Open Sans', 'padding': '6px', 'font-weight': 'bold '}),

    html.Div([
        dcc.Input(id='input-box1', value="Netherlands", type='text', style={'height': '38px',
        'padding': '6px',
        'background-color': '#fff',
        'border': '1px solid #D1D1D1',
        'border-radius': '4px',
        'box-shadow': 'none',
        'box-sizing': 'border-box',
        'font-family': "Open Sans",
        'font-size': 'inherit',
        'display': 'inline-block',
        'margin-left': '35%'})]),

    html.Div([
        html.Div([
            dcc.Graph(id='output1', style={'float': 'left', 'width': '50%', 'margin-left': '10%', 'margin-bottom': '-20%', 'margin-top': '-23%'})
        ]),

        html.Div([
            dcc.Graph(id='output2', style={'float': 'right', 'width': '5%', 'margin-right': '-18%', 'margin-top': '-13%'})
        ]),

        html.Div([
            dcc.Graph(id='worldmap'),
        ], style={'float': 'left', 'margin-left': '8%', 'margin-top': '2%', 'padding': '0px'}),

        html.Div([
            'Display type for Barchart:'
        ], style={'margin-top': '-2%', 'margin-right': '-100%', 'margin-left': '135%', 'font-family': 'Open Sans', 'font-weight': 'bold '}),

        html.Div([
            dcc.RadioItems(
                id="choice2",
                options=[
                {'label': 'Aantal doden per aanslagtype    ', 'value': 'deaths'},
                {'label': 'Aantal aanslagen per aanslagtype', 'value': 'attacks'},
                ],
                value='deaths',
                #labelStyle={'display': 'block'}
        )], style={'margin-top': '0%', 'margin-right': '-100%', 'margin-left': '135%'}),

        html.Div([
            'Type of Worldmap:'
        ], style={'margin-top': '2%', 'margin-right': '-100%', 'margin-left': '108%', 'font-family': 'Open Sans', 'font-weight': 'bold'}),

        html.Div([
            dcc.Dropdown(
                id="choice1",
                options=[
                    {'label': 'Aantal doden', 'value': 'Doden'},
                    {'label': 'Aantal aanslagen', 'value': 'Aanslagen'},
                    {'label': 'Ratio', 'value': 'Ratio'}
                ],
                value='Doden',
                #labelStyle={'display': 'block'}
        )], style={'margin-top': '0%', 'margin-right': '-100%', 'margin-left': '108%', 'width': '30%'}),

        html.Div([
            'Display type for Worldmap:'
        ], style={'margin-top': '3%', 'margin-right': '-100%', 'margin-left': '100%', 'font-family': 'Open Sans', 'font-weight': 'bold'}),

        html.Div([
            dcc.RadioItems(
            id='displaychoice',
            options=[
                {'label': 'Locatie van de aanslag(en)','value': 'Locatie'},
                {'label': 'Aantal aanslagen/doden van de aanslag','value': 'Aantal'}
            ],
            value='Locatie',
            labelStyle={'display': 'block'}
        )], style={'margin-top': '0%', 'margin-right': '-100%', 'margin-left': '100%'}),

        html.Div([
            dcc.Slider(
                id='slider',
                min=1970,
                max=2015,
                marks={i:str(i) for i in range(1970, 2015, 2)},
                value=2002
            ),
        ], style= {'float': 'left', 'width': '90%', 'margin-top': '-12%', 'margin-left': '10%'}),

    ], style={'display': 'table'}),

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
                    values=dataternat[1],
                    hole=0.5
                )
            ],
            "layout": {
                'title': "Nationality of terrorists in {}" .format(input_value),
            }
        }
@app.callback(
    Output('output2', 'figure'),
    [Input('input-box1', 'value'),
    Input('choice2','value')]
)
def update_output_2(input_value, choice):
    predata = attacktype(df, str(input_value), choice)
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
                'barmode': "stack",
                'width': '100%',
                'height': '100%',
                'xaxis': {'title': 'Years'},
                'yaxis': {'title': 'Total of {}'.format(choice)}
                }
          }

@app.callback(
    Output('worldmap', 'figure'),
    [Input('slider', 'value'),
    Input('choice1', 'value'),
    Input('displaychoice', 'value')]

)
def update_worldmap(slider, choice, display):
    worldmapdata = worldmap(df, int(slider), str(choice), str(display))
    return {'data': worldmapdata[1], 'layout': worldmapdata[0]}

if __name__ == '__main__':
    app.run_server(debug=True)
