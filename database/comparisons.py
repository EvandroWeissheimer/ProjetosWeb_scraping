# Imports
try:
    import operations as op
except ModuleNotFoundError:
    import database.operations as op

def prices(id, current_price):
    changes_happend = False

    last_price = op.check_element_price(id)

    last_price = float(last_price)
    current_price = float(current_price)

    if last_price == None:
        print("Não Existe Nenhum Produto com esse ID")
    else:
        if current_price == last_price:
            changes_happend = False
        else:
            changes_happend = True

    return changes_happend, last_price

if __name__ == "__main__":
    print(prices(1, 20.1))