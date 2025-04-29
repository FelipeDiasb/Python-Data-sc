import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Função para carregar dados e gerar gráficos
def carregar_dados():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return  # Se o usuário cancelar
    
    df = pd.read_excel(file_path)
    
    # Gráfico de Barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df.columns[0], y=df.columns[1], data=df)
    plt.title('Gráfico de Barras')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Gráfico de Linhas
    plt.figure(figsize=(10, 6))
    plt.plot(df[df.columns[0]], df[df.columns[1]], marker='o')
    plt.title('Gráfico de Linhas')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Gráfico 3D
    if len(df.columns) >= 3:
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(df[df.columns[0]], df[df.columns[1]], df[df.columns[2]], c='r', marker='o')
        ax.set_title('Gráfico 3D')
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel(df.columns[1])
        ax.set_zlabel(df.columns[2])
        plt.tight_layout()
        plt.show()
    
    # Exibir estatísticas básicas
    estatisticas = df.describe()
    estatisticas_text.delete('1.0', tk.END)
    estatisticas_text.insert(tk.END, str(estatisticas))

# Criar janela principal
root = tk.Tk()
root.title("Dashboard de Dados")
root.geometry("800x600")

# Botão para carregar dados
btn_carregar = tk.Button(root, text="Carregar Dados", command=carregar_dados, bg='#4CAF50', fg='white', font=('Helvetica', 12, 'bold'))
btn_carregar.pack(pady=20)

# Área para exibir estatísticas
estatisticas_frame = tk.LabelFrame(root, text="Estatísticas Básicas", padx=10, pady=10, font=('Helvetica', 12, 'bold'))
estatisticas_frame.pack(padx=10, pady=10, fill="both", expand=True)

estatisticas_text = tk.Text(estatisticas_frame, wrap=tk.WORD, height=10, font=('Helvetica', 10))
estatisticas_text.pack(fill="both", expand=True)

# Rodar o aplicativo
root.mainloop()
