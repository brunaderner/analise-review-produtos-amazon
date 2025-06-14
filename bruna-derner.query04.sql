#Identificando nulos da tabela review
SELECT
COUNT(*) AS total_linhas,
COUNTIF(user_id IS NULL) AS linhas_user,
COUNTIF(user_name IS NULL) AS linhas_name,
COUNTIF(review_id IS NULL) AS linhas_review,
COUNTIF(review_title IS NULL) AS linhas_title,
COUNTIF(review_content IS NULL) AS linhas_content,
COUNTIF(img_link IS NULL) AS linhas_img,
COUNTIF(product_link  IS NULL) AS linhas_productl,
COUNTIF(product_id IS NULL) AS linhas_product_id,
COUNTIF(rating IS NULL) AS linhas_rating,
COUNTIF(rating_count IS NULL) AS linhas_ratingc,
FROM `proj04.amazon_review`


#Visualizando os nulos de rating count
SELECT *
FROM `proj04.amazon_review`
WHERE rating_count IS NULL




#Identificando nulos em produto
SELECT
COUNT(*) AS total_linhas,
COUNTIF(product_id IS NULL) AS linhas_productid,
COUNTIF(product_name IS NULL) AS linhas_productname,
COUNTIF(category IS NULL) AS linhas_category,
COUNTIF(discounted_price IS NULL) AS linhas_dprice,
COUNTIF(actual_price IS NULL) AS linhas_aprice,
COUNTIF(discounted_price IS NULL) AS linhas_dprice,
COUNTIF(discount_percentage IS NULL) AS linhas_dpercent,
COUNTIF(about_product IS NULL) AS linhas_abprod,


FROM `proj04.amazon_product`


#visualizando about_product
SELECT *
FROM `proj04.amazon_product`
WHERE about_product IS NULL


#Identificando duplicados em product
SELECT
  product_id,
  product_name,
  category,
  discounted_price,
  discount_percentage,
  actual_price,


  COUNT(*) AS quantidade
FROM `proj04.amazon_product`
GROUP BY product_id, product_name, category, discounted_price, discount_percentage, actual_price
HAVING COUNT(*) > 1;


#Identificando duplicados em review


SELECT
  user_id,
  user_name,
  review_id,
  review_title,
  review_content,
  product_id,
  rating,


  COUNT(*) AS quantidade
FROM `proj04.amazon_review`
GROUP BY  user_id,user_name, review_id,review_title, review_content,  product_id, rating
HAVING COUNT(*) > 1;


##tirando duplicados de product
CREATE OR REPLACE TABLE `proj04.amazon_product1` AS
SELECT
DISTINCT *
FROM `proj04.amazon_product`;


#Tratrando Rating
SELECT DISTINCT rating
FROM `proj04.amazon_review`
ORDER BY rating;


#TRANSFORMANDO EM FLOAT E TIRANDO O NULO 
CREATE OR REPLACE TABLE `proj04.amazon_review1` AS
SELECT
  user_id,
  user_name,
  review_id,
  review_title,
  review_content,
  img_link,
  product_link,
  product_id,
  SAFE_CAST(rating AS FLOAT64) AS rating,
  rating_count,


FROM `proj04.amazon_review`
WHERE SAFE_CAST(rating AS FLOAT64) IS NOT NULL


#Analisando as informações do rating_count
SELECT
  AVG(rating_count) AS media_ratingc,
  MIN(rating_count) AS min_ratingc,
  MAX(rating_count) AS max_ratingc,
  APPROX_QUANTILES(rating_count, 2)[OFFSET(1)] AS mediana_ratingc
FROM `proj04.amazon_review1`;


#identificando o motivo da avaliação
WITH reviews_classificados AS (
  SELECT
    review_id,
    review_title,
    review_content,
    rating,
    CASE
      WHEN LOWER(review_title) LIKE '%deliver%' OR LOWER(review_content) LIKE '%deliver%'
           OR LOWER(review_content) LIKE '%late%' OR LOWER(review_content) LIKE '%delay%' THEN 'Delivery'


      WHEN LOWER(review_title) LIKE '%broken%' OR LOWER(review_content) LIKE '%broken%'
           OR LOWER(review_content) LIKE '%defect%' OR LOWER(review_content) LIKE '%damaged%'
           OR LOWER(review_content) LIKE '%doesn%t work%' THEN 'Product'


      WHEN LOWER(review_content) LIKE '%support%' OR LOWER(review_content) LIKE '%customer service%'
           OR LOWER(review_content) LIKE '%response%' OR LOWER(review_content) LIKE '%help%' THEN 'Customer Service'


      WHEN LOWER(review_content) LIKE '%expect%' OR LOWER(review_content) LIKE '%disappoint%'
           OR LOWER(review_content) LIKE '%not what%' OR LOWER(review_content) LIKE '%smaller%' THEN 'Expectations'


      ELSE 'Other'
    END AS main_reason
  FROM `proj04.amazon_review1`
)


