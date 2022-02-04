import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

# criar um dataframe
# dataFrame = pd.DataFrame()

# apartir de um dicionario
venda = {'data' : ['15/02/2020', '16/02/2021'],
         'valor' : [500, 300],
         'produto' : ['feijao', 'arroz'],
         'qtde' : [50, 70]}
vendas_df = pd.DataFrame(venda)
print(vendas_df.head())

# importar dados de um arquivo csv
vendas_df = pd.read_excel('tudopandas/Vendas.xlsx')

# exibir as 10 primeiras linhas
print(vendas_df.head(10))

# exibe as linhas e colunas do DataFrame
print(vendas_df.shape)

# exibe o resumo do DataFrame
print(vendas_df.describe())

# criar 1 serie do pandas com 1 coluna
serie = vendas_df['Produto']

# criar 1 dataframe com 2 colunas
colunas_df = vendas_df[['Produto','ID Loja']]

# .loc -> seleciona linhas e colunas
# estrutura do loc -> .loc[linhas, colunas]
# pegar 1 linha
print(vendas_df.loc[0])
# linhas de acordo com alguma condição
print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])
# pegar varias linhas e colunas usando o loc
print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['Produto', 'ID Loja','Quantidade']])
# linhas e colunas especificas
print(vendas_df.loc[:,['Produto','ID Loja']])
# pega 1 valor especifico
print(vendas_df.loc[0, 'Produto'])

# adicionar 1 coluna
# criar a partir de uma coluna existente
# caso exista a coluna, ela será substituida pelo novo valor, se não existir, será criada
## comissao de 5% sobre o valor
vendas_df['Comissao'] = vendas_df['Valor Final'] * 0.05
print(vendas_df)

# criar coluna com um valor padrão
# vendas_df = vendas_df.loc[:, 'Imposto'] = 0
# print(vendas_df)

# adicionar uma linha com base em um arquivo xlsx
vendas_dez_df = pd.read_excel('tudopandas/Vendas - Dez.xlsx')
vendas_df = vendas_df.append(vendas_dez_df)
print(vendas_df)

# excluir uma coluna ou linha
# linha usa o eixo 0
# coluna usa o eixo 1
# vendas_df = vendas_df.drop('Comissao', axis=1)
# print(vendas_df)
# vendas_df = vendas_df.drop(0, axis=0)
# print(vendas_df)

# excluir colunas vazias ou linhas completamente vazias podendo passar o eixo
# vendas_df = vendas_df.dropna(how='all', axis=1)

# deletar linas que tenham valores vazios
# vendas_df = vendas_df.dropna()

# # preencher valores vazios com a media da coluna
# vendas_df['Comissao'] = vendas_df['Comissao'].fillna(vendas_df['Comissao'].mean())
# print(vendas_df)

# preencher valores vazios com o ultimo valor
vendas_df = vendas_df.ffill()
print(vendas_df)

# calcular a quantidade de linhas por loja
print(vendas_df['ID Loja'].value_counts())

# calcular o faturamento por produto
print(vendas_df[['Produto','Valor Final']].groupby(vendas_df['Produto']).sum())

# mesclar 2 dataframes GERENTE E LOJAS
gerentes_df = pd.read_excel('tudopandas/Gerentes.xlsx')
print(gerentes_df)

vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)