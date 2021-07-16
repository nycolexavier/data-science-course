# carregue o conjunto de dados chamado kc_house_data.csv do HD para a memoria

import pandas as pd
data = pd.read_csv('datasets/kc_house_data.csv')

# Perguntas:
# 1. Quantas casas estão disponíveis para compra?
#numero de linha que o preço tem, partindo do pressoposto de todas as casas tem um preço, então escolhi esse atributo, coisa que não daria pra fazer com algum atributo
print(data[['price']].shape)
    #R: 21613

# 2. Quantos atributos as casas possuem?
#columns, colunas -> shape, numero das colunas
print(data.columns.shape)
    # R: 21


# 3. Quais são os atributos das casas?
print(data.columns)
    # R: 'id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
#        'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#        'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
#        'lat', 'long', 'sqft_living15', 'sqft_lot15'


# 4. Qual a casa mais cara (casa com o maior valor de venda)?
# preciso da coluna do 'price' e do 'id' e colocar em ordem cresente
print(data[['id','price']].sort_values('price', ascending=False))
    # R: 6762700020

# 5. Qual a casa com maior número de quartos?
#creio que seja a mesma coisa do de cima, chamei a coluna 'bedrooms' e 'id' e de acordo com a 'bedrooms' (sort_values) foi organizado do maior para o menos (ascending=False)
print(data[['bedrooms', 'id']].sort_values('bedrooms', ascending=False))
    #R: 2402100895

# 6. Qual a soma total de quartos do conjunto de dados?
# chamei o arquivo, selecionei o 'bedrooms' e com o 'sum()' somou o total de quartos
print(data['bedrooms'].sum())
    # R: 72854

# 7. Quantas casas possuem 2 banheiros?
# chamar a coluna de 'bathrooms', especificar que são dois banheiros e a quantidade de linha que ela tem
print(data[data['bathrooms']==2].shape)
    # R: 1930

# 8. Qual o preço médio de todas as casas no conjunto de dados?
#selicionar a coluna de 'price' e com o mean() puxar a média
print(data['price'].mean())

# 9. Qual o preço médio de casas com 2 banheiros?
# chamar casas com dois banheiros e com a coluna 'price' ver a media delas
# pesquisar esse 'loc'
print(data.loc[data['bathrooms']==2, 'price'].mean())
      # R: 457889.7186528497

# 10. Qual o preço médio entre as casas com 3 quartos?
# chamar casas com três quartos e com a coluna 'price' ver a média delas
print(data.loc[data['bathrooms']==3, 'price'].mean())
    #R: 708415.2324037185

# 11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
# fazer a conversão de pé para metros (1 pé quadrado = 0,09 metros)
# pegar a coluna de casas que possuem mais 300 metros quadrados (e tem que ser na sala de estar!!!!)
# observação: ele que ter MAIS de 300, antes esta sendo numero exatos, agora pode ser mais de 300 pra lá
data['m2_living'] = data['sqft_living']*0.092
print(data[data['m2_living'] > 300] .shape)
    #R: 2141

# 12. Quantas casas tem mais de 2 andares?
# chamar as casas que tem mais de 2 andares e ver quantas elas são
print(data[data['floors'] > 2].shape)
    # R: 782

# 13. Quantas casas tem vista para o mar?
#observação: porque não dá pra fazer ((data['waterfront'].shape)) porque em todas as colunas existem e nas linhas tem um tipo de dado, então é mais seguro ser preciso
# chamar a coluna 'waterfront', especificando que tem que ter uma vista para o mar
print(data[data['waterfront'] == 1 ].shape)
    # R: 163

# 14. Das casas com vista para o mar, quantas tem 3 quartos?
# chamar a coluna 'waterfront', especificando que tem que ter uma vista para o mar e ver quantas tem mais de três 'badrooms'
print(data[(data['waterfront'] == 1) & (data['bedrooms'] == 3) ].shape)
    # R: 64

# 15. Das casas com mais de 300 metros quadrados de salar de estar quantos tem MAIS (>) de 2 banheiros?
# fazer a conversão de pé para metros
# ver quantos tem MAIS de 300 metros quadrados
# E (&) dessas quais tem mais de dois banheiros
data['m2_living'] = data['sqft_living']*0.092
print(data[(data['m2_living'] > 300) & (data['bathrooms'] > 2)] .shape)
    # R: 2088

