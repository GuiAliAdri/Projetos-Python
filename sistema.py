import sqlite3 as sq
from time import sleep
import pandas as pd

def menu():
    print('-------------------')
    print('[1] Cadastrar')
    print('[2] Ver Cadastros')
    print('[3] Sair')
    print('-------------------')
    
#variaveis
nome = ''
email = ''
opc = ''
select_all = ''
s_all = ''

#criando banco e adicionando o cursor
bc = sq.connect('banco.db')
cursor = bc.cursor()

#função que cria a tabela
def tabela():
    table = '''
    CREATE TABLE IF NOT EXISTS cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT
    );
    '''

    try:
        cursor.execute(table)
        bc.commit()
        print('Tabela Criada com sucesso')
    except:
        print('Nao foi possivel criar a tabela')

#Adicionando usuario a tabela
def add_user():
    inserir_user = '''
    INSERT INTO cadastro (nome, email)
    VALUES (?, ?);
    '''
    data = (nome, email)
    cursor.execute(inserir_user, data)
    bc.commit()
    print('Dados adicionado com sucesso')

#Mostrando os usuarios com o Pandas
def show_users():
    select_all = "SELECT * FROM cadastro;"
    df = pd.read_sql_query(select_all, bc)

    print('Mostrando todos os usuarios')
    sleep(1)
    print(df)
    sleep(1)


#chamando função para criar tabela, caso nao exista
tabela()

#main
while True:
    menu()
    opc = str(input('Digite sua opção: '))
    if opc == '1':
        nome = str(input('Digite o nome a ser cadastrado: '))
        email = str(input('Digite o email: '))
        add_user()
    elif opc == '2':
        show_users()
        continue
    elif opc == '3':
        break

#fechando a conexao com o banco
bc.close()