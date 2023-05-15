from dash import html, dcc, Dash
from . import ids



def render(app: Dash) -> html.Div:

    return html.Div(
        children = [
            html.H6("Constant D"),

            dcc.Input(
                placeholder="Enter the value of the constant D",
                type = "number",
                value = '',
                id= ids.D_INPUT
            )

        ]
    )