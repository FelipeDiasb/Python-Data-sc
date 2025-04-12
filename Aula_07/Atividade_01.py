## Desafio 1

# ***Você é um profissional em transição de carreira e está avaliando novas oportunidades de emprego.***

# ***Utilize estatísticas como média, moda, mediana e desvio padrão, amplitude, variância para analisar as faixas salariais oferecidas por diferentes empresas e tomar uma decisão embasada.***

# ***Explique sua escolha com base nos dados analisados***


# Média: tendência central (valor "esperado")

# Mediana: valor do meio (resiste a outliers)

# Moda: valor mais comum (se existir)

# Desvio padrão: mostra o quanto os salários variam em torno da média

# Variância: quadrado do desvio padrão (também mede dispersão)

# Amplitude: diferença entre o maior e o menor salário





import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

empresas = {
    "Empresa 1": [2500, 2800, 3000, 9500, 12000],
    "Empresa 2": [5000, 5200, 5300, 5400, 5500],
    "Empresa 3": [1000, 2000, 8000, 15000, 20000],
    "Empresa 4": [3500, 4000, 4200, 4300, 6000],
    "Empresa 5": [1200, 1500, 1800, 2500, 10000]
}


salario_desejado = float(input("Digite o salário que você gostaria de ganhar: R$ "))


salario_valido = any(
    np.min(salarios) <= salario_desejado <= np.max(salarios)
    for salarios in empresas.values()
)

if not salario_valido:
    print("\n ⚠️Nenhuma empresa possui salários compatíveis com o valor desejado.")
    print("📌Veja as faixas salariais disponíveis em cada empresa:\n")
    for nome, salarios in empresas.items():
        print(f"{nome}: de R$ {min(salarios)} até R$ {max(salarios)}")
    exit()

print("\n📈 ANÁLISE DETALHADA DE TODAS AS EMPRESAS:\n")

melhor_empresa = None
menor_diferenca = float('inf')

# Guarda os resultados para mostrar no final
resultados_empresas = []
salarios_para_boxplot = []
nomes_empresas = []

for nome, salarios in empresas.items():
    salarios_np = np.array(salarios)
    
    media = np.mean(salarios_np)
    mediana = np.median(salarios_np)
    try:
        moda = stats.mode(salarios_np, keepdims=False).mode
    except:
        moda = "Sem moda"
    desvio_padrao = np.std(salarios_np)
    variancia = np.var(salarios_np)
    amplitude = np.max(salarios_np) - np.min(salarios_np)

    # Armazena resultados
    resultados_empresas.append({
        "nome": nome,
        "media": media,
        "mediana": mediana,
        "moda": moda if isinstance(moda, str) else moda,
        "desvio_padrao": desvio_padrao,
        "variancia": variancia,
        "amplitude": amplitude,
        "min_salario": np.min(salarios_np),
        "max_salario": np.max(salarios_np)
    })

    
    salarios_para_boxplot.append(salarios)
    nomes_empresas.append(nome)

    # Verifica se salário desejado está dentro da faixa da empresa
    if np.min(salarios_np) <= salario_desejado <= np.max(salarios_np):
        diferenca = abs(media - salario_desejado)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            melhor_empresa = nome

# Mostra estatísticas de todas as empresas para usuário ver qual deseja ver 
for e in resultados_empresas:
    print(f"📊 {e['nome']}")
    print(f"  - Média salarial: R$ {e['media']:.2f}")
    print(f"  - Mediana: R$ {e['mediana']:.2f}")
    print(f"  - Moda: {e['moda'] if isinstance(e['moda'], str) else 'R$ ' + str(e['moda'])}")
    print(f"  - Desvio padrão: R$ {e['desvio_padrao']:.2f}")
    print(f"  - Variância: R$ {e['variancia']:.2f}")
    print(f"  - Amplitude: R$ {e['amplitude']:.2f}")
    print(f"  - Faixa salarial: R$ {e['min_salario']} a R$ {e['max_salario']}")
    print("")


print("🔍 RECOMENDAÇÃO FINAL:") 
print(f"✅ Com 🫡base no salário desejado de R$ {salario_desejado:.2f}, a empresa mais adequada é: **{melhor_empresa}**") # Recomendação final

# Boxplot para visualização gráfico de coluna de pesquisa que não ficou muito bom 
plt.figure(figsize=(10, 6))
plt.boxplot(salarios_para_boxplot, labels=nomes_empresas, patch_artist=True)
plt.axhline(y=salario_desejado, color='r', linestyle='--', label=f'Salário Desejado: R$ {salario_desejado:.2f}')
plt.title("Distribuição Salarial por Empresa")
plt.ylabel("Salários (R$)")
plt.xlabel("Empresas")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()


# d = {}


# s =  input('Digite sim para continuar: ')
# while s == 'sim':
#     nome = input('Digite nome:')
#     n1 = int(input('Digite dado: '))
#     n2 = int(input('Digite dado: '))
#     n3 = int(input('Digite dado: '))
#     d[nome] = [n1,n2,n3]
#     s =  input('Digite sim para continuar: ')


# print(d)    