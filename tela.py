# tela.py
import customtkinter as ctk # 
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from controlador import processar_cadastro
from modelo import buscar_produto 

janela = ctk.CTk()
janela.geometry("500x700")
janela.title("Sistema Simples")


lbl_titulo = ctk.CTkLabel(janela, text="Cadastrar Produto")
lbl_titulo.pack(pady=10)

caixa_nome = ctk.CTkEntry(janela, placeholder_text="Nome do produto")
caixa_nome.pack(pady=5)

caixa_preco = ctk.CTkEntry(janela, placeholder_text="Preço")
caixa_preco.pack(pady=5)

caixa_quantidade = ctk.CTkEntry(janela, placeholder_text="Quantidade")
caixa_quantidade.pack(pady=5)

def salvar_dados():
    n_dig = caixa_nome.get()
    p_dig = caixa_preco.get()
    q_dig = caixa_quantidade.get()

    # Envia os dados para o Cérebro validar [cite: 61]
    sucesso, mensagem = processar_cadastro(n_dig, p_dig, q_dig)

    if sucesso:
        messagebox.showinfo("Aviso", mensagem) # [cite: 62]
        caixa_nome.delete(0, 'end')
        caixa_preco.delete(0, 'end')
        caixa_quantidade.delete(0, 'end')
    else:
        messagebox.showerror("Aviso", mensagem)

btn_salvar = ctk.CTkButton(janela, text="Gravar Produto", command=salvar_dados)
btn_salvar.pack(pady=10)

caixa_lista = ctk.CTkTextbox(janela, width=300, height=100)
caixa_lista.pack(pady=10)

def atualizar_listagem():
    caixa_lista.delete("1.0", "end")
    try:
        resultados = buscar_produto() 
        if resultados:
            for p in resultados:
                caixa_lista.insert("end", f"ID: {p[0]} | Nome: {p[1]} | R$: {p[2]} | Qtd: {p[3]}\n")
    except Exception as e:
        print("Erro na lista:", e)

btn_atualizar = ctk.CTkButton(janela, text="Atualizar Lista", command=atualizar_listagem)
btn_atualizar.pack(pady=5)

def gerar_grafico():
    try:
        resultados = buscar_produto()
        if not resultados:
            return
        
        nomes = []
        quantidades = []
        for p in resultados:
            nomes.append(p[1])       
            quantidades.append(p[3]) 

        fig, ax = plt.subplots(figsize=(4, 2))
        ax.bar(nomes, quantidades)
        
        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

    except Exception as e:
        print("Erro no gráfico:", e)

btn_grafico = ctk.CTkButton(janela, text="Gerar Gráfico", command=gerar_grafico)
btn_grafico.pack(pady=5)

janela.mainloop()