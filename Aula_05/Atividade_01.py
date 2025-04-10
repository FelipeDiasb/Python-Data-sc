# enquanto 
# for finito X infinito


acesso = input('Deseja acessar?')
carrinho =  []
while acesso == 'sim':
    print('Olá ')
    lista = [1,2,3,4,5,6]
    
    print('escolha um valor')
    v =  int(input('>>'))
    carrinho.append(lista[v])
    print(carrinho)
    acesso = input('Deseja continuar?')
else:
    print('Obrigada volte sempre')    