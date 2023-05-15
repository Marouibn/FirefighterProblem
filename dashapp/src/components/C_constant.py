from dash import html, dcc, Dash
from . import ids



def render(app: Dash) -> html.Div:

    return html.Div(
        children = [
            html.H6("Constant C"),

            dcc.Input(
                placeholder="Enter the value of the constant C",
                type = "number",
                value = '',
                id=ids.C_INPUT
            )

        ]
    )