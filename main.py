import pandas as pd
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

tabela_vendas = pd.read_excel('janeiro.xlsx')
for mes in lista_meses:
    print(mes)

print(tabela_vendas)