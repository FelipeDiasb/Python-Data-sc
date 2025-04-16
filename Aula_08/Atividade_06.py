# # Arrays NumPy
# # O objeto central do NumPy é o array. Aqui estão alguns exemplos de como 
# # criar e manipular arrays.

# # Criando Arrays

# # Array a partir de uma lista:


# # lista = [1, 2, 3, 4, 5]
# # array = np.array(lista)
# # print(array)


# # Array de zeros:

# # zeros = np.zeros(5)
# # print(zeros)
# # Array de uns:


# # ones = np.ones((2, 3))  # Array 2x3
# # print(ones)


# # Array com valores uniformemente espaçados:

# # espacado = np.arange(0, 10, 2)  # Início, fim, passo
# # print(espacado)


# # Array com valores linearmente espaçados:

# # linear = np.linspace(0, 1, 5)  # Início, fim, número de pontos
# # print(linear)
# # Operações com Arrays
# # Operações element-wise:


# # a = np.array([1, 2, 3])
# # b = np.array([4, 5, 6])
# # print(a + b)  # Soma
# # print(a - b)  # Subtração
# # print(a * b)  # Multiplicação
# # print(a / b)  # Divisão


# # Funções universais:

# # a = np.array([1, 2, 3])
# # print(np.sqrt(a))  # Raiz quadrada
# # print(np.exp(a))   # Exponencial
# # print(np.sin(a))   # Seno


# # Estatísticas e Agregações


# # Média, variância e desvio padrão:


# # dados = np.array([1, 2, 3, 4, 5])
# # print(np.mean(dados))      # Média
# # print(np.var(dados))       # Variância
# # print(np.std(dados))       # Desvio padrão


# # Soma e produto:

# # dados = np.array([1, 2, 3, 4, 5])
# # print(np.sum(dados))       # Soma
# # print(np.prod(dados))      # Produto



# # Máximo e mínimo:
# # dados = np.array([1, 2, 3, 4, 5])
# # print(np.max(dados))       # Valor máximo
# # print(np.min(dados))    

# #    # Valor mínimo
# # Manipulação de Arrays

# # Redimensionamento:


# # dados = np.arange(6)
# # dados_reshape = dados.reshape((2, 3))
# # print(dados_reshape)



# # Indexação e fatiamento:
# # dados = np.array([1, 2, 3, 4, 5])
# # print(dados[1:4])  # Elementos de 1 a 3
# # print(dados[:3])   # Primeiros 3 elementos
# # print(dados[::2])  # Elementos com passo 2


# # Filtro Booleano:

# # dados = np.array([1, 2, 3, 4, 5])
# # filtro = dados > 3
# # print(dados[filtro])  # Elementos maiores que 3


# # Concatenar arrays:

# # a = np.array([1, 2, 3])
# # b = np.array([4, 5, 6])
# # c = np.concatenate((a, b))
# # print(c)


# # Funções Matemáticas


# # Funções de arredondamento:

# # dados = np.array([1.2, 2.5, 3.8])
# # print(np.round(dados))    # Arredondar ao inteiro mais próximo
# # print(np.floor(dados))    # Arredondar para baixo
# # print(np.ceil(dados))     # Arredondar para cima



# # Trigonometria:

# # angulos = np.array([0, np.pi/2, np.pi])
# # print(np.sin(angulos))    # Seno
# # print(np.cos(angulos))    # Cosseno
# # print(np.tan(angulos))    # Tangente



# # Operações com matrizes:

# # matriz = np.array([[1, 2], [3, 4]])
# # print(np.transpose(matriz))   # Transposição
# # print(np.linalg.inv(matriz))  # Inversa




# # aleatorios =  np.random.randint(0,11)
# # aleatorios

# # t =  np.random.default_rng()
# # teste = t.random((10,5))
# # teste



# # E em Arrays 3D?
# # Para um array (3, 2, 4) (3 blocos, 2 linhas, 4 colunas):

# # axis=0 → opera entre blocos.

# # axis=1 → opera entre linhas dentro de cada bloco.

# # axis=2 → opera entre colunas dentro de cada bloco.

# # ATIVIDADE 1:

# import numpy as np

# # Crie um array NumPy [1, 2, 3, 4, 5] e:

# # Multiique todos os elementos por 10.

# # Calcule a média dos valores.

# # Substitua os números pares por -1.

# ar = np.array([1, 2, 3, 4, 5])
# # Multiique todos os elementos por 10.
# m = ar * 200
# m
# # Calcule a média dos valores.
# media  =  np.mean(ar)
# media
# # Substitua os números pares por -1.
# x = -1
# r = ar [ar % 2 == 0 ] = x
# ar

# filtro = ar > 7
# x = ar[filtro]


# #-------------------------------------------------------------------

# # ATIVIDADE 2:

# # Crie um array 2D de tamanho (5, 5) com valores aleatórios entre 0 e 100.

# # Calcule a média de cada linha.

# # Encontre o valor máximo e mínimo de toda a matriz.


# #---------------------------------------------------------------------------

# # 3 - EXPLOQUE A DOCUMENTAÇÃO 


# # https://numpy.org/doc/stable/

# # vendas = np.array([120,90,150,80,200,110,50,300])


# # Filtre apenas as vendas maiores que 100.

# # Calcule quantas vendas ficaram abaixo da média.

# # Crie um novo array com os valores normalizados (divida cada valor pelo máximo).


# import numpy as np

# # ATIVIDADE 2:

# # Crie um array 2D de tamanho (5, 5) 
# # Com valores aleatórios entre 0 e 100.
# # Calcule a média de cada linha.
# # Encontre o valor máximo e mínimo de toda 
# # a matriz.

# dados =  np.random.randint(0,100, size=(5,5))
# print(dados)

# media = np.mean(dados, axis=1)
# print(media)

# maior, menor  =  np.max(dados), np.min(dados)
# print(maior, menor)



# # 3 - EXPLOQUE A DOCUMENTAÇÃO 
# # https://numpy.org/doc/stable/
# vendas = np.array([120,90,150,80,200,110,50,300])
# # Filtre apenas as vendas maiores que 100.

# filtro =  vendas[vendas>100]
# print(filtro)



# # Calcule quantas vendas ficaram abaixo da média.

# tamanho = len(vendas[vendas < np.mean(vendas)])
# print(tamanho)


# # Crie um novo array com os valores normalizados 
# # (divida cada valor pelo máximo).


# nova_array = [vendas/np.max(vendas)]

# # l = []
# # for n in vendas:
# #     v = n/max(vendas)
# #     l.append(v) 
# # nova = np.array(l)
# # print(nova)


# print(nova_array)


# import numpy as np

# # dir serve para descobrir os métodos para aquele 
# # objeto
# ar = np.array([1,2,3,4])

# function= dir(ar)

# print(function)

import numpy as np


# ar =  np.random.randint(0,100, size = (5,5))


# minino =  np.min(ar)
# maior = np.max(ar)
# media  =  np.mean(ar)
# print(ar, maior, minino, media)



vendas = np.array([120,90,150,80,200,110,50,300])
# filtro
filtro = vendas[vendas > 100]
print(filtro)
media  =  np.mean(vendas)
# media
print(media)
abaixo = len(vendas[vendas < np.mean(vendas)])
# nova array 
nova  =  [vendas/np.max(abaixo)]
print(nova)