# Imports
import pandas as pd

def add_element(product_name, price):
    product_name = str(product_name) # Defines like String
    price = str(price) # Defines like Int

    df = pd.read_csv('database\db.csv') # Read The Dataset
    df1 = pd.DataFrame() # Create the Dataframe
    df2 = pd.DataFrame({'prices': [price], "id": [product_name]}) # Create the second dataframe
    
    j = 0

    for e in df["id"]:
        if str(e) != str(product_name):
            df1 = pd.concat([df2, df], ignore_index=True) # Concatenate the Data
        else:
            if df["prices"][j] == price:
                ret_text = "None"
                df1 = df.copy()
                return ret_text
            else:
                ret_text = df["prices"][j]
                df.at[j, 'prices'] = price
                df.to_csv(r"database\db.csv", index=False) # Save Data in File
                return ret_text
        j = j + 1
    
    df1.to_csv(r"database\db.csv", index=False) # Save Data in File

if __name__ == "__main__":
    print(add_element("Notebook Vaio Fe15 I7 Linux Debian 10 8gb 512gb Ssd Cor Deep Gray", "R$3.01"))