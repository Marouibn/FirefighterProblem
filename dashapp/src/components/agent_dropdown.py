from dash import Dash, html, dcc # Dash core components
from dash.dependencies import Input, Output
from source.agents.agents import agents
from . import ids

def render(app: Dash) -> html.Div:
    options = list(agents.keys())


    return html.Div(
        children=[
            html.H3("Policy: "),
            dcc.Dropdown(
                id = ids.DROPDOWN,
                options = [{"label": pol, "value": pol} for pol in options],
                multi=False
            )
        ]
    )