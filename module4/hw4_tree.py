# -*- coding: utf-8 -*-
"""
Module 4

In this module we’ll be looking at data from the New York City tree census:
    
https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh

This data is collected by volunteers across the city, and is meant to catalog information
about every single tree in the city.

Build a dash app for a arborist studying the health of various tree species (as defined by the
variable ‘spc_common’) across each borough (defined by the variable ‘borough’). This
arborist would like to answer the following two questions for each species and in each
borough:
    
    
Learn Dash app python code from:
https://www.youtube.com/watch?v=sea2K4AuPOk
https://www.youtube.com/watch?v=5BAthiN0htc    

@author: Ada
"""


#import dash app package 
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import datetime
from datetime import date


#read data from url
url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json')
df = pd.read_json(soql_url)
#df.shape
#df.info()

#For more analysis
# - conver created datetime format to date formate
df["created_%y-%m"] = pd.to_datetime(df['created_at']).dt.year.map(str) +"-"+pd.to_datetime(df['created_at']).dt.month.map(str)


#create Dash app 
app = dash.Dash()


"""
1. What proportion of trees are in good, fair, or poor health according to the ‘health’
variable?
"""


app.layout = html.Div([
    html.Div(id='output-text',children=''),
    
    #dropdown manuel
    dcc.Dropdown(
        id='my-dropdown-widget',
        value='Montreal',
        #auto updater the dropdown 
        options=[
            {'label':i, 'value':i} for i in 
            df.spc_common.unique()
        ]        
    ),
    
    dcc.Graph(id='indicator-graphic'),
    
    #Time-series data
    dcc.Slider(
        id='year_month--slider',
        min=df["created_%y-%m"].min(),
        max=df["created_%y-%m"].max(),
        value=df["created_%y-%m"].max(),
        step=None,
        marks={str(year_month): str(year_month)
            for year_month in df["created_%y-%m"].unique()}
    )

])
# get input values from user and sent to Dash app for two dropdown manuels
# --one for 'spc_common’ and one for 'borough’
@app.callback(
    Output('my-graph','figure'),
    [Input('my-dropdown-tree','value'),
     Input('my-dropdown-boro','value'),
     Input('year_month--slider','value')]
)
def update_text(selected_tree,selected_boro ):
    return ( #select common name of tree
            'You select "{}" tree in {}'
    ).format(
        selected_spc_common,
        selected_borough
    )
    
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_month_value):
    dff = df[df["created_%y-%m"] == year_month_value]
    
    return {
        'data': [go.Scatter(
                x=dff[dff['health'] == xaxis_column_name],
                y=dff[dff['Indicator Name'] == yaxis_column_name],
                text=dff[dff['Indicator Name'] == ],
                type='sxcatter',
                mode='markers',
        )]
    }
    
if _name_ == '_main_':
    app.run_server(debug=True, port=8054)






















#++++++++++++++++++++++++++++++++




"""
2. Are stewards (steward activity measured by the ‘steward’ variable) having an impact
on the health of trees?
"""






import pandas as pd
import numpy as np


url = 'https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh'
trees = pd.read_json(url)
trees.head(10)

trees.shape

firstfive_url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json?$limit=5&$offset=0'
firstfive_trees = pd.read_json(firstfive_url)
firstfive_trees


nextfive_url = 'https://data.cityofnewyork.us/resource/nwxe-4ae8.json?$limit=5&$offset=5'
nextfive_trees = pd.read_json(nextfive_url)
nextfive_trees


boro = 'Bronx'
soql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
        '$select=spc_common,count(tree_id)' +\
        '&$where=boroname=\'Bronx\'' +\
        '&$group=spc_common').replace(' ', '%20')
soql_trees = pd.read_json(soql_url)

soql_trees



'https://api-url.com/?query with spaces'.replace(' ', '%20')


