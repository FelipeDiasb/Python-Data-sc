def sub(a,b):
    return a - b


def soma(a,b):
    return a + b


def mult(a,b):
    return a * b


def div(a,b):
    return a / b




def calculadora():
 while True:    
    n1 = float(input('>>'))
    op = input('Escolha a operação = +|-|*|/')
    if op == '+':
        n2 = float(input('>>'))
        print(soma(n1,n2))
        
    elif op == '-':
        n2 = float(input('>>'))
        print(sub(n1,n2))  
                  
    elif op == '*':
        n2 = float(input('>>'))
        print(mult(n1,n2))  


    elif op == '/':
        n2 = float(input('>>'))
        print(div(n1,n2))  
                          


calculadora()                  