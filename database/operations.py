# Importando a biblioteca pandas e atribuindo o alias pd
import pandas as pd
from telegram import Bot
import asyncio

async def send_message_to_telegram(text):
    bot = Bot(token='6228537252:AAHiu9l4Qq_10jXzQiT8uKa1kN4UTYFugXQ')
    await bot.send_message(chat_id='-1002001344315', text=text)

# Definindo uma função chamada add_element que recebe quatro parâmetros: product_name_id, product_price, name_geral, product_link
def add_element(product_name_id, product_price, name_geral, product_link):
    
    # Convertendo product_name para string
    product_name_id = str(product_name_id)
    
    # Convertendo price para string
    product_price = str(product_price)

    # Convertendo name_geral para string (se for None, será convertido para uma string vazia)
    name_geral = str(name_geral)

    # Lendo o arquivo CSV 'database\db.csv' e armazenando os dados em um DataFrame chamado df
    df = pd.read_csv('database\db.csv')

    # Verificando se o ID já existe no DataFrame
    if product_name_id in df['Id'].values:
        # Obtendo o preço atual no DataFrame
        current_price = df.loc[df['Id'] == product_name_id, 'Prices'].iloc[0]

        # Verificando se o preço atual é diferente do novo preço
        if current_price != product_price:
            # Calculando a diferença no preço
            diff = float(product_price.replace("R$", "").replace(",", ".")) - float(current_price.replace("R$", "").replace(",", "."))
            
            # Atualizando o preço no DataFrame
            df.loc[df['Id'] == product_name_id, 'Prices'] = product_price

            # Salvando os dados no arquivo CSV 'database\db.csv'
            df.to_csv(r"database\db.csv", index=False)

            # Imprimindo informações no console
            print(f"\nPreço atualizado para {product_price}.")
            print(f"\nNome: {name_geral}")
            print(f"\nDiferença no preço: {diff}")

            # Enviando mensagem para o Telegram apenas se houver desconto
            if diff > 0:
                message_text = f"Nome: {name_geral}\nPreço atualizado: {product_price}\nDesconto: {diff}\nLink do produto: {product_link}"
                asyncio.run(send_message_to_telegram(message_text))
        else:
            # Imprimindo informações no console para produto existente sem mudança no preço
            print(f"\nProduto existente sem mudança no preço.")
            print(f"\nNome: {name_geral}")
    else:
        # Adicionando um novo produto ao DataFrame
        new_data = {'Id': [product_name_id], 'Prices': [product_price]}
        df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)

        # Salvando os dados no arquivo CSV 'database\db.csv'
        df.to_csv(r"database\db.csv", index=False)

        # Imprimindo informações no console para novo produto
        print(f"\nNovo produto adicionado.")
        print(f"\nNome: {name_geral}")

        # Enviando mensagem para o Telegram
        message_text = f"Novo Produto ;)\nNome: {name_geral}\nPreço:  {product_price}\nLink do produto: {product_link}"
        asyncio.run(send_message_to_telegram(message_text))

# Verificando se o script está sendo executado como o programa principal
if __name__ == "__main__":
    # Chamando a função add_element com argumentos específicos e imprimindo o resultado
    result = add_element("1005006202269562", "R$517,35", "Processador gamer Intel Core i5-2400 CM8062300834106 de 4 núcleos e 3.4GHz de frequência com gráfica integrada", "link_do_produto")

    # Verificando se o resultado indica que o produto foi adicionado ou atualizado
    if "Novo produto adicionado" in result or "Preço atualizado para" in result:
        # Produto adicionado ou atualizado com sucesso, pode enviar a mensagem para o Telegram
        asyncio.run(send_message_to_telegram(result))
