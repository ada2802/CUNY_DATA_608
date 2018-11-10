# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 22:54:25 2018

https://www.youtube.com/watch?v=J_Cy_QjG6NE&list=PLQVvvaa0QuDfsGImWNt1eUEveHOepkjqt



@author: Ada
"""

#pip install dash dash-renderer dash-html-components dash-core-coponents plotly
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div("Dash tutorials")

if __name == '__man__':
    app.run_server(debug=True)
    