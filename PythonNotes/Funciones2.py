def calculate_price(cost, profit_rate):
    price = cost/ (1- profit_rate)
    return price


products = []

def create_product(price):

    product = []

    product_id = input("Id product")
    product.append(product_id)
    product_name = input("Nombre producto")
    product.append(product_name)
    brand = input("Marca")
    product.append(brand)
    description = input("Descripcion")
    product.append(description)
    product_price = price
    product.append(price)
    
    products.append(product)

 
#create_product(price)

#print(product)


def print_products():
    for product in products:
        print(product)



def menuApp():
    opc = int(input(f"1. registrar producto\n 2. listar productos"))

    match opc:
        case 1:
            print("1. Registrar")
            cost = float(input("Costo"))
            profit_rate = float(input("Margen de ganancia "))
            price = calculate_price(cost, profit_rate)
            create_product(price)
        case 2:
            print("2.Listar productos")
            print_products()
        case 3:
            init = 0    

        case _:
            print("Seleccione una opcion valida")




def app():
    init = int(input("Presione 1 para iniciar")) 

    while init != 0:
        menuApp()

app()        

