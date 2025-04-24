# # import matplotlib.pyplot as plt
# # import pandas as pd

# # # leitura do arquivo csv

# # dados  = pd.read_csv('train_and_test2.csv')


# # # Exploração 

# # # print(dados.head())
# # # print(dados.info())
# # # print(dados.describe())

# # # limpeza e tratamento dos dados

# # # df =  pd.DataFrame(dados)
# # # print(df)

# # # renomenado 
# # dados = dados.rename(columns={
# #     '2urvived':'Sobreviventes',
# #     'Pclass':'Classes',
# #     'Sex':'Sexo',
# #     'Age':'Idade',
# #     'Fare':'Tarifa'
# # }
# # )

# # # remover colunas desnecessárias

# # dados = dados.loc[:, ~dados.columns.str.contains('zero')]

# # # print(f'{round(dados.head(),2)}')
# # # print(round(dados.info(),2))
# # # print(round(dados['Idade'].describe(),2))
# # # print(dados['Classes'].describe())

# # # # analise básica: 

# # # taxa_sobrevivencia = dados['Sobreviventes'].mean()
# # # print('Média de sobreviventes Titanic', taxa_sobrevivencia)


# # # groupby associação entre as colunas 


# # sobreviventes_por_sexo = dados.groupby('Classes')['Tarifa'].std()
# # print(sobreviventes_por_sexo)

# # sobreviventes_por_classe = dados.groupby('Classes')['Sobreviventes'].mean()
# # print('Por classe:', sobreviventes_por_classe)

# # # visualização dos dados

# # plt.figure(figsize=(15,4))


# # # line
# # plt.subplot(1,3,1)
# # dados.groupby('Sexo')['Sobreviventes'].mean().plot(kind='bar', color='red')
# # plt.title('SOBREVIVENTES POR SEXO')

# # # bar
# # plt.subplot(1,3,2)
# # dados.groupby('Classes')['Sobreviventes'].mean().plot(kind='bar')
# # plt.title('SOBREVIVENTES POR CLASSE')

# # # hist

# # # df = pd.DataFrame(dados)

# # plt.subplot(1,3,3)
# # plt.hist(dados['Idade'].dropna(), bins=20)


# # plt.tight_layout()
# # plt.show()





# ****************************************************

# #  gráfico de linha
# def grafico_linha():
#     df = ler_csv()
#     df.plot(kind='line')
#     plt.title("Gráfico de Linha")
#     plt.xlabel("Índices")
#     plt.ylabel("Valores")
#     plt.show()

# #   gráfico de (scatter)
# def grafico_dispersion():
#      df = ler_csv()
#      plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
#      plt.title("Gráfico de Dispersão")
#      plt.xlabel("Coluna 1")
#      plt.ylabel("Coluna 2")
#      plt.show()

# #  histograma
# def grafico_histograma():
#      df = ler_csv()
#      df.hist()
#      plt.title("Histograma")
#      plt.xlabel("Valores")
#      plt.ylabel("Frequência")
#      plt.show()

# # gráfico de caixa (boxplot)
# def grafico_boxplot():
#     df = ler_csv()
#     df.boxplot()
#     plt.title("Gráfico de Caixa")
#     plt.show()

# # # Função para criar a interface gráfica com Tkinter
# # def criar_interface():
# #     root = tk.Tk()
# #     root.title("Interface Gráfica de Gráficos")

# #     # Botões para gerar gráficos
# #     botao_barras = tk.Button(root, text="Gráfico de Barras", command=grafico_barras)
# #     botao_barras.pack(pady=5)

# #     botao_linha = tk.Button(root, text="Gráfico de Linha", command=grafico_linha)
# #     botao_linha.pack(pady=5)

# #     botao_dispersion = tk.Button(root, text="Gráfico de Dispersão", command=grafico_dispersion)
# #     botao_dispersion.pack(pady=5)

# #     botao_histograma = tk.Button(root, text="Histograma", command=grafico_histograma)
# #     botao_histograma.pack(pady=5)

# #     botao_boxplot = tk.Button(root, text="Boxplot", command=grafico_boxplot)
# #     botao_boxplot.pack(pady=5)

# #     # Botão para mostrar estatísticas
# #     botao_estatisticas = tk.Button(root, text="Mostrar Estatísticas", command=mostrar_estatisticas)
# #     botao_estatisticas.pack(pady=20)

# #     # Iniciar a interface
# #   root.mainloop()

# # if __name__ == "__main__":
# #    criar_interface()
