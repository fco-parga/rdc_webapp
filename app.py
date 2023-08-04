import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from rcd_webapp import home, data, tanks, benches, common

def start_app(app):

    dbc_css = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
    #app = Dash(__name__, external_stylesheets=[dbc_css])

    app.scripts.config.serve_locally = True
    app.css.config.serve_locally = True
    app.config.external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
    app.config.suppress_callback_exceptions = True


    app.layout = html.Div(
        [
            common.get_header(),
            common.get_menu(),
            dcc.Location(id='url', refresh=True),
            html.Div(id='page-content',)
        ]
    )


    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])

    def display_page(pathname):
        pathname = pathname.split("/")[-1]
        if pathname == 'Data':
            if len(data.wells_list_dataiku)==0:
                return data.layout
            else:
                return html.Img(src=Image.open(data.img_data))
        elif pathname == 'Tanks':
             return tanks.layout
        elif pathname == 'Benches':
             return benches.layout
        else:
            return home.layout

    

    external_css = ["hhttps://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
                    "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]
                
#if __name__ == '__main__':
#    app.run_server(debug=True)