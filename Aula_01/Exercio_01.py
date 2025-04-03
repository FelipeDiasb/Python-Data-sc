


print ('''------Calculadora-------- '
       ''')

peso = float(input("\nDigite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))


def calcular_imc(peso, altura):
        return peso / (altura ** 2)


def classificar_imc(imc):
     if imc < 18.5:
         return "Abaixo do normal"
     elif 18.5 <= imc < 24.9:
         return "Peso normal"
     elif 25 <= imc < 30:
         return "Sobrepeso"
     elif 30 <= imc < 34.9:
         return "Obesidade grau I"
     elif 35 <= imc < 39.9:
          return "Obesidade grau II"
     else:
         return "Obesidade grau III"


def mostrar_tabela ():
     
          print("\nTabela de IMC:")
          print("IMC < 18,5: Abaixo do normal")
          print("18,5 - 24,9: Peso normal")
          print("25 - 30: Sobrepeso")
          print("30 - : Obesidade")
          print("Acima de 40: Obesidade grave")

mostrar_tabela()

def calcular_e_classificar_imc():


    imc = calcular_imc(peso, altura)
    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificar_imc(imc)}")

print ('''
       
        ''')

calcular_e_classificar_imc()
