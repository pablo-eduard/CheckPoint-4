import sqlite3

def conectar():
    return sqlite3.connect("controle_estoque.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            produto TEXT NOT NULL,
            quantidade INTEGER,
            preco FLOAT
           )
                   
        """)
    conexao.commit()
    conexao.close()

def inserir_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO produtos (nome, quantidade , preco) VALUES (?, ?, ?)"

    cursor.execute(sql, (nome, preco, quantida))

    conexao.commit()
    conexao.close()

    pass
def buscar_produto():

    pass

def atualizar_preco(id_produto,novo_produto):

    pass

def deletar_produto(id_produto):

    pass


criar_tabela()