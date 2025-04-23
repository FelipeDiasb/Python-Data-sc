import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg


dados = pd.read_csv('Exerci_Aula_10.py/dados.csv')

df =  pd.DataFrame(dados)
 
print(dados.head())

plt.figure(figsize=(9, 7))
plt.subplot(221)
plt.pie(df['Vendas'], labels=df['Mês'], autopct='%1.1f%%', startangle=50, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title(' Vendas por Mês')
plt.axis('equal') 

plt.subplot(222)
plt.scatter(df['Vendas'], df['Lucro'], color='blue', edgecolor='black')
plt.title('Vendas e Lucro')
plt.xlabel('Vendas')
plt.ylabel('Lucro')
plt.grid(True)


plt.subplot(223)
plt.bar(df['Mês'], df['Vendas'], color='green')
plt.title('Comparação de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas')



plt.subplot(223)
plt.bar(df['Mês'], df['Vendas'], color='green')
plt.title('Comparação de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas')


plt.subplot(224)
plt.plot(df['Mês'], df['Lucro'], marker='o', color='red', linestyle='-', markersize=8)
plt.title('Evolução do Lucro ao Longo dos Meses')
plt.xlabel('Mês')
plt.ylabel('Lucro')
plt.grid(True)
plt.show()




















