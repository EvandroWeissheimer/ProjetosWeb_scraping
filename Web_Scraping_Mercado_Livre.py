import requests
from bs4 import BeautifulSoup

# Melhorias pelo oq eu testei so mostra a primeira pagina com os produtos tem que tentar fazer um jeito de passar as paginas

# URL base do Mercado Livre

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = "rtx 4090"  # Nome do produto a ser pesquisado

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

