import modelo

def processar_cadastro(nome, p_txt, q_txt):
    
    if nome.strip() == "" or p_txt.strip() == "" or q_txt.strip() == "":
        return False, "CAMPOS VAZIOS!"
    
    try:
        preco = float(p_txt)
        quantidade = int(q_txt)
    except ValueError:
        return False, "Erro nos números!" 
    
    sucesso = modelo.inserir_produto(nome, preco, quantidade)
    if sucesso:
        return True, "Produto cadastrado com sucesso!"
    else:
        return False, "Erro ao salvar no banco de dados."

def obter_estoque():
    
    return modelo.buscar_produto()

def processar_atualizacao(id_txt, preco_txt):
    if id_txt.strip() == "" or preco_txt.strip() == "":
        return False, "CAMPOS VAZIOS!"
        
    try:
        id_produto = int(id_txt)
        novo_preco = float(preco_txt)
    except ValueError:
        return False, "O ID precisa ser inteiro e o Preço um número!"

    sucesso = modelo.atualizar_preco(id_produto, novo_preco)
    if sucesso:
        return True, "Preço atualizado com sucesso!"
    else:
        return False, "Produto não localizado!"

def processar_delecao(id_txt):
    if id_txt.strip() == "":
        return False, "Digite o ID do produto!"
        
    try:
        id_produto = int(id_txt)
    except ValueError:
        return False, "O ID precisa ser um número inteiro."

    sucesso = modelo.deletar_produto(id_produto)
    if sucesso:
        return True, "Produto removido do estoque."
    else:
        return False, "Produto não localizado!"