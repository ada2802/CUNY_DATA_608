# -*- coding: utf-8 -*-
"""
Dash App Learning 

@author: Ada
"""
import dash
from dash.react import Dash

my_app = Dash('my app')

from dash_components import h1, PlotlyGraph, TextInput, div

my_app.layout = div([
    h1("Hello World"),
    TextInput(
        label='Stock Tickers',
        value='TSLA',
        id='my-input'
    ),
    PlotlyGraph(
        figure={
                'data':[
                        {'x':[1,2],'y':[3,1]}
                ]
        },
        id='my-graph'
    )        
])

my_app.server.run(debug=True)


app = dash.Dash()
app = dash.react.Dash('Dash Hello World')