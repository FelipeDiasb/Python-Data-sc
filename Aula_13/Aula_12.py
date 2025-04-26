import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://bea3853.github.io/site_teste_2/'


dados = requests.get(url)
site = BeautifulSoup(dados.text, 'html.parser')


valores_site = site.findAll('span')
nome = site.findAll('h1')


valores = [i.text for i in valores_site]
valores_novos = [float(valor.replace('R$', '').replace(',', '.').strip()) for valor in valores]


nomes = [x.text for x in nome if x.text != 'PRODUTO DA LOJA']


fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(nomes, valores_novos, color='black')

for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'R${altura:.2f}', xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

ax.set_ylim([0, max(valores_novos) + 10])  
plt.show()
