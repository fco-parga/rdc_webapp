import os
from dash import Dash, html, dcc, callback, Output, Input, State, no_update
import dash_bootstrap_components as dbc
from dash import callback_context as ctx
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from shapely.geometry import LineString
import geopandas as gpd
import contextily as cx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from PIL import Image

from rcd_webapp import common

try:
    import dataiku
    is_dataiku = hasattr(dataiku, "Project")
except:
    is_dataiku = False

from rcd.well_dataiku import WellsDataIku

PATH_DATA = 'data'
loading = False
wells_list_dataiku = []
img_data = io.BytesIO()

layout = html.Div([
        dcc.Store(id="loaded_wells", data=-1),
        dcc.Store(id="image_store", storage_type="local", data=-1),
        dbc.Row([
                dbc.Col([
                    dbc.Card([
                            dbc.CardHeader("Data Source Selection"),
                            dbc.CardBody([
                                dbc.Label("Input type"),
			                    dcc.Dropdown(id ="data_source_selection", style = {"minWidth":"100%", "marginBottom":"10px"},
                                             multi = False, clearable = False, options = sorted(['csv','snowflake']), value = "csv"),
                                # Wrap the button with a Loading component and set the type attribute
                                dcc.Loading(
                                    id="ls-loading-button",
                                    children=[dbc.Button("Load", id='load_data_now', outline=True, color="success", className="me-2 m-2")],
                                    type="default"
                                )
                                ])
                    ],className="mb-3"),
                    dbc.Card(id="wells-information"),

                ],md=1,style={"text-align": "center"}),
                dbc.Col([dbc.Label('Available data',id='display_wells',style={'color': 'black', 'margin-right': '25px', 'font-size': '25px'}, className="custom-label"),
                         # Wrap the graph with a Loading component and set the type attribute
                         dcc.Loading(
                             id="ls-loading-graph",
                             children=[dcc.Store(id="loaded_wells_store",data=-1),
                                       dcc.Graph(id="selected_data_plot",config={'editable': True,'edits': {'shapePosition': True, 'titleText': False, 'axisTitleText': False}}),
                                       html.Img(className="plot_image",)],
                             type="circle"
                         )],md=11)
                ], style={"padding":"2%", "text-align": "center"},className="g-2"),
        common.get_footer(),
    ])

@callback(
    [Output('ls-loading-graph', 'children'), Output('image_store', 'data'), Output('wells-information', 'children')],
    [Input('load_data_now', 'n_clicks'), Input('data_source_selection', 'value')],
    State('loaded_wells', 'data'),
    prevent_initial_call=True
)

def update_graph(load_data_now, data_source_selection,loading_state):
    # Check if the loaded_wells data is valid or not
    global loading
    global wells_list_dataiku
    global img_data
    triggered_input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_input_id=='load_data_now' and data_source_selection=='csv' and not loading:
        print('Loading data')
        loading = True
        wells_list_dataiku = WellsDataIku.load_wells_data(wells_data_df)
        print('Abailable wells: ',len(wells_list_dataiku))
        
        wells_sublist_dik = [well for well in wells_list_dataiku if isinstance(well.survey_linestring,LineString)]
        wells_linestrings_df = WellsDataIku.to_df(wells_sublist_dik)[['wellid','survey_linestring']]
        wells_linestrings_gdf = gpd.GeoDataFrame(wells_linestrings_df, geometry='survey_linestring', crs="EPSG:4326")

        fig, ax = plt.subplots(figsize=(15, 15)) # create a figure and an axes object 
        wells_linestrings_gdf.plot(ax=ax, alpha=0.5, edgecolor='k') # plot the well data on the axes object 
        cx.add_basemap(ax, zoom=12, crs=wells_linestrings_gdf.crs) # add a basemap to the axes object 
        ax.set_axis_off() # remove the axis labels and ticks

        fig.savefig(img_data, format='png', bbox_inches='tight')# save the figure to the BytesIO object 
        img_data.seek(0) # rewind the data

        print('Wells to plot: ', len(wells_sublist_dik))
        img_html = html.Img(src=Image.open(img_data))

        wells_info = html.Div([
                        html.Div([dbc.Label("Total wells: "), dbc.Label(str(len(wells_list_dataiku)))]),
                        html.Div([dbc.Label("Horizontal wells: "), dbc.Label(str(len(wells_sublist_dik)))]),
        ])
        loading = False
        return img_html, img_html, wells_info

if is_dataiku:
    wells_data = dataiku.Dataset("wells_data")
    wells_data_df = wells_data.get_dataframe()
else:
    wells_data_df = pd.read_csv(os.path.join(PATH_DATA, 'wells_data_df.csv'))
