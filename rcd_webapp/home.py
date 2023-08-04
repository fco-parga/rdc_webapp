from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from rcd_webapp import common

#from app import app


layout = html.Div([
    html.H3('This is home screen'),
    common.get_footer(),
])
