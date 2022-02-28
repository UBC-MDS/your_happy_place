from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc
import pandas as pd


app = Dash(__name__)
server = app.server

app.layout = html.Div('Start of the YHP App!')

if __name__ == '__main__':
    app.run_server(debug=True)