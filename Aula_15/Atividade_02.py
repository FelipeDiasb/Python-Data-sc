# Processo e analise da dados 
#  Mais objetivo:
 
import pandas as pd
import matplotlib.pyplot as plt

#Coleta de Dados
dados = pd.read_csv('dados.csv')

# limpeza de Dados
dados.dropna(inplace=True)

# exploração de Dados
print(dados.describe())

# visualização de Dados
plt.hist(dados['vendas'])
plt.xlabel('Vendas')
plt.ylabel('Frequência')
plt.title('Distribuição das Vendas')
plt.show()
