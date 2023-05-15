from source.simulations import run_simulation_MP
import numpy as np


from dash import Dash, html
from dashapp.src.components.layout import app_layout
from dash_bootstrap_components.themes import BOOTSTRAP

def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "ORIE 6125 Project"
    app.layout = app_layout(app)
    app.run()

if __name__ == "__main__":
    main()


# if __name__ == "__main__" :
#     run_simulation_MP(lambda n:np.log(n)/n, lambda n : max(1,int(np.log(n))))
    