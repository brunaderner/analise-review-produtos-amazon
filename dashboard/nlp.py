import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/nlp", name="💬 NLP & Hipóteses")

# Carregar dataset
df = pd.read_csv("dataset_final.csv")

df_unico = df.drop_duplicates(subset="review_id")

# Gráfico 1 - Frequência dos Temas
tema_counts = df_unico["tema_categoria"].value_counts().reset_index()
tema_counts.columns = ["tema", "count"]

graf_tema = px.bar(
    tema_counts, x="tema", y="count",
    title="Frequência dos Temas (NLP)",
    color_discrete_sequence=["black"]
)

# Gráfico 2 - Sentimento por Categoria (Hipótese 10)
df_sent_cat = df_unico.groupby(["primeira_categoria", "sentimento_ajustado"]).size().reset_index(name="count")

graf_sentimento_cat = px.bar(
    df_sent_cat,
    x="primeira_categoria", y="count", color="sentimento_ajustado",
    title="Sentimento por Categoria (Hipótese 10)",
    color_discrete_sequence=["black", "dimgray", "gray"],
    barmode="group"
)

# Layout
layout = html.Div([
    html.H2("💬 Análise NLP & Hipóteses", style={"textAlign": "center", "marginTop": "20px"}),

    dcc.Graph(figure=graf_tema),
    dcc.Graph(figure=graf_sentimento_cat)
])

