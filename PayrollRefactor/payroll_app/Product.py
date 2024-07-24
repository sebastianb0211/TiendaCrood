from Category import Category

class Product:

    product_id = None
    product_name = None
    price = None
    quantity = None
    description = None
    category = None

    def __init__(self, product_id, product_name, price , quantity , description, category):
        self._product_id = product_id
        self._product_name = product_name
        self._price = price
        self._quantity = quantity
        self._description = description
        self._category = category


    #Getters and Setters

    #Methods

    products= {}

    def create_product(self, category):
        self._product_id = int(input("Id producto"))
        self._product_name = input("Nombre producto")
        self._price = float(input("Precio"))
        self._quantity = int(input("Cantidad"))
        self._description =  input("Descripción")
        self._category  = self.find_category(category)
        self.products[self._product_id] = {"Id": self._product_id, "Nombre": self._product_name, "Precio": self._price, "Cantidad" : self._quantity, "Descripción": self._description, "Categoria": self._category}


    def find_category(self, category):
        category.listing_categories()
        category_id = int(input("Seleccione la categporia"))
        list_category = category.categories.get(category_id)
        self._category = list_category
        return self._category

    def listing_products(self):
        for product_key, product_value in self.products.values():
            print(product_value)
            print(product_key)
            # print(self.print_product_personaliced(product_value))



    def print_product_personaliced(self, product):
        return f""" 
            Producto ID: {product.product_id}
            Nombre: {product.product_name}
            Precio: {product.price}
            Cantidad: {product.quantity}
            Descripción: {product.description}
            Categoria: {product.category["Nombre"]}
            """
