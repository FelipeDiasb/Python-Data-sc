import numpy as np

def gerar_numeros():
   
    pares = np.arange(2, 61, 2)
    impares = np.arange(1, 60, 2)
    
    
    pares = np.random.choice(pares, 3, replace=False)
    impares = np.random.choice(impares, 3, replace=False)
    
 
    nu = np.concatenate((pares, impares))
    np.random.shuffle(nu) 
    
    return nu


print("Números:", gerar_numeros())


