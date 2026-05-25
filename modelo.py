import sqlite3

def conectar():
    return sqlite3.connect("controle_estoque.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco FLOAT,
            quantidade INTEGER
        )
    """)  
    conexao.commit()
    conexao.close()

def inserir_produto(nome, preco, quantidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)"
        cursor.execute(sql, (nome, preco, quantidade))

        conexao.commit()
        conexao.close()
        return True
    except sqlite3.Error as erro:
        print(f"ERRO: {erro}")
        return False

def buscar_produto():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()
        conexao.close()
        return resultados 
    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
        return []

def atualizar_preco(id_produto, novo_preco):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cmd_sql = "UPDATE produtos SET preco = ? WHERE id = ?"
        cursor.execute(cmd_sql, (novo_preco, id_produto))
        conexao.commit()
        
        linhas_afetadas = cursor.rowcount
        conexao.close()
        return linhas_afetadas > 0
    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
        return False

def deletar_produto(id_produto):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cmd_sql = "DELETE FROM produtos WHERE id = ?"
        cursor.execute(cmd_sql, (id_produto,))
        conexao.commit()

        linhas_afetadas = cursor.rowcount
        conexao.close()
        return linhas_afetadas > 0
    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
        return False