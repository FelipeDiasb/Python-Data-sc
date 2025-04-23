

# def soma():
#     n1 = float(input_entry.get())
#     n2 = float(input_entry2.get())
#     soma  =  n1 + n2
#     label_resultado.config(text=soma)

# # Criando a tela
# janela  = tk.Tk()
# janela.geometry('500x500')
# janela.title('TESTANDO TKINTER')

# #Criando um título para a tela
# text_label = tk.Label(janela, text='calculadora' )
# text_label.pack()

# #inserir dados
# input_entry = tk.Entry(janela)
# input_entry.pack()
# input_entry2 = tk.Entry(janela)
# input_entry2.pack()

# #Criando um botão
# botao = tk.Button(janela, text ='clique aqui', command=soma)
# botao.pack()

# #Visualizando o resltado na tela
# label_resultado = tk.Label(janela, text='Resultado')
# label_resultado.pack()

# # Mantendo a tela em loop 
# janela.mainloop()

# ---------------------------
import tkinter as tk 

def soma():
    n1 = float(input_entry.get())
    n2 = float(input_entry2.get())
    soma = n1 + n2
    resultado.config(text = f'={soma}')



janela  =  tk.Tk()
janela.title('CALCULADORA')
janela.geometry('300x300')

texto = tk.Label(janela, text='INSIRA O PRIMEIRO Nº')
texto.pack()

input_entry = tk.Entry(janela)
input_entry.pack()


text2 = tk.Label(janela, text = 'INSIRA O SEGUNDO Nº')
text2.pack()

input_entry2 = tk.Entry(janela)
input_entry2.pack()

btn = tk.Button(janela, text = '+', command=soma)
btn.pack()

resultado = tk.Label(janela, text = 'Resultado:')
resultado.pack()

janela.mainloop()