# main.py
from tela import janela
from modelo import criar_tabela

if __name__ == "__main__":
    # 1. Garante que a tabela exista antes de iniciar a interface
    criar_tabela()
    
    # 2. Inicia o loop principal da janela do CustomTkinter
    janela.mainloop()