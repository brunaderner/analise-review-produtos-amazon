import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path="/geral", name="📊 Visão Geral")

# Carregar dataset
df = pd.read_csv("dataset_final.csv")

df_unico = df.drop_duplicates(subset="review_id")

# Scorecards
total_reviews = df_unico.shape[0]
media_rating = round(df_unico["rating"].mean(), 2)
ticket_medio = f"₹ {round(df_unico['discounted_price'].mean(), 2)}"

perc_elogio = round((df_unico[df_unico["sentimento_ajustado"] == "elogio"].shape[0] / total_reviews) * 100, 2)

# Gráfico Distribuição de Rating
graf_rating = px.histogram(
    df_unico, x="rating", nbins=20,
    title="Distribuição de Ratings",
    color_discrete_sequence=["black"]
)

# Hipótese 1 → Produtos com mais avaliações tendem a ter ratings mais altos → Dispersão rating_count vs rating
graf_hip1 = px.scatter(
    df_unico, x="rating_count", y="rating",
    trendline="ols",
    title="Hipótese 1: Número de Avaliações vs Rating",
    color_discrete_sequence=["black"]
)

# Hipótese 2 → Categoria do produto afeta o rating médio → Boxplot categoria vs rating
graf_hip2 = px.box(
    df_unico, x="primeira_categoria", y="rating",
    title="Hipótese 2: Categoria do Produto vs Rating",
    color_discrete_sequence=["black"]
)

# Hipótese 3 → Associação entre % desconto e rating → Dispersão discount_percentage vs rating
graf_hip3 = px.scatter(
    df_unico, x="discount_percentage", y="rating",
    trendline="ols",
    title="Hipótese 3: % de Desconto vs Rating",
    color_discrete_sequence=["black"]
)

# Hipótese 5 → Produtos mais caros tendem a ter avaliações maiores → Boxplot grupo_preco vs rating
# Criar Grupo de Preço
df_unico["actual_price"] = pd.to_numeric(df_unico["actual_price"], errors="coerce")
mediana_preco = df_unico["actual_price"].median()
df_unico["grupo_preco"] = df_unico["actual_price"].apply(lambda x: "Alto" if x > mediana_preco else "Baixo")

graf_hip5 = px.box(
    df_unico, x="grupo_preco", y="rating",
    title="Hipótese 5: Grupo de Preço vs Rating",
    color_discrete_sequence=["black"]
)

# Gráfico de rosca (Distribuição geral dos sentimentos)
df_sentimento_geral = df_unico["sentimento_ajustado"].value_counts().reset_index()
df_sentimento_geral.columns = ["sentimento_ajustado", "count"]

graf_sentimento_geral = px.pie(
    df_sentimento_geral, names="sentimento_ajustado", values="count",
    title="Distribuição Geral dos Sentimentos",
    color_discrete_sequence=["black", "dimgray", "gray"]
)

# Layout
layout = html.Div([
    html.H2("📊 Visão Geral do Negócio", style={"textAlign": "center", "marginTop": "20px"}),

    html.Div([
        html.Div([
            html.H4("Total Avaliações"),
            html.H5(total_reviews)
        ], className="card"),

        html.Div([
            html.H4("Rating Médio"),
            html.H5(media_rating)
        ], className="card"),

        html.Div([
            html.H4("Ticket Médio"),
            html.H5(ticket_medio)
        ], className="card"),

        html.Div([
            html.H4("% Elogio"),
            html.H5(f"{perc_elogio}%")
        ], className="card"),
    ], style={"display": "flex", "justifyContent": "space-around", "margin": "40px"}),

    dcc.Graph(figure=graf_rating),

    # Hipóteses:
    dcc.Graph(figure=graf_hip1),
    dcc.Graph(figure=graf_hip2),
    dcc.Graph(figure=graf_hip3),
    dcc.Graph(figure=graf_hip5),

    dcc.Graph(figure=graf_sentimento_geral)
])
