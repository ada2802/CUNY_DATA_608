# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:02:58 2018

@author: Ada
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


import pandas as pd
df = pd.read_csv('filename.csv')

app = dash.Dash()

app.layout = html.Div([
    html.Div(id='output-text',children=''),
    
    #dropdown manuel
    dcc.Dropdown(
        id='my-dropdown-widget',
        value='Montreal',
        #auto updater the dropdown 
        options=[
            {'label':i, 'value':i} for i in 
            df.country.unique()
        ]        
    )

    """
    #style from css
    style={
            'color':'white',
            'backgroud-color': 'rgb(63,63,63)
    },
    """
    #css
    children=[
            html.H1(
                'hello scipy',
                style = {'test-align':'center'}
            )]
    html.h1,
    dcc.Markdown(
            
    ),
    
    dcc.Graph(
            id = 'graph',
            figure = {
                    'data':[
                            #add graph 
                            go.Scatter(
                                    x=df.lifeExp,
                                    y=df.gdpPercep,
                                    text=df.country,
                                    type='scatter',
                                    mode='markers'
                            )
                    ]
            }
    ),
    
    dcc.slider
    
    #disply table
    Table(df)
])
            
            
@app.callback(
    Output('output-text','children'),
    [Input('my-dropdown-widget','value')]
)
def update_text(selected_value):
    return (
            'Avg GDP per Capita of "{}" since {} is {}'
    ).format(
        selected_value,
        df.year.min(),
        df[df.country == selected_value]\.gdpPercap.mean()
    )
    
if _name_ == '_main_':
    app.run_server(debug=True)

