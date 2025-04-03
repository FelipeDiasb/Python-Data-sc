# Exemplos:

numero =  12
text =  "Isso é um texto"
dado =  8.12
v =  True
f  =  False 


# CONCATENAÇÃO: 

# naturalmente mostra um dado do tipo texto

nome  = str(input('Digite um nome '))
idade  = int(input('Digite outro idade'))
endereco = input('Digite seu endereço')
curso =  'Programação em Python'
cumprimento  = 'Olá, como vai'

#concatenar é juntar um texto com uma variável, mas tb posso juntar
# 2 variáveis

# concatenar =  juntar os dados 
# 5 formas

nome  =  input('Digite o seu nome: ')
print('Olá '+''+ nome)
print('Olá {}'.format(nome))
print('Olá %s '%(nome))
print(f'Olá {nome}')
print('Olá', nome)


print(cumprimento, nome)
print('Nome', nome)
print('Endereço', endereco)
print('Idade', idade)
print('Curso', curso)



# Para melhorar a explicação, imagine uma caixa, que possue um nome e dados 
# alocados nela.

# O sinal de igual é uma atribuição (=), não é uma comparação, você está guardando 
# um dado não comparando algo.     