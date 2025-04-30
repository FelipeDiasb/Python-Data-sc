# ATIVIDADE 1
# GERAR GRAFICO


# Buscar todas as idades 

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt  
import pandas as pd
import tkinter as tk


url = 'https://tabelatest.netlify.app/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
dados = soup.find('tbody').get_text()
print(dados)

idade = []
cidade =[]

dados in soup.find_all('tbory', class_='colunas'):
    idade.append(dados.find('td'[2]).text)
    cidade.append(dados.find('td'[3]).text)

    print(cidade)
   


#    df  = pd.DataFrame({
#     'Modelos':nome,
#     'Preço':preco,
#     'Avaliação':avaliacao
# })