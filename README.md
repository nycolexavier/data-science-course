# data-scientist-course

## Comandos

### Selecione 2 colunas
    "data[[X, Y]]"

### Ordena as linhas do conjunto de dados pela coluna Z
    "data.sort_values(Z)"

### Ordena as linhas do conjunto de dados pela coluna Z de forma crescente
    "data.sort_values(Z, ascending=True)"

### Função - read_csv() 
toda função recebe parâmentros de entrada

#mostre na tea as cinco primeiras linhas do conjunto de dados
print(data.head())

#mostre o numero de linhas e o numero de columas do conjunto de dados
print(data.shape)

# mostre na tela o nome das colunas do conjunto de dados
print(data.columns)

#mostre na tela o conjunto de dados ordenados pela columa price
print(data[['id', 'price']].sort_values('price'))

# mostre na tela o conjuntos de dados ordenados pela columa price do maior para o menor
print(data[['id', 'price']].sort_values('price', ascending=False))

# data-science-course
