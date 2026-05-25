import customtkinter as ctk 
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from controlador import processar_cadastro, obter_estoque, processar_delecao

janela = ctk.CTk()
janela.geometry("500x650")
janela.title("Sistema Simples")


frame_scroll = ctk.CTkScrollableFrame(janela)
frame_scroll.pack(fill="both", expand=True, padx=10, pady=10)


lbl_titulo = ctk.CTkLabel(frame_scroll, text="Cadastrar Produto")
lbl_titulo.pack(pady=10)

caixa_nome = ctk.CTkEntry(frame_scroll, placeholder_text="Nome do produto")
caixa_nome.pack(pady=5)

caixa_preco = ctk.CTkEntry(frame_scroll, placeholder_text="Preço")
caixa_preco.pack(pady=5)

caixa_quantidade = ctk.CTkEntry(frame_scroll, placeholder_text="Quantidade")
caixa_quantidade.pack(pady=5)

def salvar_dados():
    n_dig = caixa_nome.get()
    p_dig = caixa_preco.get()
    q_dig = caixa_quantidade.get()

    sucesso, mensagem = processar_cadastro(n_dig, p_dig, q_dig)

    if sucesso:
        messagebox.showinfo("Aviso", mensagem)
        caixa_nome.delete(0, 'end')
        caixa_preco.delete(0, 'end')
        caixa_quantidade.delete(0, 'end')
        atualizar_listagem() 
    else:
        messagebox.showerror("Aviso", mensagem)

btn_salvar = ctk.CTkButton(frame_scroll, text="Gravar Produto", command=salvar_dados)
btn_salvar.pack(pady=10)

caixa_lista = ctk.CTkTextbox(frame_scroll, width=300, height=100)
caixa_lista.pack(pady=10)

def atualizar_listagem():
    caixa_lista.delete("1.0", "end")
    try:
        resultados = obter_estoque() 
        if resultados:
            for p in resultados:
                caixa_lista.insert("end", f"ID: {p[0]} | Nome: {p[1]} | R$: {p[2]} | Qtd: {p[3]}\n")
    except Exception as e:
        print("Erro na lista:", e)

btn_atualizar = ctk.CTkButton(frame_scroll, text="Atualizar Lista", command=atualizar_listagem)
btn_atualizar.pack(pady=5)

lbl_deletar = ctk.CTkLabel(frame_scroll, text="Deletar Produto")
lbl_deletar.pack(pady=(15, 5))

caixa_id_delete = ctk.CTkEntry(frame_scroll, placeholder_text="Digite o ID para deletar")
caixa_id_delete.pack(pady=5)

def deletar_dados():
    id_dig = caixa_id_delete.get()
    sucesso, mensagem = processar_delecao(id_dig)
    
    if sucesso:
        messagebox.showinfo("Aviso", mensagem)
        caixa_id_delete.delete(0, 'end')
        atualizar_listagem() 
    else:
        messagebox.showerror("Aviso", mensagem)

btn_deletar = ctk.CTkButton(frame_scroll, text="Deletar Produto", command=deletar_dados, fg_color="#C0392B", hover_color="#922B21")
btn_deletar.pack(pady=5)


def gerar_grafico():
    try:
        resultados = obter_estoque()
        if not resultados:
            return
        
        nomes = []
        quantidades = []
        for p in resultados:
            nomes.append(p[1])       
            quantidades.append(p[3]) 

        fig, ax = plt.subplots(figsize=(4, 2.5)) 
        ax.bar(nomes, quantidades)
        
        canvas = FigureCanvasTkAgg(fig, master=frame_scroll)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=(15, 20)) 

    except Exception as e:
        print("Erro no gráfico:", e)

btn_grafico = ctk.CTkButton(frame_scroll, text="Gerar Gráfico", command=gerar_grafico)
btn_grafico.pack(pady=10)