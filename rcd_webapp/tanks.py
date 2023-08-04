from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.graph_objs as go

from rcd_webapp import common

#from app import app
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

layout = html.Div([
    html.H3('Scatter Chart'),    
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x = random_x,
                    y = random_y,
                    mode = 'markers',
                   
                )                
            ],
        }
    ),

    common.get_footer(),
  
])
