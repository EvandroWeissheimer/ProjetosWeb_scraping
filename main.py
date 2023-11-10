# Imports
import requests
from bs4 import BeautifulSoup

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk


def montaTela():
    global selected_var

    root = tk.Tk()

    root.title("Web Scraping")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (731 / 2)
    y = (screen_height / 2) - (600 / 2)

    root.geometry('%dx%d+%d+%d' % (731, 600, x, y))

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, font=("Arial", 14, "bold"), text="Mandar WhatsApp\n", anchor="center").grid(column=1, row=1, sticky=tk.W)
    # ttk.Label(mainframe, font=("Arial", 10),  text="Informe ás empresas separadas por vírgula ','\n").grid(column=1, row=2, sticky=tk.W)

    global produto
    produto = ttk.Entry(mainframe)
    produto.grid(column=1, row=4, sticky=tk.EW)
    # ttk.Button(mainframe, text="Criar Contado",  command=telaCadastro).grid(column=1, row=7, sticky=tk.W)
    ttk.Button(mainframe, text="Merca Livre", command=get_product_ml).grid(column=1, row=5, sticky=tk.W)
    # ttk.Button(mainframe, text="Aliexpress",  command=enviarMensagem).grid(column=1, row=6, sticky=tk.W)
    ttk.Button(mainframe, text="Sair", command=root.destroy).grid(column=1, row=7, sticky=tk.W)

    root.mainloop()


def mercadoLivre():
    teste = produto.get()
    return teste

def get_product_ml():
    # Melhorias pelo oq eu testei so mostra a primeira pagina com os produtos tem que tentar fazer um jeito de passar as paginas
    url_base = 'https://lista.mercadolivre.com.br/'

    produto_nome = mercadoLivre() # Nome do produto a ser pesquisado

    # Faz uma requisição HTTP para obter a página HTML
    response = requests.get(url_base + produto_nome) # https://lista.mercadolivre.com.br/ + o produto
    print('\nURL da Busca ', url_base + produto_nome, '\n')

    # Cria um objeto BeautifulSoup para analisar o HTML
    site = BeautifulSoup(response.text, 'html.parser')

    # Encontra todos os produtos na página usando a classe específica
    produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'})

    # Inicializa um contador
    i = 0

    # Itera sobre cada produto encontrado
    for produto in produtos:
        # Incrementa o contador
        i += 1
        
        # Encontra e imprime o título do produto
        titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
        print('Título do produto:', titulo.text)

        # Encontra e imprime o id do produto
        id = produto.find('section', attrs={'class': 'andes-carousel-snapped__container andes-carousel-snapped__container--full andes-carousel-snapped__container--with-controls'})
        print('Id do produto:', id.get('id'))
        
        # Encontra e imprime o link do produto
        link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})
        print('Link do produto:', link['href'])
        
        # Encontra e imprime o preço do produto (considerando centavos)
        centavos = produto.find('span', attrs={'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})
        print('Preço do produto: R$', centavos.text)

        # Imprime o contador
        print('Contador para quantidade de produtos encontrados:', i)
        
        # Adiciona linhas em branco para melhorar a legibilidade
        print('\n\n')



montaTela()