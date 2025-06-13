import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Registrar página
dash.register_page(__name__, path="/quartil1", name="🔻 Quartil 1")

# Carregar dataset
df = pd.read_csv("dataset_final.csv")

# Filtrar reviews únicos
df_unico = df.drop_duplicates(subset="review_id")

# Filtrar para quartil 1 (menor 25% de rating)
df_q1 = df_unico[df_unico["quartil_rating_count"] == 1]

# Scorecards
media_rating = round(df_q1["rating"].mean(), 2)
media_preco = f"₹ {round(df_q1['discounted_price'].mean(), 2)}"
total_avaliacoes = df_q1.shape[0]

# Gráfico 1 - Categoria no Q1
df_cat_q1 = df_q1["primeira_categoria"].value_counts().reset_index()
df_cat_q1.columns = ["primeira_categoria", "count"]

graf_categoria_q1 = px.bar(
    df_cat_q1, x="primeira_categoria", y="count",
    title="Distribuição de Categoria (Q1)",
    color_discrete_sequence=["black"]
)

# Gráfico 2 - Sentimento no Q1
df_sent_q1 = df_q1["sentimento_ajustado"].value_counts().reset_index()
df_sent_q1.columns = ["sentimento_ajustado", "count"]

graf_sentimento_q1 = px.bar(
    df_sent_q1, x="sentimento_ajustado", y="count",
    title="Distribuição de Sentimentos (Q1)",
    color_discrete_sequence=["black"]
)

# Gráfico 3 - Ticket médio no Q1 por categoria
graf_ticket_q1 = px.bar(
    df_q1.groupby("primeira_categoria")["discounted_price"].mean().reset_index(),
    x="primeira_categoria", y="discounted_price",
    title="Ticket Médio por Categoria (Q1)",
    color_discrete_sequence=["black"]
)

# Gráfico 4 - Rating por Categoria (Q1)
graf_rating_cat_q1 = px.bar(
    df_q1.groupby("primeira_categoria")["rating"].mean().reset_index(),
    x="primeira_categoria", y="rating",
    title="Média de Rating por Categoria (Q1)",
    color_discrete_sequence=["black"]
)

# Gráfico 5 - Dispersão Preço vs Rating (Hipótese 7/8 visualmente)
graf_disp_q1 = px.scatter(
    df_q1, x="discounted_price", y="rating",
    trendline="ols",
    title="Dispersão Preço com Desconto vs Rating (Q1)",
    color_discrete_sequence=["black"]
)

# Layout
layout = html.Div([
    html.H2("🔻 Avaliações Quartil 1", style={"textAlign": "center", "marginTop": "20px"}),

    html.Div([
        html.Div([
            html.H4("Média Rating"),
            html.H5(media_rating)
        ], className="card"),

        html.Div([
            html.H4("Média Preço"),
            html.H5(media_preco)
        ], className="card"),

        html.Div([
            html.H4("Total Avaliações"),
            html.H5(total_avaliacoes)
        ], className="card"),
    ], style={"display": "flex", "justifyContent": "space-around", "margin": "40px"}),

    dcc.Graph(figure=graf_categoria_q1),
    dcc.Graph(figure=graf_sentimento_q1),
    dcc.Graph(figure=graf_ticket_q1),
    dcc.Graph(figure=graf_rating_cat_q1),
    dcc.Graph(figure=graf_disp_q1)
])
