from dash import html, dcc, Dash
from . import ids
from source.functions import *



def render(app: Dash) -> html.Div:

    return html.Div(
        children = [
            html.H6("Order of B"),

            dcc.Slider(
                1,
                len(B_labels),
                marks = {i+1: elem for i,elem  in enumerate(B_labels)},
                id = ids.B_SLIDER,
                value = 1
            )

        ]
    )