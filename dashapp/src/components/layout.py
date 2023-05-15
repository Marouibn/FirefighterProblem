from dash import Dash, html
from . import p_slider, B_slider, C_constant, D_constant, agent_dropdown
from dashapp.src.components import graph

def app_layout(app: Dash) -> html.Div:

    return html.Div(
        className="app-layout",
        children = [
            html.H1(app.title),



            html.H2("This is our first Dash web app"),


            
            html.Div(
                className = "p_slider",
                children = [
                    p_slider.render(app)
                ]
            ),
            html.Div(
                className = "C_input",
                children = [
                    C_constant.render(app)
                ]
            ),

            html.Div(
                className = "nodes_slider",
                children = [
                    B_slider.render(app)
                ]
            ),

            html.Div(
                className = "D_input",
                children = [
                    D_constant.render(app)
                ]
            ),
            
            html.Div(
                className = "dropdown_container",
                children = [
                    agent_dropdown.render(app)
                ]
            ),


            graph.render(app)
        ]
    )