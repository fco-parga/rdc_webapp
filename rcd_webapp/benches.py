from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from rcd_webapp import common

#from app import app

layout = html.Div([    
    html.H3('Bar Chart'),    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    common.get_footer(),
  
])