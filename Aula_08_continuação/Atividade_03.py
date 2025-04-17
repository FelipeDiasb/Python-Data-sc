# Desafio 1:
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
# Reshape o array 1D para um array 2D (2x5).


import numpy as np

#01 
array =  [i for i in range(20)]

print(f'20 elementos',array)

#02

primeiros_05 = array[:5]

print(f'primeiros:',primeiros_05)

ultmos_05 = array[-5:]

print(f'Ultimos:',ultmos_05)

elementos_5_a_10 = array[5:11]

print(f'Extração:',elementos_5_a_10)

# Desafio 02

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])


produto = np.dot(matriz1,matriz2)


print("Matriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\nProduto das matrizes:")
print(produto)


#Desafio 3:


array_1_a_10 = np.arange(1, 11)

matriz_aleatoria = np.random.rand(3, 3)

print("Array de 1 a 10:")
print(array_1_a_10)

print("\nMatriz 3x3 com valores aleatórios entre 0 e 1:")
print(matriz_aleatoria)


#Desafio 4 

soma = np.sum(array_1_a_10)#-----------------------------------------

valor_maximo = np.max(array_1_a_10)
valor_minimo = np.min(array_1_a_10)

print("Array de 1 a 10:")
print(array_1_a_10)

print("\nSoma dos elementos do array:", soma)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)


#Desafio 4 

media = np.mean(array_1_a_10)

mediana = np.median(array_1_a_10)

print("Array de 1 a 10:")
print(array_1_a_10)

print("\nMédia :", media)
print("Mediana:", mediana)

#Desafio 6:

array_adicionado = array_1_a_10 + 10

array_2d = array_adicionado.reshape(2, 5)

print("Array original de 1 a 10:")
print(array_1_a_10)

print("\nArray após adicionar 10 :")
print(array_adicionado)

print("\nArray(2x5):")
print(array_2d)


#--------------------Resolução professora

# import numpy as np 

# frequencia  = np.arange(1,21)
# # 1. 5 primeiro elementos 
# primeiro_5 = frequencia[0:4]

# # 2. 5 último
# ultimos_5 = frequencia[15:]
# print(ultimos_5)

# # 3. 5 das posições 5 a 10.
# posicao = frequencia[5:10]
# print(posicao)

# # Crie duas matrizes 3x3.
# matriz = np.random.randint(1,3,(3,3))
# matriz2 = np.random.randint(1,3,(3,3))
# # c = np.arange(9).reshape((3,3))
# c1 = np.arange(9).reshape((3,3))
# # print(c*c1)

# # matriz2 = np.random.randint(1,3,(3,3))

# # r = np.arange(1,21,(3,3))
# # print(r)
# # print(matriz)
# ar =  np.arange(1,11)
# print(ar)

# m = np.random.randint(0,2,(3,3))
# maximo = np.max(m)
# minimo = np.min(m)
# media = np.mean(m)
# mediana = np.median(m)
# print(minimo, maximo, m, media, mediana)
# soma  =  np.sum(m)
# print(soma)

# x = [n for n in ar + 10]
# b = np.array(x).reshape(2,5) 
# print(b)




# # l = []
# # for n in ar:
# #     for x  in n:
# #         c =  x  + 10
# #         l.append(c)
# # print(l)

# # n = np.array(l).reshape(2,5)





        
   
     
