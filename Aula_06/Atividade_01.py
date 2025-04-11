 


# Media da soma dos valores e a contagem de objetos.
dados = [1, 2, 3, 4, 5]
media = sum(dados) / len(dados)
print(f"Média: {media}")




#  A moda é o valor que aparece com maior frequência em um conjunto de dados.
import statistics 


dados = [1, 2, 2, 3, 4, 4, 4, 5]
moda = statistics.mode(dados)
print(f"Moda: {moda}")



#- Cálculo em Python:
  
# dados = [1, 2, 3, 4, 5]
# dados.sort()
# n = len(dados)
# mediana = (dados[n//2] if n % 2 != 0 else (dados[n//2 - 1] + dados[n//2]) / 2)
# print(f"Mediana: {mediana}")


# from collections import Counter

# lista  =  [1,2,3,6,6]

# n = Counter(lista)

# moda  =  n.most_common()

# print(moda)






# # moda


# # def moda(lista):
# #     c = {}
# #     for i in lista:
# #         c[i] = c.get(i,0) + 1
# #     print(c)    

# #     moda  =  max(c, key=c.get)
# #     print(moda)




# lista = [1,2,45,6,5,6,6,6]
# moda  = 1
# for i in lista:
#     c =  lista.count(i)
#     if c > 1:
#        moda = i
#        if c > moda:
#            moda  =  c
# print(moda)






# # def media(lista):
# #     m  =  sum(lista)/len(lista)
# #     return m

# # def mediana(lista):
# #     lista.sort()
# #     n = len(lista)
# #     mediana = (lista[n//2] if n % 2 != 0 else (lista[n//2 - 1] + lista[n//2]) / 2)
# #     print(f"Mediana: {mediana}")

# # lista = [1,2,45,6,5,6,6,6]
# # media(lista)
# # moda(lista)
# # mediana(lista)



import statistics as st


# moda

f = [1,2,6,9,5,9,9,9,3]
moda = st.mode(f)
print(moda)

# media 
# mediana 




 