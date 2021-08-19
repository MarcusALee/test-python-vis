import requests
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

 

def visualization():
    df = pd.read_csv('test.csv')

    fig = px.scatter_3d(
        df, 
        x = df.columns[0], 
        y = df.columns[1], 
        z = df.columns[2], 
        size = df.columns[1], 
        color = df.columns[1],
        title='Apple Share Prices over time (2014)'
    )
    fig.show()
    return fig

app.layout = html.Div(children=[
    #html.H1(children='Hello Dash'),

    #html.Div(children='''
    #    Dash: A web application framework for Python.
    #'''),

    dcc.Graph(
        id='example-graph',
        figure=visualization()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

