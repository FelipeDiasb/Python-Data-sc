import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def ler_csv():
    
 return pd.read_csv('Atividade_forms/dados.csv')
 
# dados = pd.read_csv('Atividade_forms/dados.csv')

# df = pd.DataFrame(dados)

# print(dados)

def calcular_estatisticas(df):
    estatisticas = {
        'Média': np.mean(df),
        'Mediana': np.median(df),
        'Desvio Padrão': np.std(df),
        'Máximo': np.max(df),
        'Mínimo': np.min(df)
    }
    return estatisticas


def mostrar_estatisticas():
      df = ler_csv()
      estatisticas = calcular_estatisticas(df)
      estatisticas_texto = "\n".join([f"{key}: {value}" for key, value in estatisticas.items()])
      messagebox.showinfo("Estatísticas", estatisticas_texto)


def grafico_barras():
      df = ler_csv()
      df.plot(kind='bar')
      plt.title("Gráfico de Barras")
      plt.xlabel("Índices")
      plt.ylabel("Valores")
      plt.show()



def grafico_linha():
     df = ler_csv()
     df.plot(kind='line')
     plt.title("Gráfico de Linha")
     plt.xlabel("Índices")
     plt.ylabel("Valores")
     plt.show()


def grafico_dispersion():
     df = ler_csv()
     plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
     plt.title("Gráfico de Dispersão")
     plt.xlabel("Coluna 1")
     plt.ylabel("Coluna 2")
     plt.show()


def grafico_histograma():
      df = ler_csv()
      df.hist()
      plt.title("Histograma")
      plt.xlabel("Valores")
      plt.ylabel("Frequência")
      plt.show()


def grafico_boxplot():
     df = ler_csv()
     df.boxplot()
     plt.title("Gráfico de Caixa")
     plt.show()


def criar_interface():
    root = tk.Tk()
    root.title("Interface Gráfica de Gráficos")

   
    botao_barras = tk.Button(root, text="Gráfico de Barras", command=grafico_barras)
    botao_barras.pack(pady=5)

    botao_linha = tk.Button(root, text="Gráfico de Linha", command=grafico_linha)
    botao_linha.pack(pady=5)

    botao_dispersion = tk.Button(root, text="Gráfico de Dispersão", command=grafico_dispersion)
    botao_dispersion.pack(pady=5)

    botao_histograma = tk.Button(root, text="Histograma", command=grafico_histograma)
    botao_histograma.pack(pady=5)

    botao_boxplot = tk.Button(root, text="Boxplot", command=grafico_boxplot)
    botao_boxplot.pack(pady=5)

    
    botao_estatisticas = tk.Button(root, text="Mostrar Estatísticas", command=mostrar_estatisticas)
    botao_estatisticas.pack(pady=20)

    
    root.mainloop()

if __name__ == "__main__":
   criar_interface()
