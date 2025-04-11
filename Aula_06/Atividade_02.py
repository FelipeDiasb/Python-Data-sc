from statistics import median
from math import isnan
from itertools import filterfalse

data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
sorted(data)  # Isso tem um comportamento surpreendente

median(data)  # Este resultado é inesperado


sum(map(isnan, data))    # Número de valores em falta

clean = list(filterfalse(isnan, data))  # Remove valores NaN
clean

sorted(clean)  # A classificação agora funciona como esperado

median(clean)       # Este resultado é agora bem definido
