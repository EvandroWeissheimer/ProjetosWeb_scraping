# Imports
import requests
from bs4 import BeautifulSoup
import database.operations as op  # As informações do produto são enviadas para a função op.add_element() no módulo database.operations.

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk

import graphic_screen as tg
import time

# from graphic_screen import mercadoLivre

def get_product_ml(): #  faz web scraping no Mercado Livre.

    # Melhorias pelo oq eu testei so mostra a primeira pagina com os produtos tem que tentar fazer um jeito de passar as paginas
    url_base = 'https://lista.mercadolivre.com.br/'

    produto_nome = tg.Saida_Graphic() # Nome do produto a ser pesquisado

    # Faz uma requisição HTTP para obter a página HTML
    response = requests.get(url_base+produto_nome) # https://lista.mercadolivre.com.br/ + o produto
    print('\nURL da Busca ', url_base+produto_nome, '\n')

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
        titulo_text = titulo.text if titulo else None
        print('Título do produto:', titulo_text)

        # Encontra e imprime o id do produto
        id = produto.find('section', attrs={'class': 'andes-carousel-snapped__container andes-carousel-snapped__container--full andes-carousel-snapped__container--with-controls'})
        id_text = id.get('id') if id else None
        print('Id do produto:', id_text)
        
        # Encontra e imprime o link do produto
        link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})
        link_href = link['href'] if link else None
        print('Link do produto:', link_href)
        
        # Encontra e imprime o preço do produto (considerando centavos)
        valor = produto.find('span', attrs={'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})
        valor_text = valor.text if valor else None
        print('Preço do produto: R$', valor_text)

        if titulo_text and valor_text and id_text and link_href:
            op.add_element(titulo_text, valor_text, titulo_text, link_href)
        else:
            print("Alguns valores são nulos ou vazios. Não chamando op.add_element.")

        # Imprime o contador
        print('Contador para quantidade de produtos encontrados:', i)
        
        # Adiciona linhas em branco para melhorar a legibilidade
        print('\n\n')
        # send_message_to_telegram(str(produto))
        #asyncio.run(send_message_to_telegram(titulo.text + '\n'  + str(link['href'] + '\n' + centavos.text))) # Mensagens sobre o produto também são enviadas ao Telegram usando 

        # ajeitar saida Mensagens sobre o produto também são enviadas ao Telegram usando send_message_to_telegram().

if __name__ == "__main__":
    tg.montaTela()
    