from modelo import inserir_produto



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

