# São variáveis  
# espaços na memoria da máquina

texto = 'Ana'
numero_inteiro = 10 
numero_real = 0.10
dado_boleano = True

# print() -> mostrar  ou  imprimir dados no console
print(texto)
print(numero_inteiro)
print(numero_real)
print(dado_boleano)


#type() - verificar o tipo de dado 

print(type(texto))
print(type(numero_inteiro))
print(type(numero_real))
print(type(dado_boleano))

# concatenação == juntar textos, variáveis, resultados

text = type(texto)

inteiro  = type(numero_inteiro)
real = type(numero_real)
boleano = type(dado_boleano)

print('Essa variável ->', texto,'é da', text  )
print('Essa variável ->', numero_inteiro,'é da', inteiro  )
print('Essa variável ->', numero_real,'é da', real)
print('Essa variável ->', dado_boleano,'é da', boleano  )

print(f'Essa variável ->, {texto},é da, {text} ' )
print(f'Essa variável ->, {numero_inteiro},é da, {inteiro} ' )
print(f'Essa variável ->, {numero_real},é da, {real}')
print(f'Essa variável ->, {dado_boleano},é da, {boleano} ' )


print((1+3)+3 ** 2/5)


nome  = input('digite seu nome: ')
print(nome)


x = '10'
text = int(x)
n = text  + 1
print(n)


# ----------------------


# n1 =  float(input('Digite um número:'))
# n2 =  float(input('Digite outro número:'))


# print(f'''
# Resultado da soma: {n1+n2}
# Resultado da divisão: {n1//n2}
# Resultado da Multiplicação: {n1*n2}
# Resultado da subtração: {n1-n2}
# '''
# )


# ### Sobre Tuplas 


# # lista = [10,15,3,1,5]
# # indice = lista[0]
# # indice2 = lista[1] 
# # print(indice + indice2)
# # numeros1 = list(range(1,11,2))
# # print(numeros1)

# # comprimento/ tamanho  ==  len()
# lista = [10,15,3,2,5]
# menor1 = min(lista)
# print(len(lista))
# print('menor numero:', menor1)


# # add  == append()
# lista.append(10)
# print(lista)

# #transformar uma variável em uma lista do tipo str
# variavel  = 'text'
# lista2 = list(variavel)
# print(lista2)

# # criar uma lista com list()
# cria_sequencia  = list(range(1,101))
# soma  =  sum(cria_sequencia)
# print(soma)


# # max e min 
# menor  = min(lista2)
# print(menor)

# maior = max(lista2)
# print(maior)
 
# lista3 =  [6456,56,45,1,89,11100,1,9,7]
# organizar = sorted(lista3)
# print(organizar)


# # pop() -> remover um indice
# lista3.pop(0)
# print(lista3)

# lista3.remove(89)

# del lista3[0]
# print(lista3)



# -----------------------

# ### Sobre Tuplas


# # Tuplas 
# # Lista imutáveis 
# # Usamos parenteses

# lista = [1,33]

# lista[0] = 22

# print(lista)

# tupla2 = tuple(lista)
# print(tupla2)



# tupla =  (1,2,150,6,9,9,9,9)
# print(tupla[2])
# # conta a quantidade de valores 
# # que foi declarado no parenteses
# contador  = tupla.count(9)

# # verifica o indice do valor 
# indice = tupla.index(9)
# print(contador, indice)

# # tamanho len()
# print(len(tupla))

# #max e min


# maior  =  max(tupla)
# menor = min(tupla)
# print(menor, maior)

# ordenar = sorted(tupla)
# print(ordenar)

# tupla4 = (1,4546,1,89,3,4,656)
# sorted(tupla4)
# a,b,c,d,e,f,g= tupla4
# numero =  tupla4[1]
# print(numero)
# print(a,b,c,d,e,f,g)









