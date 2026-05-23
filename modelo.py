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
            preco FLOAT,
            quantidade INTEGER
            
           )
                   
        """)
    conexao.commit()
    conexao.close()

def inserir_produto(nome, preco, quantidade):
    try:
        produto = input("Digite o nome do produto: ").strip()
        preco = input("Digite o preço do produto : ").strip()
        quantidade = input(int("Digite o preço do produto : "))

        if not produto or not preco and not preco :
            print("❌ ERRO: Campos não podem ficar em branco .")

        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO produtos (nome, quantidade , preco) VALUES (?, ?, ?)"

        cursor.execute(sql, (nome, preco, quantidade))

        conexao.commit()
        conexao.close()

        if cursor.rowcount == 0:
            print("Produto não foi adicionado no estoque !")
        
        else:
            print("Produto adicionado com sucesso ao estoque !")

    except sqlite3.Error as erro:
        print(f"ERRO : {erro}")

    finally:
        if conexao:
            conexao.close()

def buscar_produto():
    try:
        print(" ---- LISTA DE PRODUTOS EM ESTOQUE ---- ")
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtos ")
        resultados = cursor.fetchall()

        if len(resultados) ==0:
            print("Não há produtos cadastrados .")
            
        else:
            for produto in produto :
                print(f"ID : {produto[0]} | Produto: {produto[1]} | Preço : R$ {produto[2]} | Quantidade : {produto[3]}")

    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")

    finally:
        if conexao:
            conexao.close()
            
if __name__ == "__main__":
    buscar_produto()
