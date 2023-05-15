from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd
from source import simulations
from source.functions import B_labels, p_labels
from source.agents.agents import agents

def render(app: Dash) -> html.Div:    



    @app.callback(
        Output(ids.GRAPH, "children"),
        [
            Input(ids.P_SLIDER, "value"),
            Input(ids.C_INPUT, "value"),
            Input(ids.B_SLIDER, "value"),
            Input(ids.D_INPUT, "value"),
            Input(ids.DROPDOWN, "value")
        ]
    )
    def update_barchart(p_label, C, B_label, D, agent_id):

        if (type(C) != type(0.5) and type(C) != type(1)) or (type(D) != type(0.5) and type(D)!=type(1)) or agent_id==None:
            return html.H6("Invalid values", id = ids.GRAPH)
        

        if p_label-int(p_label) < int(p_label)+1-p_label:
            p_label = int(p_label)
        else:
            p_label = int(p_label+1)

        if B_label-int(B_label) < int(B_label)+1-B_label:
            B_label = int(B_label)
        else:
            B_label = int(B_label+1)


        fig = simulations.run_simulation_MP(
            p_labels[list(p_labels.keys())[p_label-1]](C),
            B_labels[list(B_labels.keys())[B_label-1]](D),
            agent=agents[agent_id],
            max_n=50,
            n_iterations=20
        )
        
        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.GRAPH
        )



    return html.Div(id=ids.GRAPH)

