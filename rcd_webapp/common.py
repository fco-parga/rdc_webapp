from PIL import Image
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

try:
    import dataiku
    is_dataiku = hasattr(dataiku, "Project")
except:
    is_dataiku = False

if is_dataiku:
    from tqdm import tqdm
    logos = dataiku.Folder("eT9PpYK1")
    slb_src=Image.open(logos.get_download_stream(path='/slb.png'))
    rcd_src=Image.open(logos.get_download_stream(path='/rcd.png'))
    dik_src=Image.open(logos.get_download_stream(path='/dataiku.png'))
    if_src=Image.open(logos.get_download_stream(path='/if.png'))
else:
    from tqdm.notebook import tqdm
    slb_src='assets/slb.png'
    rcd_src='assets/rcd.png'
    dik_src='assets/dataiku.png'
    if_src='assets/if.png'
    


def get_header():
    header = html.Div(
        children=[
                 html.A(
                    html.Img(
                            className="slb-logo",
                            src=slb_src,
                            style={'width': '150px','backgroundColor': '#FFFFFF', "margin-left": "15px"}),
                        href="https://www.slb.com/"),
                 html.H1(
                    children="Rock Cube Clusters APP",
                    style={
                        'backgroundColor': '#0014DC',
                        'color': '#FFFFFF',
                        'textAlign': 'center',
                        'display': 'inline-block',
                        'justify-content': 'center',
                        'align-items': "center",
                        'width':'100%',
                        'font-size': '55px'
                    },),
                html.A(
                    html.Img(
                            className="rcd-logo",
                            src=rcd_src,
                            style={'height': '105px',"margin-right": "15px"}),
                        href="https://www.slb.com/"),
        ],
        style={"display": "flex",
                   "align-items": "center",
                   "justify-content": "space-between",
                   "width": "100%",
                   'height':'147px',
                   'backgroundColor':'#0014DC'
                  },
        )
        

    return header

def get_menu():
    menu = html.Div(
        children=[
            dcc.Link('Home', href='Home', className="nav-link active custom-font", style={'color': 'white', 'margin-right': '25px', 'font-size': '25px'}),
            dcc.Link('Load data', href='Data', className="nav-link active custom-font", style={'color': 'white', 'margin-right': '25px', 'font-size': '25px'}),
            dcc.Link('Scan tanks', href='Tanks', className="nav-link active custom-font", style={'color': 'white', 'margin-right': '25px', 'font-size': '25px'}),
            dcc.Link('Scan benches', href='Benches', className="nav-link active custom-font", style={'color': 'white','margin-right': '25px', 'font-size': '25px'}),
            ], 
        className="nav nav-pills", style={'background-color': '#0014DC', 'border-radius': '1px', 'padding': '15px'})
    return menu


def get_footer():
    footer = html.Div(
        children=[
                 html.A(
                    html.Img(
                            className="dik-logo",
                            src=dik_src,
                            style={'height': '55px','backgroundColor': '#FFFFFF', "margin-left": "15px"}),
                        href="https://www.slb.com/"),
                 html.H4(
                    children="Domain Data Science Cohort II",
                    style={
                        'color': '#004788',
                        'textAlign': 'center',
                        'display': 'inline-block',
                        'justify-content': 'center',
                        'align-items': "center",
                        'width':'100%',
                    },),
                html.A(
                    html.Img(
                            className="if-logo",
                            src=if_src,
                            style={'height': '55px','backgroundColor': '#FFFFFF', "margin-right": "15px"}),
                        href="https://www.slb.com/"),
        ],
        style={"display": "flex",
                   "align-items": "center",
                   "justify-content": "space-between",
                   "width": "100%",
                   'height':'55px',
                   'position': 'fixed', 
                   'bottom': '0' 
                  },
        )

    return footer