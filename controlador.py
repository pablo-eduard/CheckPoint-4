from modelo import sqlite3


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
            
            
def processar_cadastro(nome, p_txt, q_txt ):
    if nome == " " or p_txt == " ":
        return False, "CAMPOS VAZIOS!"
    
    try:
        preco = float (p_txt)
        quantidade = int(q_txt)
    except ValueError:
        return False, print("Erro nos número !")
    
    inserir_produto(nome, preco, quantidade )
    return True, print("Produto cadastrado com sucesso")



def atualizar_preco(id_produto,novo_produto):
    try:
        print(" --- ATUALIZAR PREÇO --- ")
        conexao = conectar()
        cursor = conexao.cursor()

        id_produto = int(input("Digite o ID do produto : "))
        novo_preco = float(input("Digite o novo preço :"))

        if not novo_preco:
            print("ERRO : Campo não pode ficar em branco !")
            return
        
        cmd_sql = "UPDATE produtos SET preco = ? WHERE id = ?"
        cursor.execute(cmd_sql, (novo_preco, id_produto))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Produto não localizado !")

        else : 
            print("Preço atualizado com sucesso ! ")

    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
    except ValueError:
        print("❌ ERRO: O ID precisa ser um número inteiro.")
    finally:
        if conexao:
            conexao.close()


def deletar_produto(id_produto):
    try:
        print(" --- EXCLUIR PRODUTO --- ")
        conexao = conectar()
        cursor = conexao.cursor()

        id_produto = int(input("Digite o ID do produto á ser excluído:"))
        cmd_sql = "DELETE FROM clientes WHERE id = ?"
        cursor.execute(cmd_sql, (id_cliente, ))
        conexao.commit()

        if cursor.rowcount == 0:
            print("❌ ERRO: produto não localizado.")
        else:
            print("✅ Produto removido do estoque .")

    except sqlite3.Error as erro:
        print(f"❌ Erro: {erro}")
    except ValueError:
        print("❌ ERRO: O ID precisa ser um número inteiro.")
    finally:
        if conexao:
            conexao.close()

