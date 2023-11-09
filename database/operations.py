# Imports
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=database\db.accdb;') # Establish a connection
cursor = conn.cursor() # Create a cursor object

def add_element(product_name, id, price):
    data = (product_name, price, id)
    sql = f"INSERT INTO Products(product_name, prices, id) VALUES(?, ?, ?)"

    cursor.execute(sql, data) # Execute the query
    conn.commit() # Commit the transaction
    
def check_element_price(id):
    sql = f"SELECT prices FROM Products WHERE id = ?"
    cursor.execute(sql, (id)) # Execute the query

    row = cursor.fetchone() # Fetch one record

    if row is not None:
        return row.prices
    else:
        return None


if __name__ == "__main__":
    check_element_price(2)