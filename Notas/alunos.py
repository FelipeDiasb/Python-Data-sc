# alunos.py
from statistics import calcular_estatisticas

def processar_alunos(dados_alunos):
    relatorio = {}
    for nome, notas in dados_alunos.items():
        relatorio[nome] = calcular_estatisticas(notas)
    return relatorio

def exibir_relatorio(relatorio):
    for aluno, stats in relatorio.items():
        print(f"\n📚 Estatísticas de {aluno}:")
        for chave, valor in stats.items():
            print(f"{chave.capitalize().replace('_', ' ')}: {valor}")



#***************modulo Aluno**********