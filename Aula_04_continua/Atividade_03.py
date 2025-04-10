```python
carrinho = []

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Ver carrinho")
    print("4. Calcular total")
    print("5. Sair")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        nome = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço do produto: R$ "))
        carrinho.append((nome, preco))
        print(f"Produto {nome} adicionado ao carrinho.")
        
    elif opcao == 2:
        nome_remover = input("Informe o nome do produto a ser removido: ")
        for i, (produto, preco) in enumerate(carrinho):
            if produto.lower() == nome_remover.lower():
                carrinho.pop(i)
                print(f"Produto {nome_remover} removido do carrinho.")
                break
        else:
            print("Produto não encontrado no carrinho.")
    
    elif opcao == 3:
        if not carrinho:
            print("O carrinho está vazio.")
        else:
            print("Carrinho de compras:")
            for produto, preco in carrinho:
                print(f"- {produto}: R$ {preco:.2f}")
    
    elif opcao == 4:
        total = sum(preco for _, preco in carrinho)
        print(f"Total da compra: R$ {total:.2f}")
    
    elif opcao == 5:
        print("Saindo... Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        
        
        -----------------------------------------------------------
        
        
saldo = 1000.00  # Saldo inicial

dados = {

'senha': 123,
'conta':0,
'ag':0

}

print('Insira o cartão:')
senha = int(input('Digite sua senha '))

while senha == dados['senha'] and dados['conta']==0 and dados["ag"] == 0:

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = int(input("Digite o número da opção desejada: "))
        
        if opcao == 1:
            print(f"Saldo atual: R$ {saldo:.2f}")
            
        elif opcao == 2:
            deposito = float(input("Informe o valor a ser depositado: R$ "))
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
            
        elif opcao == 3:
            saque = float(input("Informe o valor a ser sacado: R$ "))
            if saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= saque
                print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        
        elif opcao == 4:
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

input('Digite enter para sair')    
        
        
        