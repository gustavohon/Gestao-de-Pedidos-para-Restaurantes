#Made by Gustavo
#Sistema de gestão de pedidos para restaurantes, com interface gráfica básica
#Não se esqueça de salvar em UTF-8

import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa messagebox para exibir alertas
from datetime import datetime  # Importa datetime para obter data e hora

# Função que adiciona um novo pedido com o número da mesa, pedido e horário
def adicionar_pedido():
    mesa = entrada_mesa.get()  # Obtém o número da mesa
    pedido = entrada_pedido.get()  # Obtém o pedido

    # Verifica se ambos os campos foram preenchidos
    if mesa and pedido:
        # Obtém a data e hora atual formatada
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Adiciona o pedido à lista com data e hora
        lista_pedidos.insert(tk.END, f"Mesa {mesa}: {pedido} - {horario}")
        
        # Limpa os campos de entrada
        entrada_mesa.delete(0, tk.END)
        entrada_pedido.delete(0, tk.END)
    else:
        # Exibe uma mensagem de erro caso algum campo esteja vazio
        messagebox.showwarning("Erro", "Por favor, preencha o número da mesa e o pedido.")

# Função que marca um pedido como pronto e o remove da lista de pedidos
def pedido_pronto():
    # Verifica se algum item está selecionado na lista de pedidos
    selecionado = lista_pedidos.curselection()
    
    if selecionado:
        # Obtém o texto do pedido selecionado e remove da lista
        pedido = lista_pedidos.get(selecionado)
        lista_pedidos.delete(selecionado)
        
        # Exibe o pedido na lista de pedidos prontos com status "Pronto!"
        lista_pedidos_prontos.insert(tk.END, f"{pedido} - Pronto!")
    else:
        # Exibe uma mensagem de erro se nenhum item estiver selecionado
        messagebox.showwarning("Erro", "Selecione um pedido para marcar como pronto.")

# Configuração da janela principal da interface gráfica
janela = tk.Tk()
janela.title("Gestão de Pedidos para Restaurantes")  # Define o título da janela

# Campo para entrada do número da mesa
tk.Label(janela, text="Número da Mesa:").grid(row=0, column=0, padx=5, pady=5)
entrada_mesa = tk.Entry(janela)
entrada_mesa.grid(row=0, column=1, padx=5, pady=5)

# Campo para entrada do pedido
tk.Label(janela, text="Pedido:").grid(row=1, column=0, padx=5, pady=5)
entrada_pedido = tk.Entry(janela)
entrada_pedido.grid(row=1, column=1, padx=5, pady=5)

# Botão para adicionar o pedido à lista
botao_adicionar = tk.Button(janela, text="Adicionar Pedido", command=adicionar_pedido)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

# Lista que exibe os pedidos em espera
tk.Label(janela, text="Pedidos:").grid(row=3, column=0, padx=5, pady=5)
lista_pedidos = tk.Listbox(janela, width=50)  # Aumenta a largura para acomodar a data e hora
lista_pedidos.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botão para marcar o pedido selecionado como pronto
botao_pronto = tk.Button(janela, text="Pedido Pronto", command=pedido_pronto)
botao_pronto.grid(row=5, column=0, columnspan=2, pady=10)

# Lista que exibe os pedidos que já estão prontos
tk.Label(janela, text="Pedidos Prontos:").grid(row=6, column=0, padx=5, pady=5)
lista_pedidos_prontos = tk.Listbox(janela, width=50)  # Aumenta a largura para acomodar a data e hora
lista_pedidos_prontos.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Inicia o loop da interface gráfica
janela.mainloop()