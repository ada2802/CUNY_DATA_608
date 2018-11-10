# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:14:34 2018

@author: John
"""

import dash
import dash_core_components as dcc
import dash_html_components as html


import pandas as pd
import numpy as np


def getData(Boro):
    groupByHealth = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?$select=spc_common,health,count(spc_common)&$where=boroname=\''+ str(Boro) +'\'&$group=spc_common,health' )

    df = pd.read_json(groupByHealth)
    
    return df

x = getData("Manhattan")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='NYC Tree Popuplation'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x.spc_common, 'y': x.loc[ x['health'] == 'Good', 'count_spc_common'] , 'type': 'bar', 'name': 'Good'},
                {'x': x.spc_common, 'y': x.loc[ x['health'] == 'Fair', 'count_spc_common'], 'type': 'bar', 'name': 'Fair'},
                {'x': x.spc_common, 'y': x.loc[ x['health'] == 'Poor', 'count_spc_common'], 'type': 'bar', 'name': 'Poor'},
                
                ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)