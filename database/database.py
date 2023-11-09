# Imports
import pyodbc

def add_element(product_name, id, price):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=database\db.accdb;') # Establish a connection
    cursor = conn.cursor() # Create a cursor object

    data = (product_name, price, id)
    sql = f"INSERT INTO Products(product_name, prices, id) VALUES(?, ?, ?)"

    cursor.execute(sql, data) # Execute the query
    conn.commit() # Commit the transaction
    conn.close() # Close the connection

if __name__ == "__main__":
    add_element("test", 1, 20.2)