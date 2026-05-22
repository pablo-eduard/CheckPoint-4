📦 Sistema de Gestão de Inventário (ERP) - Checkpoint 4
Este projeto consiste em um sistema desktop de gestão de inventário (ERP), desenvolvido com o objetivo de integrar interface gráfica, banco de dados e lógica de negócios seguindo o padrão de arquitetura MVC (Model-View-Controller).

🛠️ Tecnologias Utilizadas
Linguagem: Python

Interface Gráfica: CustomTkinter

Banco de Dados: SQLite3

Visualização de Dados: Matplotlib (Dashboard de estoque)

📋 Funcionalidades (CRUD)
O sistema permite a gestão completa de produtos, incluindo:

Adicionar: Cadastro de novos itens com ID, nome, preço e quantidade.

Listar: Exibição visual de todos os produtos cadastrados.

Atualizar: Edição de preços e quantidades de itens existentes.

Excluir: Remoção definitiva de produtos do inventário.

Dashboard: Painel visual com gráfico de barras para análise do estoque.

🏗️ Arquitetura do Projeto
Para garantir a modularização e manutenibilidade, o código está dividido em:

main.py: Ponto de entrada que inicializa a aplicação.

modelo.py: Responsável pela comunicação direta com o banco de dados (SQLite).

controlador.py: "Cérebro" do sistema; valida entradas e gerencia a lógica entre a View e o Model.

tela.py: Camada de interface (View) construída com CustomTkinter.

🚀 Como Executar
Clone o repositório: git clone https://github.com/pablo-eduard/CheckPoint-4.git

Certifique-se de ter as bibliotecas instaladas: pip install customtkinter matplotlib

Execute o arquivo principal: python main.py, porém ainda o transformaremos em um doc .exe ou seja, executável mesmo em computadores que não houverem o programa Python instalado. 
