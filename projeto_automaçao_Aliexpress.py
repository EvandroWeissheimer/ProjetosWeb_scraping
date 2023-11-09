import requests
from bs4 import BeautifulSoup

# Melhorias pelo oq eu testei so mostra a primeira pagina com os produtos tem que tentar fazer um jeito de passar as paginas

# URL base do Mercado Livre

url_base = 'https://pt.aliexpress.com/w/wholesale-.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7'

produto_nome = "rx 580 8g elsa"  # Nome do produto a ser pesquisado

# Faz uma requisição HTTP para obter a página HTML
base_url = "https://pt.aliexpress.com/w/wholesale-{}-8g.html?spm=a2g0o.home.auto_suggest.2.53451c912VxIl7"
url = base_url.format(produto_nome)
response = requests.get(url)
print('\nURL da Busca ', url, '\n')

# Cria um objeto BeautifulSoup para analisar o HTML
site = BeautifulSoup(response.text, 'html.parser')

# Encontra todos os produtos na página usando a classe específica
produtos = site.findAll('div', attrs={'class': 'list--galleryWrapper--29HRJT4'})

print(site.text)

valor = site.find('span', attrs={'class': 'a2g0o.productlist.main.i2.52945fe7XFQBdO'})
print('Preço do produto: R$', valor.text)

# # Inicializa um contador
i = 0

# Itera sobre cada produto encontrado
# for produto in produtos:
#     # Incrementa o contador
#     i += 1
    
#     # # Encontra e imprime o título do produto
#     # titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
#     # print('Título do produto:', titulo.text)

#     # # Encontra e imprime o id do produto
#     # id = site.find('section', attrs={'class': '_blank'})
#     # print('Id do produto:', id.get('id'))
    
#      # Encontra e imprime o link do produto
#     link = site.find('a', attrs={'class': 'multi--container--1UZxxHY cards--card--3PJxwBm search-card-item'})
#     print('Link do produto:', link['href'])
    
#      Encontra e imprime o preço do produto (considerando centavos)
#     valor = produto.find('span', attrs={'class': 'a2g0o.productlist.main.i2.52945fe7XFQBdO'})
#     print('Preço do produto: R$', valor.text)

#     # Imprime o contador
#     print('Contador para quantidade de produtos encontrados:', i)
    
#     # Adiciona linhas em branco para melhorar a legibilidade
#     print('\n\n')