-- Consulta final usando a CTE:
SELECT main_reason, COUNT(*) AS total_reviews
FROM reviews_classificados
GROUP BY main_reason
ORDER BY total_reviews DESC;






#ADICIONANDO NA TABELA
CREATE OR REPLACE TABLE `proj04.amazon_review1` AS
SELECT
  *,
  CASE
    WHEN LOWER(review_title) LIKE '%deliver%' OR LOWER(review_content) LIKE '%deliver%'
         OR LOWER(review_content) LIKE '%late%' OR LOWER(review_content) LIKE '%delay%' THEN 'Delivery'


    WHEN LOWER(review_title) LIKE '%broken%' OR LOWER(review_content) LIKE '%broken%'
         OR LOWER(review_content) LIKE '%defect%' OR LOWER(review_content) LIKE '%damaged%'
         OR LOWER(review_content) LIKE '%doesn%t work%' THEN 'Product'


    WHEN LOWER(review_content) LIKE '%support%' OR LOWER(review_content) LIKE '%customer service%'
         OR LOWER(review_content) LIKE '%response%' OR LOWER(review_content) LIKE '%help%' THEN 'Customer Service'


    WHEN LOWER(review_content) LIKE '%expect%' OR LOWER(review_content) LIKE '%disappoint%'
         OR LOWER(review_content) LIKE '%not what%' OR LOWER(review_content) LIKE '%smaller%' THEN 'Expectations'


    ELSE 'Other'
  END AS main_reason
FROM `proj04.amazon_review1`;






#união
CREATE OR REPLACE TABLE `proj04.amazon_uniao1` AS
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY product_id
      ORDER BY
        ( CASE WHEN img_link     IS NOT NULL THEN 1 ELSE 0 END
        + CASE WHEN product_link IS NOT NULL THEN 1 ELSE 0 END
        + CASE WHEN about_product IS NOT NULL THEN 1 ELSE 0 END
        ) DESC,
        review_id ASC
    ) AS rn
  FROM
    `proj04.amz_uniao`
)
SELECT
 product_id,
product_name,
category,
discounted_price,
actual_price,
discount_percentage,
about_product,
user_id,
user_name,
review_id,
review_title,
review_content,
img_link,
product_link,
rating,
rating_count
FROM
  ranked
WHERE
  rn = 1;


CREATE OR REPLACE TABLE `proj04.amazon_uniao` AS
SELECT
  *
FROM
  `proj04.amazon_uniao`
WHERE
  product_id <> 'B08L12N5H1';


#CRIANDO AS VARIAVEIS DE CATEGORIA
CREATE OR REPLACE TABLE `proj04.amazon_uniao` AS
SELECT
  *,
  REGEXP_EXTRACT(category, r'^[^|]+') AS primeira_categoria,
  REGEXP_EXTRACT(category, r'[^|]+$') AS ultima_categoria
FROM
  `proj04.amazon_uniao`;


#visuzalizando distribuição desconto
SELECT
  MIN(discount_percentage) AS minimo,
  MAX(discount_percentage) AS maximo,
  AVG(discount_percentage) AS media,
  APPROX_QUANTILES(discount_percentage, 2)[OFFSET(1)] AS mediana
FROM `proj04.amazon_uniao`
WHERE discount_percentage IS NOT NULL




#distribuição de rating
SELECT
  MIN(rating) AS minimo,
  MAX(rating) AS maximo,
  AVG(rating) AS media,
  APPROX_QUANTILES(rating, 2)[OFFSET(1)] AS mediana
FROM `proj04.amazon_uniao`
WHERE rating IS NOT NULL


#rating_count 
SELECT
  MIN(rating_count) AS minimo,
  MAX(rating_count) AS maximo,
  AVG(rating_count) AS media,
  APPROX_QUANTILES(rating_count, 2)[OFFSET(1)] AS mediana
FROM `proj04.amazon_uniao`
WHERE rating_count IS NOT NULL


## CALCULANDO QUARTIS
CREATE OR REPLACE TABLE `proj04.amazon_uniao` AS
SELECT *,
NTILE(4) OVER (ORDER BY discount_percentage) AS quartil_discount,
NTILE(4) OVER (ORDER BY rating) AS quartil_rating,
NTILE(4) OVER (ORDER BY rating_count) AS quartil_rating_count,
  FROM `proj04.amazon_uniao`
  WHERE discount_percentage IS NOT NULL
  OR rating IS NOT NULL
  OR rating_count IS NOT NULL




