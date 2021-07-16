# carregar um arquivo do disco rigido para a memoria
# função: é um seguencia de comando
# Recebe uma entrada:
# Devolve uma saída: ( parametros de entrada -> um resultado)
import pandas as pd
from numpy import int64

data = pd.read_csv('datasets/kc_house_data.csv')

# função que converte de objet (string) -> date
data['date']= pd.to_datetime(data['date'])

#mostra as primeiras seis linhas
print(data.head())

# mostrar na tela os tipos de variáveis em casa coluna
print(data.dtypes)

# =======================================
# Como converter os tipos de variáveis
# =======================================

# Inteiro -> float
#data['bedrooms'] = data['bedrooms'].astype(float)

# Float -> Inteiro
#data ['bedrooms'] = data['bedrooms'].astype(int64)

# Inteiro -> String
#data['bedrooms'] = data['bedrooms'].astype(str)

# String -> Inteiro
#data['bedrooms'] = data['bedrooms'].astype(int64)

# String -> Data
#data['date'] = pd.to_datetime(data['date'])

# =======================================
# Criando novas variáveis
# =======================================

data = pd.read_csv('datasets/kc_house_data.csv')

#data['nome_do_meigarom']= "meigarom"
#data['comunidade_ds'] = '80'
#data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-28')

# =======================================
# Deletar variáveis
# =======================================

print(data.columns)
#cols =['nome_do_meigarom', 'comunidade_ds','data_abertura_comunidade_ds']
#data= data.drop(cols, axis=1)
print(data.columns)

# =======================================
# Forma 01: Direto pelos nome das columas
# =======================================
data = pd.read_csv('datasets/kc_house_data.csv')
print(data[['price', 'id', 'date']])

# =============================================
# Forma 02: Pelos indices das linhas e columas
# =============================================
# DADOS(linhas, colunas)
# 'iloc' localizar de acordo com o index
print(data.iloc[0:10, 0:3])

# =============================================
# Forma 03: Pelos indices das linhas e columas
# =============================================
# 'loc' localizar linhas e colunas
print(data.loc[0:10, ['price', 'id', 'date']])

# =============================================
# Forma 04: Indices Booleanos
# =============================================
# 1, 0
# True, False
#cols = [True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
print(data.loc[0:10, cols])

# =============================================
# Respondendo as perguntas de negócios
# =============================================
data = pd.read_csv('datasets/kc_house_data.csv')

# 1. Qual a data do imóvel mais antigo do portifólio?
# Ordenar o conjunto de dados pela menor data
#data['date'] = pd.to_datetime(data['date'])
print(data.sort_values('date', ascending=True))
    # R: 02-05-2014

# 2. Quantos imóveis possuem máximo de andares?
# Encontrar os números de andares e determinar o maior
# Contar quantos imóveis eu tenho por andar
print(data['floors'].unique())
print(data[data['floors'] == 3.5].shape)
    # R: 8

# 3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acordo com preço.

data['level'] = 'standard'

data.loc[data['price'] > 540000, 'level'] = 'high_level'
data.loc[data['price'] < 540000, 'level'] = 'low_level'

# 4. Gostaria de um relatório ordenado pelo preço
report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot' , 'level']].sort_values('price' , ascending=False)

report.to_csv('datasets/report_aula02.csv', index=False)

# 5- Gostaria de um mapa indicando onde as casas estão localizadas geograficamente

# Plotly - Bibliotexa que armazena uma função que desenha mapa
# Scatter MapBox - função que desenha o mapa
import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long',
               hover_name= 'id',
               hover_data=['price'],
               color_discrete_sequence=['fuchsia'],
               zoom=3,
               height=300)

mapa.update_layout(mapbox_style = 'open-street-map')
mapa.update_layout(height= 600, margin={'r':0, 't':0,'l':0,'b':0})
mapa.show()

mapa.write_html('datasets/mapa_house.html')

# Exercícios

# 01. Crie uma nova coluna chamada: 'house_age'
    # Se o valor da coluna 'date' for maior que 2014-01-01 -> 'new_house'
    # Se o valor da coluna 'date' for menor que 2014-01-01 -> 'old_house'

# coverter primeiro
data['date'] = pd.to_datetime(data['date'])

#criar uma coluna
data['house_age'] = 'standard'

# fazer os 'se'
data.loc[data['date'] > '2014 - 01 - 01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age' ] = 'old_house'


# 02. Crie uma nova coluna chamada: 'dormitory_type'
    # Se o valor da coluna 'bedrooms' for igual á 1 -> 'studio'
    # Se o valor da coluna 'bedrooms' for igual a 2 -> 'apartament'
    # Se o valor da coluna 'bedrroms' for maior que 2 -> 'house'

# criar a nova coluna
data['dormitory_type'] = 'standard'

# fazer os 'ses'
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartament'
data.loc[data['bedrooms'] > 3, 'dormitory_type'] = 'house'


