import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Criando o banco
conexao = sqlite3.connect('meu_banco.bd')

# Posso introduzir o sql no código 
cursor = conexao.cursor()

# Criar tabela
cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS clientes(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT Not null,
          idade integer not null,
          email TEXT not null,
          cidade TEXT not null          
    )
''')

# Inserir os dados
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade) VALUES ('Maria', 30, 'maria@gmail.com','SÃO PAULO')")
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade) VALUES ('Lucas', 25, 'lucas@gmail.com', 'SÃO CARLOS')")
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade) VALUES ('Carlos', 19, 'carlos@gmail.com','GUARULHOS')")
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade) VALUES ('CarlA', 35, 'carla@gmail.com','BELO HORIZONTE')")
conexao.commit()

cursor.execute('SELECT * FROM clientes')

# Listas para armazenar os dados
LISTA_cidade = []
LISTA_idade = []
LISTA_nomes = []
lista_email = []
lista_id = []
for dados in cursor.fetchall():
    lista_id.append(dados[0])  # ID
    LISTA_nomes.append(dados[1])  # Nome
    LISTA_idade.append(dados[2])  # Idade
    lista_email.append(dados[3])  # Email
    LISTA_cidade.append(dados[4])  # Cidade

# Criando o DataFrame
data = {
    'id': lista_id,
    'nome': LISTA_nomes,
    'idade': LISTA_idade,
    'cidade': LISTA_cidade,
    'email': lista_email
}

df = pd.DataFrame(data)

# Salvar os dados em um arquivo CSV
df.to_csv('dados_do_banco.csv', index=False)

# Calcular a média de idades por cidade
media = df.groupby('cidade')['idade'].mean()

# Mostrar a média
print(media)

# Fechar o cursor
cursor.close()

# Gráfico de pizza com a média de idades por cidade
plt.figure(figsize=(10, 6))
plt.pie(media, labels=media.index, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow'])
plt.title("Distribuição da Média de Idades por Cidade")
plt.show()

# Gráfico de barras: Idade por Cidade
plt.figure(figsize=(10, 6))
plt.bar(media.index, media)
plt.xlabel('Cidade')
plt.ylabel('Média de Idade')
plt.title('Média de Idade por Cidade')
plt.show()
