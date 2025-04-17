

# 1. Array a partir de uma lista:

#    import numpy as np
#    lista = [1, 2, 3, 4, 5]
#    array = np.array(lista)
   

# 2. Array de zeros:

#    array_zeros = np.zeros(5)
   

# 3. Array de uns:

#    array_uns = np.ones(5)
   

# 4. Array de uma sequência de números:

#    array_sequencia = np.arange(10)  # Array de 0 a 9
   

# 5. Array de uma sequência de números com espaçamento definido:

#    array_espacamento = np.arange(0, 10, 2)  # Array de 0 a 8 com espaçamento de 2
   

# 6. Array de números igualmente espaçados:

#    array_espacado = np.linspace(0, 1, 5)  # 5 números de 0 a 1 igualmente espaçados
   

# ### Operações com Arrays

# 7. Soma, subtração, multiplicação e divisão:

#    a = np.array([1, 2, 3])
#    b = np.array([4, 5, 6])
#    soma = a + b
#    subtracao = a - b
#    multiplicacao = a * b
#    divisao = a / b
   

# 8. Raiz quadrada e exponenciação:

#    raiz_quadrada = np.sqrt(a)
#    exponenciacao = np.exp(a)
   

# ### Estatísticas

# 9. Média, mediana e desvio padrão:

#    dados = np.array([1, 2, 3, 4, 5])
#    media = np.mean(dados)
#    mediana = np.median(dados)
#    desvio_padrao = np.std(dados)
   

# 10. Máximo, mínimo e soma:
 
#     maximo = np.max(dados)
#     minimo = np.min(dados)
#     soma = np.sum(dados)
    

# ### Manipulação de Arrays

# 11. Redimensionar um array:
 
#     array_reshape = np.arange(6).reshape((2, 3))  # 2 linhas e 3 colunas
    

# 12. Indexação e fatiamento:
 
#     array = np.array([1, 2, 3, 4, 5])
#     primeiro_elemento = array[0]
#     ultimos_tres = array[-3:]
    
# slice: 
    
# vetor = np.arange(1,30)
# print(vetor[0])

# percorer = vetor[-25:-19]
# print(percorer)
    

# 13. Filtragem com condições:
 
#     condicao = array > 2
#     filtrado = array[condicao]  # Elementos maiores que 2
    

# 14. Concatenação de arrays:
 
#     a = np.array([1, 2, 3])
#     b = np.array([4, 5, 6])
#     concatenado = np.concatenate((a, b))
    
# --------------------------------------------

# teste  = np.array([[1,2,3], [4,5,6], [7,8,9], [1,10,0]]) # 4x3
# # teste[3][1] = 20
# # teste

# # print(teste.shape) # mostrar como a  matriz está estrutrada
# # print(teste.size)  # tamanho
# # print(teste.ndim)  # numero de dimensões - x e y


# # soma =  teste + teste
# # soma


# numeros =  np.random.random()
# numeros = np.random.randint(1,50) # vetor aleatorio
# numeros = np.random.randint(1,50, (5)) # com uma coluna de 5 numero
# numeros = np.random.randint(1,50, (5,10)) # com 5 linhas 10 colunas
# numeros = np.random.randint(1,50, (5,10,3)) # com 3 matriz 
#                                           5 linhas 10 colunas,
                                                  


# x =  np.array([1,11])
# y =  np.array([1,11])
# aleatorio1 =  np.random.randint(1,10,(5,10))
# print('1:', aleatorio1)
# aleatorio2 =  np.random.randint(1,10,(5,10))
# print('2', aleatorio2)


# print(np.sum(teste))
# print(np.min(teste))
# print(np.max(teste))
# print(np.std(teste))

