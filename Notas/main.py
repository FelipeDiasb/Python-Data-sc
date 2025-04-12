# main.py
from dados import carregar_dados
from Notas.alunos import processar_alunos, exibir_relatorio

def main():
    dados_alunos = carregar_dados()
    relatorio = processar_alunos(dados_alunos)
    exibir_relatorio(relatorio)

if __name__ == "__main__":
    main()
