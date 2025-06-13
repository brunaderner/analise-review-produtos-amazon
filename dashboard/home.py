# pages/home.py
import dash
from dash import html, dcc, Output, Input

dash.register_page(__name__, path="/")

layout = html.Div([
    html.Img(
        src="/assets/amazon_intro.gif",
        style={
            "width": "50%",
            "display": "block",
            "margin": "0 auto",
            "borderRadius": "10px"
        }
    ),
    html.Br(),
    html.H3("Bem-vindo ao Dashboard de Análise da Amazon", style={"textAlign": "center", "marginTop": "20px"}),
    html.P("Clique no botão abaixo para iniciar a navegação.", style={"textAlign": "center", "fontSize": "16px"}),
    html.Br(),
    html.Div([
        dcc.Location(id='url-home'),
        html.Button("Começar", id="start-button", n_clicks=0, style={"fontSize": "18px", "padding": "10px 20px"})
    ], style={"textAlign": "center", "marginTop": "20px"})
])

@dash.callback(
    Output("url-home", "href"),
    Input("start-button", "n_clicks"),
    prevent_initial_call=True
)
def redirecionar(n_clicks):
    if n_clicks:
        return "/geral"

