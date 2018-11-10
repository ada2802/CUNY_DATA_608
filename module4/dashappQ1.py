# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:14:34 2018

@author: chunhui zhu
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np



def get_data(boro):
    health_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
            '$select=spc_common,health,count(spc_common)' +\
            '&$where=boroname=\''+ str(boro) +'\'' +\
            '&$group=spc_common,health' )
    #print (health_url)
    df = pd.read_json(health_url)
    df2=df.pivot_table(values='count_spc_common', index='spc_common', columns='health')
    df2['total']=df2.sum(axis=1)
    df2.fillna(0, inplace=True)
    df2['Fair_perc']=df2['Fair']/df2['total']
    df2['Good_perc']=df2['Good']/df2['total']
    df2['Poor_perc']=df2['Poor']/df2['total']
    df3=df2[['Fair_perc','Good_perc','Poor_perc']]
    return (df3)

Bronxdf=get_data('Bronx')
Manhattandf=get_data('Manhattan')
Brooklyndf=get_data('Brooklyn')
Queensdf=get_data('Queens')
StatenIslanddf=get_data('Staten%20Island')


    

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='New York City Tree Census'),

    html.Div(children='''
        Dash: Health condition in Boro: .
    '''),

    dcc.Graph(
        id='Bronx',
        figure={
            'data': [
                {'x': Bronxdf.index, 'y': Bronxdf['Fair_perc'].values, 'type': 'bar', 'name': 'Fair_perc'},
                {'x': Bronxdf.index, 'y': Bronxdf['Good_perc'].values, 'type': 'bar', 'name': 'Good_perc'},
                {'x': Bronxdf.index, 'y': Bronxdf['Poor_perc'].values, 'type': 'bar', 'name': 'Poor_perc'},
              
            ],
            'layout': {
                'title': 'Dash Data Visualization Bronx'
            }
        }
    ),
    
    dcc.Graph(
        id='Manhattan',
        figure={
            'data': [
                {'x': Manhattandf.index, 'y': Manhattandf['Fair_perc'].values, 'type': 'bar', 'name': 'Fair_perc'},
                {'x': Manhattandf.index, 'y': Manhattandf['Good_perc'].values, 'type': 'bar', 'name': 'Good_perc'},
                {'x': Manhattandf.index, 'y': Manhattandf['Poor_perc'].values, 'type': 'bar', 'name': 'Poor_perc'},
              
            ],
            'layout': {
                'title': 'Dash Data Visualization Manhattan'
            }
        }
    ),
    
    dcc.Graph(
        id='Brooklyn',
        figure={
            'data': [
                {'x': Brooklyndf.index, 'y': Brooklyndf['Fair_perc'].values, 'type': 'bar', 'name': 'Fair_perc'},
                {'x': Brooklyndf.index, 'y': Brooklyndf['Good_perc'].values, 'type': 'bar', 'name': 'Good_perc'},
                {'x': Brooklyndf.index, 'y': Brooklyndf['Poor_perc'].values, 'type': 'bar', 'name': 'Poor_perc'},
              
            ],
            'layout': {
                'title': 'Dash Data Visualization Brooklyn'
            }
        }
    ),
    
    dcc.Graph(
        id='Queens',
        figure={
            'data': [
                {'x': Queensdf.index, 'y': Queensdf['Fair_perc'].values, 'type': 'bar', 'name': 'Fair_perc'},
                {'x': Queensdf.index, 'y': Queensdf['Good_perc'].values, 'type': 'bar', 'name': 'Good_perc'},
                {'x': Queensdf.index, 'y': Queensdf['Poor_perc'].values, 'type': 'bar', 'name': 'Poor_perc'},
              
            ],
            'layout': {
                'title': 'Dash Data Visualization Queens'
            }
        }
    ),
    
    dcc.Graph(
        id='Staten Island',
        figure={
            'data': [
                {'x': StatenIslanddf.index, 'y': StatenIslanddf['Fair_perc'].values, 'type': 'bar', 'name': 'Fair_perc'},
                {'x': StatenIslanddf.index, 'y': StatenIslanddf['Good_perc'].values, 'type': 'bar', 'name': 'Good_perc'},
                {'x': StatenIslanddf.index, 'y': StatenIslanddf['Poor_perc'].values, 'type': 'bar', 'name': 'Poor_perc'},
              
            ],
            'layout': {
                'title': 'Dash Data Visualization Staten Island'
            }
        }
    ),
    
])

    
    
#http://127.0.0.1:8050/ (Press CTRL+C to quit)
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    