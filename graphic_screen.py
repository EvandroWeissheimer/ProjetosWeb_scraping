# Importando os módulos necessários da biblioteca tkinter
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk

# Importando funções de módulos externos (mercado_livre e aliexpress)
from mercado_livre import get_product_ml
from aliexpress import get_data

# Função para criar e configurar a interface gráfica (GUI)
def montaTela():
    global selected_var

    # Criando a janela principal do Tkinter
    root = tk.Tk()

    # Configurando o título da janela
    root.title("Web Scraping")

    # Obtendo a largura e altura da tela para posicionar a janela no centro
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculando as coordenadas x e y para centralizar a janela
    x = (screen_width / 2) - (731 / 2)
    y = (screen_height / 2) - (600 / 2)

    # Configurando a geometria da janela
    root.geometry('%dx%d+%d+%d' % (731, 600, x, y))

    # Configurando a cor de fundo
    root.configure(bg='black')

    # Criando um frame principal dentro da janela
    mainframe = ttk.Frame(root, padding="300 200 200 200")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    # Configurando pesos para redimensionamento
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Criando um rótulo para a GUI
    ttk.Label(mainframe, font=("Arial", 14, "bold"), text="Web Scraping\n", anchor="center").grid(column=1, row=1, sticky=tk.W)

    # Criando um widget de entrada para inserir informações do produto
    global produto
    produto = ttk.Entry(mainframe)
    produto.grid(column=1, row=4, sticky=tk.EW)

    # Criando botões para diferentes ações
    ttk.Button(mainframe, text="Merca Livre", command=get_product_ml).grid(column=1, row=5, sticky=tk.W) #obtém dados do Mercado Livre.
    ttk.Button(mainframe, text="Aliexpress",  command=get_data).grid(column=1, row=6, sticky=tk.W) # obtém dados do Mercado Livre.
    ttk.Button(mainframe, text="Sair", command=root.destroy).grid(column=1, row=7, sticky=tk.W)
    # Executando o loop principal do Tkinter
    root.mainloop()

# Função para obter informações do produto do Mercado Livre

def Saida_Graphic():
    # Obtendo a entrada do widget de entrada
    teste = produto.get() # entrada de dados
    return teste
