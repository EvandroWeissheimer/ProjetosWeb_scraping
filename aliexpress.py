# Importa bibliotecas necessárias
import time  # Biblioteca para manipulação de tempo
from bs4 import BeautifulSoup  # Biblioteca para fazer scraping HTML
from selenium import webdriver  # Biblioteca para automação de navegador
from selenium.webdriver.common.keys import Keys  # Classe para simular pressionar teclas
from selenium.webdriver.common.by import By  # Classe para seleção de elementos
from selenium.webdriver.support.ui import WebDriverWait  # Classe para aguardar condições específicas
from selenium.webdriver.support import expected_conditions as EC  # Módulo para definir condições de espera
from selenium.common.exceptions import TimeoutException  # Exceção para timeout
import re  # Módulo para expressões regulares
import database.operations as op

import graphic_screen as tg

from telegram import Bot
import asyncio





def get_data():
    # Função para extrair dados de uma página
    def extrair_dados_pagina(url, contador):
        # Abre a URL no navegador controlado pelo Selenium
        driver.get(url)
        # Aguarda até que o elemento com a classe 'list--gallery--C2f2tvm' esteja presente
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'list--gallery--C2f2tvm')))
        except TimeoutException:
            print("TimeoutException: Elemento 'list--gallery--C2f2tvm' não encontrado na página.")
            return contador

        # Rola até o final da página (simula pressionar a tecla END)
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(5):  # Rola 5 vezes (ajuste conforme necessário)
            body.send_keys(Keys.END)
            time.sleep(0.5)  # Aguarda um segundo entre rolagens (ajuste conforme necessário)

        # Obtém o HTML da página
        page_source = driver.page_source
        site = BeautifulSoup(page_source, 'html.parser')

        # Encontra todos os produtos na página usando a classe específica
        produtos = site.find_all('div', class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')

        # Processa os produtos
        for i, produto in enumerate(produtos, start=1):
            # Extrai informações do produto
            link = produto.find('a', class_='multi--container--1UZxxHY cards--card--3PJxwBm search-card-item')
            titulo = produto.find('h1', class_='multi--titleText--nXeOvyr')
            valor = produto.find('div', class_='multi--price-sale--U-S0jtj')

            # Extrai dados e imprime
            link = link['href']
            print(f' Link do produto:', link)

            titulo = titulo.text
            print(f'Título do produto:', titulo)

            valor = valor.text.strip()  # Remove espaços em branco extras
            print(f'Preço do produto: R$ {valor}')

            # Extrai o ID do produto da URL usando expressão regular
            id = re.search(r'/(\d+).html', link)
            if id:
                id = id.group(1)
                print(f'ID do produto:', id)
            else:
                print('ID do produto não encontrado na URL.')

            # Imprime o contador
            print('Contador:', contador)
            print('\n\n')

            valor_antigo = op.add_element(id, valor)
            print("\n\nMUDANÇA DE VALOR",titulo, valor_antigo, "-->", valor)

            contador += 1

        return contador

    # Configuração do Selenium em modo headless
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Executar em modo headless (sem interface gráfica)
    driver = webdriver.Chrome(options=chrome_options)

    # Inicializa o contador global
    contador = 1

    # URL base do ali
    url_base = 'https://pt.aliexpress.com/w/wholesale-.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7'

    # produto_nome = 'placa de video' # produto pra busca
    produto_nome = tg.mercadoLivre() # produto pra busca
    produto_nome = produto_nome.replace(" ", "-")

    # url da primeira página
    url_primeira_pagina = f'https://pt.aliexpress.com/w/wholesale-{produto_nome}.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7'
    contador = extrair_dados_pagina(url_primeira_pagina, contador)


    for pagina in range(10, 61, 10): # coleta dados das páginas subsequentes (de 10 em 10 até 60)
        url_pagina = f'https://pt.aliexpress.com/w/wholesale-{produto_nome}-8g/{pagina}.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7'
        contador = extrair_dados_pagina(url_pagina, contador)

        asyncio.run(send_message_to_telegram(str(produto_nome) + '\n' + url_pagina))

    # Fechar o navegador controlado pelo Selenium
    driver.quit()

async def send_message_to_telegram(text):
    bot = Bot(token='6930586463:AAHIykB3XYJzAIAclpWA9RKVRMg0IcNXOSk')
    await bot.send_message(chat_id='-1002114023473', text=text)

if __name__ == "__main__":
    get_data()