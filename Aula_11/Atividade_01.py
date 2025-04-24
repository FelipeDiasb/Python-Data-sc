# Para trabalhar com DataFrames, filtros e gráficos em Python,vc precisa 
# entender algumas bibliotecas e conceitos fundamentais. Vamos cobrir cada um dos 
# tópicos:

# ### DataFrames com Pandas

# #### O que são DataFrames
# DataFrames são estruturas de dados bidimensionais, semelhantes a tabelas em 
# bases de dados ou planilhas do Excel. Eles são um dos componentes principais da 
# biblioteca Pandas.

# #### Como criar DataFrames

# import pandas as pd

# # Criando um DataFrame a partir de um dicionário
# data = {
#     'Nome': ['Alice', 'Bob', 'Charlie'],
#     'Idade': [25, 30, 35],
#     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
# }

# df = pd.DataFrame(data)

# # Exibindo o DataFrame
# print(df)


# ### Filtros em DataFrames

# #### Selecionando colunas

# # Selecionando a coluna 'Nome'
# nomes = df['Nome']
# print(nomes)


# #### Filtrando linhas

# # Filtrando pessoas com idade maior que 30
# idade_maior_30 = df[df['Idade'] > 30]
# print(idade_maior_30)


# #### Usando condições múltiplas

# # Filtrando pessoas com idade maior que 25 e que moram em São Paulo
# filtro = df[(df['Idade'] > 25) & (df['Cidade'] == 'São Paulo')]
# print(filtro)


# ##Gráficos com Matplotlib e Seaborn

# ## Instalando as bibliotecas:
# Se você ainda não tem essas bibliotecas instaladas, pode instalá-las usando pip:




# # Criando gráficos com Matplotlib

# import matplotlib.pyplot as plt

# # Gráfico de barras
# plt.bar(df['Nome'], df['Idade'])
# plt.xlabel('Nome')
# plt.ylabel('Idade')
# plt.title('Idade das pessoas')
# plt.show()



# #### Acessando JSON

# Json é o object notion JS, é uma notação para organizar e 
# armazenar dados.

# Vamos criar manualmente: 

# {
#     "alunos": [
#         {
#             "Nome": "2",
#             "Media": 10.0
#         },
#         {
#             "Nome": "10",
#             "Media": 10.0
#         }
#     ]
# }

# --------------------------------------------------------------------

# podemos também usar usar essa função pára 
# criar seu próprio JSON:

# import json

# qA = int(input('quantidade de alunos: '))
# nomes = [0] * qA
# media = [0] * qA
# nomeE = input('nome do json')
# alunos = {nomeE:[]}



# for i in range(qA):
#     nomes[i] = input('nome do aluno: ')
#     media[i] = float(input(' media aluno: '))

# for j in range(qA):
#       alunos['alunos'].append(
#         {  'Nome': nomes[j],
#             'Media': media[j]
#         }
#     )
# with open('alunos2.json', 'w') as arquivo:     
#     json.dump(alunos, arquivo, indent=4)
   
   
#    Com a função acima criar um json com pelo 10 
#    dados extraia os dados da media.  
   
#    e crie um grafico plot/scartter/pie/bar  
   
   
   
#   --------------------------------  
    
#  {
# "test":{
# "a":[1,2,3],
# "b":[1,2,6],
# "c":[12,5,6],
# "d":[10,5,6],
# "e":[25,6,8],
# "f":[5,6,9],
# "g":[10,5,9]
# }
# }
#   --------------------------------------------
  
#   # para acessar o JSON, podemos usar pandas 
  
#   import pandas as pd
  
#   acessar =  pd.read_json('nome_do_arquivo.json')
  
  
  
#   print(acessar)  



# --------------------------------


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import 
# FigureCanvasTkAgg
# import tkinter as tk

# def plot_data():
#     #  ler CSV file
#     data = pd.read_csv('dados.csv')

#     # Extrair data
#     anos = data['ano']
#     vendas = data['vendas']

#     # Criar a figura
#     fig, grafico = plt.subplots()
#     grafico.plot(anos, vendas, marker='o', linestyle='-', color='b')

#     # add as labels
#     grafico.set_xlabel('Ano')
#     grafico.set_ylabel('Vendas')
#     grafico.set_title('Vendas Anuais')

#     # mostrar o grafico
#     canvas = FigureCanvasTkAgg(fig, master=janela)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# # janela tkinter
# janela = tk.Tk()
# janela.title('Gráfico de Vendas')

# # button
# botao = tk.Button(janela, text='Exibir Gráfico', command=plot_data)
# botao.pack(pady=20)

# # loop tkinter
# janela.mainloop()



# ------------------------------

# ### Resumo

# 1.DataFrames: Estruturas de dados bidimensionais com linhas e colunas.
# 2.Filtros: Seleção de dados com base em condições específicas.
# 3.Gráficos: Visualização de dados usando bibliotecas como Matplotlib e Seaborn.

# -------------



# Extraindo dado que possui virgula

# dados.csv:
# ano,Valores
# JAN,"2000,5"
# FEV,"5000,5"


# arquivo.py
# import pandas as pd

# n = []
# dado =  pd.read_csv('dados.csv')

# # extraindo dado do csv
# r = dado['Valores'].str.replace(',','').astype(float).to_list()
# soma  = sum(r)
# print(soma)



# ----------------------------------------------------

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # 1 - Carregamento dos dados

# # 2 Exploração inicial

# # 3 Limpeza e tratamento de dados

# # 4 anlise

# # 5 Visualizações com Matplotlib



# # ----------------------------------------------//----------------------------------------




