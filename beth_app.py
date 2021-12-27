import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

class CreateApp(object):
    def __init__(self, server):
        self.server = server

        print("VF: Creating class: type of Dash is %s" % type(dash.Dash))
        self.dash_app = dash.Dash(__name__, server=server)

        # assume you have a "long-form" data frame
        # see https://plotly.com/python/px-arguments/ for more options
        df = pd.DataFrame({
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })
        
        fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
        
        self.dash_app.layout = html.Div(children=[
            html.H1(children='VF Hello Dash - Using bet_runner'),
        
            html.Div(children='''
                VF Dash: A web application framework for your data.
            '''),
        
            dcc.Graph(
                id='example-graph',
                figure=fig
            )
        ])
        return


