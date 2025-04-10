# 1 - Crie um sistema de banco, com as seguintes operações:

# # SISTEMA DE BANCO 

# - Acesso a conta
# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 
# - Ao finalizar seu sistema adicione:






dados = {'login':[], 'senha':[]}


for n in range(1,2):# cadastramento de usuário
    login = input('usuario:')
    senha = input('senha:')

    dados['login'].append(login)
    dados['senha'].append(senha)

print('Extrato de Usuários com acesso')
print(dados)
print('''----------------------------
      ''')


# acesso aconta


l = [1, 2]
for i in l:
    login_usuario = input('Digite o login: ')
    senha = input('Digite a senha: ')

    
    if login_usuario in dados['login']:
        index_usuario = dados['login'].index(login_usuario)  
        if dados['senha'][index_usuario] == senha:
            print('Seja bem-vindo à Conta Master!')
            break  
        else:
            print("Senha incorreta! - 2 tentativas ")
    else:
        print("Login incorreto!")

opcoes =['1 - Deposito','2 - Saque','3 -Extrato''4 - Sair'] 
print(opcoes)

#banco = [1,2,3,4]
deposito = []
saque = []

opcao = int(input('Escolha uma opção (1, 2, 3 ou 4): '))

  
if opcao == 1:
    deposito = float(input('Qual valor do seu depósito: '))
elif opcao == 2:
    saque = float(input('Qual valor do saque: '))
    
elif opcao == 3:
    print(f'Seu extrato: Depósito = {deposito}, Saque = {saque}')
elif opcao == 4:
    print('Obrigado pela confiança em nosso banco!')
else:
    print('Opção inválida. Tente novamente.')


print('''-------------
      ''')




