# pip install pytest-timeit

# def soma1 ():
#     lista =  list(range(1,2000))
#     print(lista)
#     return lista

# # soma1()
# time = timeit.timeit(soma1, number=10)
# print('função1', time)

# def soma():
#     aleatorio1 =  np.random.randint(1,10,(5,10))
#     soma2  =  np.sum(aleatorio1)
#     return soma2

# time = timeit.timeit(soma, number=10)
# print('função2', time)
# esafio 1:
# 1. Crie um array de 20 elementos.

# 2. Extraia os primeiros 5 elementos, os últimos 5 
# elementos e os elementos 
# das posições 5 a 10.


# Desafio 2:
# 1. Crie duas matrizes 3x3.
# 2. Calcule o produto.


# Desafio 3:
# Criação de Arrays:

# Crie um array de 1 a 10.
# Crie uma matriz 3x3 com valores aleatórios entre 0 e 1.

# Desafio 4:
# Calcule a soma dos elementos do array.
# Encontre o valor máximo e mínimo do array.


# Desafio 5:
# Calcule a média dos valores do array.
# Calcule a mediana dos valores do array.


# Desafio 6:
# Adicione 10 a todos os elementos do array.
# Reshape o array 1D para um array 2D (2x5


import numpy as np

# Desafio 1:
# 1. Crie um array de 20 elementos.
# 2. Extraia os primeiros 5 elementos, os últimos 5 
# elementos e os elementos 
# das posições 5 a 10.

# vetor =  np.arange(1,21)
# print(vetor)
# cinco_p = vetor[0:5]
# print(cinco_p) 
# cinco_u = vetor[-5:]
# print(cinco_u)
# cinco_a_dez =  vetor[4:10]
# print(cinco_a_dez)



# Desafio 2:
# 1. Crie duas matrizes 3x3.
# 2. Calcule o produto.

n = np.random.randint(1,5, (3,3))
n2 = np.random.randint(1,5, (3,3))
print(n)
print(n2)
c = n * n2
print(c)

l = [1,3,4,10]
m = [4,2,5, 10]

mult = np.dot(l,m)
print(mult)



# Desafio 3:
# Criação de Arrays:

# Crie um array de 1 a 10.
n = np.array([1,11])

# Crie uma matriz 3x3 com valores aleatórios entre 0 e 1.

ale =  np.random.randint(0,1, (3,3))
print(ale)

# Desafio 4:
# Calcule a soma dos elementos do array.

soma  =  np.sum(ale)

# Encontre o valor máximo e mínimo do array.

min =  np.min(soma)


# Desafio 5:
# Calcule a média dos valores do array.
# Calcule a mediana dos valores do array.


# Desafio 6:
# Adicione 10 a todos os elementos do array.

ale =  ale + 10
print(ale)

# Reshape o array 1D para um array 2D (2x5).
# # 

n = np.arange(1,11)
p = np.arange(1,11) 
print(n)

format  =  np.concatenate([n,p])
# print(format)
novo = n.reshape(2,5)
print(novo)