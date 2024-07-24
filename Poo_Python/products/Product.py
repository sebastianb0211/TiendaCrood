

from Category import Category

class Product:

    product_id = None
    product_name = None
    category = None
    description = None
    price = None
    quantity = None
    brand = "My own brand"

    def __init__(self, product_id, product_name, category, description, price, quantity, brand):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.description = description
        self.price = price
        self.quantity = quantity
        self.brand = brand


    #Getters and Setters


    products = {}

    def create_product(self, category):
        self.product_id = input("id Producto")
        self.product_name = input("NOmbre producto")
        self.category = self.find_category(category)
        self.description  = input("Descripción")
        self.price = float(input("Precio"))
        self.quantity = int(input("Cantidad"))
        self.brand = input("Marca")
        #self.products[self.product_id] = {"id": self.product_id , "Nombre" :  self.product_name , "Categoria": self.category , "Decripcion": self.description, "Precio": self.price, "Cantidad": self.quantity, "Marca": self.brand}
        self.products[self.product_id] = self.product_id, self.product_name,self.category,self.description,self.price,self.quantity,self.brand



    def listing_products(self):
        for product in self.products.items():
            print(product)


    def find_category(self,category):
        category_id = int(input("Categoria"))
        category_list = category.categories.get(category_id)[1]
        self.category = category_list
        print(self.category)
        #value = input("Nombre categoria")
        #if value in self.category:
        return self.category
        #print(self.category)


