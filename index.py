from dash import Dash
from app import start_app

if __name__ == "__main__":
    app = Dash(__name__)
    start_app(app)
    app.run(debug=True)