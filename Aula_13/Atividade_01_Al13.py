# Desafio 2: 
# Objetivo
# O objetivo deste desafio é criar um script em Python que acesse a aplicação 
# web `https://gratuitos.netlify.app` e extraia a tabela de cursos exibido na página 
# usando a biblioteca BeautifulSoup.

# Passos a Seguir

# 1.Instalação das Bibliotecas Necessárias:
#  Primeiro, certifique-se de que você tem as bibliotecas `requests` e 
# `beautifulsoup4` instaladas. 
#  Você pode instalá-las usando o `pip`:
#  pip install requests beautifulsoup4

# 2.Criação do Script:
# Crie um script Python seguindo os passos abaixo para acessar a 
# aplicação web e extrair a tabela da aplicação.
# mandar para o print

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://gratuitos.netlify.app'


dados = requests.get(url)
site = BeautifulSoup(dados.text,'html.parser')


# valores_site = site.findAll('table',)
# nome = site.findAll('tr','th')
# valores = [i.text for i in valores_site]

print(site.prettify())

site.title