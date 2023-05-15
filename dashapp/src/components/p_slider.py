from dash import html, dcc, Dash
from . import ids
from source.functions import *



def render(app: Dash) -> html.Div:

    return html.Div(
        children = [
            html.H6("Order of p"),

            dcc.Slider(
                1,
                len(p_labels),
                marks = {i+1: elem for i,elem  in enumerate(p_labels)},
                id = ids.P_SLIDER,
                value = 1
            )

        ]
    )