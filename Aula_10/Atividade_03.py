
import matplotlib.pyplot as plt
import numpy as np

#2 - Crie um gráfico plot para mostra:

ano = [2021,2022,2023,2024,2025,2026]

vendas = [10000,2000,30000,10000,5000,20000]


plt.figure(figsize=(8, 4))
plt.subplot(321)
plt.title('Vendas por Ano')
plt.plot(ano, vendas, marker='o', linestyle='-', color='blue') 
plt.xlabel('Ano')
plt.xticks(ano)



plt.subplot(332)
medias_jose = [10, 5, 8, 9, 10, 5, 4]
meses = ['fev', 'mar', 'abril', 'maio', 'junho', 'julho', 'agosto']


#plt.figure(figsize=(10, 5))
plt.bar(meses, medias_jose, color='#1bb289')

plt.title('Médias de José por Mês')  # titulos 
plt.xlabel('Meses')
plt.ylabel('Média')

plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# names = ['group_a', 'group_b', 'group_c', 'd']
# values = [1, 10, 100, 400]

# plt.figure(figsize=(12,4))

# plt.subplot(241)
# plt.bar(names, values)

# plt.subplot(242)
# plt.plot(names, values)

# plt.subplot(243)
# plt.pie( values, labels=values, autopct='%1.1f%%')

# plt.subplot(244)
# plt.scatter(values, values)


# plt.subplot(245)
# plt.bar(names, values)

# plt.subplot(246)
# plt.plot(names, values)

# plt.subplot(247)
# plt.pie( values, labels=values)

# plt.subplot(248)
# plt.scatter(values, values)



# plt.show()