# Análise de Reviews de Produtos na Amazon

O objetivo deste trabalho é validar hipóteses sobre os fatores que influenciam a avaliação de produtos (ratings) na Amazon. A partir de um banco de dados com informações de reviews e características dos produtos, a análise busca identificar padrões que afetam a nota média, como preço, descontos, popularidade (número de avaliações), sentimento expresso nos comentários e categoria dos produtos.

Os resultados visam fornecer insights para apoiar decisões estratégicas em marketing e posicionamento de produtos.

## Objetivo

Investigar hipóteses sobre os fatores que impactam o rating médio dos produtos na Amazon, considerando variáveis como preço, percentual de desconto, volume de avaliações, sentimento do review e categoria do produto.

## Tecnologias e Ambiente de Desenvolvimento

- **Linguagem**: Python  
- **Bibliotecas Python**: Pandas, NumPy, Matplotlib, Plotly, Seaborn, SciPy, Statsmodels, Scikit-learn, Scikit-posthocs, NLTK  
- **Banco de Dados**: CSV processado localmente (`dataset_final.csv`)  
- **Visualização de Dados**: Plotly e Matplotlib (gráficos interativos e estáticos)  
- **Ambiente de Desenvolvimento**: Visual Studio Code + Jupyter Notebook (`notebook04.ipynb`)

## Estrutura do Projeto

- `assets/`: Arquivos visuais e de estilo (GIF de introdução, CSS)  
- `pages/`: Páginas de código Python para construção do dashboard e análise:
  - `geral.py` — Análise geral  
  - `home.py` — Página inicial  
  - `nlp.py` — Análise de sentimentos e NLP  
  - `quartil1.py` — Análise específica do primeiro quartil de ratings  
- `dataset_final.csv`: Base de dados consolidada e tratada  
- `dashboard04.py`: Código para dashboard interativo  
- `notebook04.ipynb`: Notebook com análises exploratórias, testes de hipóteses e regressões   

## Metodologia

- **Integração e Tratamento de Dados:** O dataset original foi processado e consolidado em `dataset_final.csv`. Foram tratadas variáveis como preço real (actual_price), percentual de desconto, sentimentos dos comentários, categorias e número de avaliações.
  
- **Análise Exploratória:** Gráficos de dispersão, boxplots e histogramas foram utilizados para explorar a relação entre variáveis-chave e o rating.

- **Análise de Sentimento:** Foram extraídos sentimentos dos reviews (positivo, negativo, elogio), com base em análise NLP (NLTK + modelagem própria).

- **Testes Estatísticos:** Foram aplicados testes de:
  - Comparação de médias (t-test)  
  - Testes não paramétricos (Mann-Whitney U, Qui-quadrado para associação entre categoria e sentimento)  
  - Regressões lineares simples e múltiplas  
  - Regressões logísticas (para entender a probabilidade de avaliações estarem no quartil inferior Q1)

- **Modelagem:** Regressões múltiplas foram utilizadas para avaliar o impacto conjunto de variáveis como preço, popularidade, sentimento e categoria sobre o rating.

## Principais Resultados

- **Popularidade importa:** Produtos com maior número de avaliações tendem a exibir ratings médios ligeiramente superiores.

- **Descontos afetam percepção:** Percentuais de desconto mais elevados estão associados a ratings mais baixos, possivelmente por influência na percepção de valor ou qualidade.

- **Preço não influencia significativamente:** Não foi observada diferença significativa de rating entre produtos de preços altos e baixos.

- **Sentimento e categoria influenciam fortemente o Q1:** Produtos com maior proporção de sentimentos negativos e determinadas categorias (Electronics, Home&Kitchen) apresentaram maior probabilidade de figurar no primeiro quartil de avaliações (Q1).

- **Características combinadas:** A regressão múltipla confirmou que sentimento positivo, número de avaliações, preço e categoria explicam parte relevante da variação no rating (R² = 17,5%).

## Autora

Bruna Derner  
Economista e Analista de Dados  
[LinkedIn](https://www.linkedin.com/in/bruna-derner/)

