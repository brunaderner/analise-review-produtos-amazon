# app.py
import dash
from dash import html, dcc
import pandas as pd

# Carrega o dataset para o app todo (se necessário em callbacks futuros)
df = pd.read_csv("dataset_final.csv")

# Inicializa o app com suporte a páginas
app = dash.Dash(__name__, use_pages=True)
app.title = "Dashboard Amazon"

# Layout do app com navegação customizada
app.layout = html.Div([

    html.Div([
        dcc.Link("🏠 Início", href="/", style={"margin": "10px"}),
        dcc.Link("📊 Visão Geral", href="/geral", style={"margin": "10px"}),
        dcc.Link("🔻 Quartil 1", href="/quartil1", style={"margin": "10px"}),
        dcc.Link("💬 NLP", href="/nlp", style={"margin": "10px"}),
    ], style={
        "textAlign": "center",
        "padding": "10px",
        "backgroundColor": "#f0f0f0",
        "borderBottom": "1px solid #ccc"
    }),

    dash.page_container
])

# Rodar o app
if __name__ == "__main__":
    app.run(debug=True)
