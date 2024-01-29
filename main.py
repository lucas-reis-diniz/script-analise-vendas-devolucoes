
import os
import pandas as pd
print(pd.__version__)

pasta_base = r"D:\Vendas"
lista_arquivo = os.listdir(pasta_base)
print(lista_arquivo)

tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        caminho_arquivo = os.path.join(pasta_base, arquivo)
        tabela = pd.read_csv(caminho_arquivo)
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)


print(tabela_total)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)

import plotly.express as px

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()
