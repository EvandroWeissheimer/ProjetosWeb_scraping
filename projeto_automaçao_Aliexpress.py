import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver

# URL base do AliExpress
url_base = 'https://pt.aliexpress.com/w/wholesale-.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7'

produto_nome = "mause gamer"  # Nome do produto a ser pesquisado

# Configuração do Selenium
driver = webdriver.Chrome()

# Faz uma requisição HTTP para obter a página HTML
base_url = "https://pt.aliexpress.com/w/wholesale-{}-8g.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7"
url = base_url.format(produto_nome)

# Abre a página no navegador controlado pelo Selenium
driver.get(url)
time.sleep(0.3)  # Aguarda um tempo para o carregamento inicial

# Número de rolagens desejadas
num_rolagens = 16  # Ajuste conforme necessário

# Rolar a página gradualmente
for _ in range(num_rolagens):
    driver.execute_script("window.scrollBy(0, 500);")  # Rola a página para baixo em incrementos de 500 pixels
    time.sleep(0.3)  # Aguarda um tempo entre as rolagens para dar tempo de carregar

# Obtém o HTML da página atualizada após as rolagens
page_source = driver.page_source

# Cria um objeto BeautifulSoup para analisar o HTML
site = BeautifulSoup(page_source, 'html.parser')

# Encontra todos os produtos na página usando a classe específica
produtos = site.find_all('div', class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')

# Inicializa um contador
i = 0

# Itera sobre cada produto encontrado
for produto in produtos:
    # Incrementa o contador
    i += 1

    # Extrai informações do produto
    link = produto.find('a', class_='multi--container--1UZxxHY cards--card--3PJxwBm search-card-item')
    titulo = produto.find('h1', class_='multi--titleText--nXeOvyr')
    valor = produto.find('div', class_='multi--price-sale--U-S0jtj')

    # Imprime informações do produto
    link = link['href']
    print('Link do produto:', link)

    titulo = titulo.text
    print('Título do produto:', titulo)

    valor = valor.text
    print('Preço do produto: R$', valor)

    # Extrai o ID do produto da URL usando expressão regular
    id = re.search(r'/(\d+).html', link)

    # Verificar se o ID foi encontrado
    if id:
        id = id.group(1)
        print('ID do produto:', id)
    else:
        print('ID do produto não encontrado na URL.')

    print('Contador para quantidade de produtos encontrados:', i)
    print('\n\n')

# Fechar o navegador controlado pelo Selenium
driver.quit()
