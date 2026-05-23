import customtkinter as ctk
from controlador import conectar, salvar_dados, processar_cadastro

janela = ctk.CTk()

janela.geometry("1280x720")
janela.title("Controle de Estoque")



lbl_titulo = ctk.CTkLabel ( janela, text= "Adicionar novo produto : ")
lbl_titulo.pack(pady= 10)

caixa_nome = ctk.CTkEntry (janela, placeholder_text = "Nome do produto")
caixa_nome.pack(pady=10)

caixa_quantidade = ctk.CTkEntry (janela, placeholder_text = "Quantidade do produto : ")
caixa_quantidade.pack(pady=10)

caixa_preco = ctk.CTkEntry (janela, placeholder_text = "Preço do produto : ")
caixa_preco.pack(pady=10)

def salvar_dados():
    n_dig = caixa_nome.get()
    q_dig = caixa_quantidade.get()
    p_dig = caixa_preco.get()

    sucesso, mensagem = processar_cadastro(n_dig, p_dig, q_dig)

    if sucesso :
        lbl_mensagem.configure(text=mensagem, text_color="green")
    
    else:
        lbl_mensagem.configure(text=mensagem, text_color="red")

btn_salvar = ctk.CTkButton(janela, text= "Salvar",command=salvar_dados)
btn_salvar.pack(pady=20)

lbl_mensagem = ctk.CTkLabel(janela, text="")
lbl_mensagem.pack()