# 03. Crie uma nova coluna chamada: 'condition_type'
    # Se o valor da coluna 'condition' for menor ou igual a 2 -> 'bad'
    # Se o valor da coluna 'condition' for igual a 3 ou 4 -> 'regular'
    # Se o valor da coluna 'condition' for igual a 5 -> 'good'

#criar uma coluna
data['condition_type'] = 'standard'

# fazer os 'ses'
data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[(data['condition'] == 3) | (data['condition'] == 4), 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'
print(data[['condition','condition_type']].head(50))


# 04. Modifique o TIPO da coluna 'condition' para STRING
#ver qual é o tipo
print(data.dtypes)

# Int -> STRING
data['condition'] = data['condition'].astype(str)
print(data.dtypes)

# 05. Delete as colunas: 'sqft_living15' e 'sqft_lot15'

cols=['sqft_living15', 'sqft_lot15']
data = data.drop(cols, axis=1)


# 06. Modifique o TIPO da coluna 'yr_build' para DATE

#ver o tipo de coluna
print(data.dtypes)

# converter int64 -> DATE
data['yr_built'] = pd.to_datetime(data['date'])

# 7. Modifique o TIPO da coluna 'yr_renovated' para DATE
# ver o tipo de coluna
print(data.dtypes)

# converter int64 -> DATE
data['yr_renovated'] = pd.to_datetime(data['date'])
print(data.dtypes)

# 8. Qual a data mais antiga de construção de um imóvel?
data[['yr_built']].sort_values('yr_built', ascending=True)
# R: 2014-05-02

# 9. Qual a data mais antiga de renovação de um imóvel?
data[['yr_renovated']].sort_values('yr_renovated', ascending=True)
# R: 2014-05-02

# 10. Quantos imóveis tem 2 andares?
data[data['floors'] == 2].shape
# R: 8241

# 11. Quantos imóveis estão com a condição igual a 'regular'?
data[data['condition_type'] == 'regular'].shape
# R: 19710

# 12. Quantos imóveis estão com a condição igual a 'bad' e possuem 'vista para água'?]
# deu essa mensagem de erro: TypeError: unsupported operand type(s) for &: 'float' and 'bool'
print(data.dtypes)
# condition_type = str
# waterfront = int64

# conversão str -> int64
data['waterfront'] = data['waterfront'].astype(str)

data[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)].shape
# R: 0

# 13. Quantos imóveis estão com a condição igual a 'good' e são 'new_house'?
data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].shape
# R: 1701

# 14. Qual o valor do imóvel mais caro do tipo 'studio'?
data[data['dormitory_type'] == 'studio'].sort_values('price', ascending=False)[['price','dormitory_type']]
# R: 1247000

# 15. Quantos imóveis do tipo 'apartament' foram reformatados em 2015?
# ver a coluna dormitory_type e especificar 'apartament'
# ver qual deles foram reformatados e especificar aqueles de 2015

# NÃO CONSEGUI PEGAR DEPOIS DE 2015
# quando for commitar, colocar o 3/3
data[data['dormitory_type'] == 'apartament'].sort_values('yr_renovated', ascending=True)

# 16. Qual o maior número de quartos de um imóveis do tipo 'house' possui?
data[data['dormitory_type'] == 'house'].sort_values('bedrooms', ascending=False)[['bedrooms','id','dormitory_type']]
# R: 33

# 17. Quantos imóveis 'new_house' foram reformados no ano de 2014?
# NÃO CONSEGUI PEGAR SÓ OS DOS ANOS DE 2014
# quando for commitar, colocar 3/3
data[data['house_age'] == 'new_house'].sort_values('yr_renovated', ascending=True)[['date', 'yr_renovated']]

#========================================================================
#18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18
#========================================================================

# 18. Selecione as colunas: 'id', 'date', 'price', 'floors', 'zipcode' pelo método:
    # 18.1 Direto pelo nome das colunas.
print(data[['id', 'date', 'price', 'floors', 'zipcode']])

    # 18.2 Pelos Índices
print(data.iloc[0:, 0:5])

    # 18.3 Pelos Índices das linhas e o nome das colunas
print(data.loc[0:, ['id', 'date', 'price', 'floors', 'zipcode']])

    # 18.4 Índices Booleanos
print(data.columns)
#cols = [True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False]
print(data.loc[0: , cols])

# 19. Salve um arquivo .csv com somente a coluna do item 10 ao 17
report.to_csv('datasets/question_aula02.csv', index=False)

# 20. Modifique a cor do ponto no mapa de pink para 'verde-escuro'

# Plotly - Bibliotexa que armazena uma função que desenha mapa
# Scatter MapBox - função que desenha o mapa
import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long',
               hover_name= 'id',
               hover_data=['price'],
               color_discrete_sequence=['lightgreen'],
               zoom=3,
               height=300)

mapa.update_layout(mapbox_style = 'open-street-map')
mapa.update_layout(height= 600, margin={'r':0, 't':0,'l':0,'b':0})
mapa.show()

mapa.write_html('datasets/mapa_house_aula02.html')
