from Conexion import Conexion


class Product:
    product_id = None
    product_name = None
    description = None
    category_id = None
    price = None
    quantity = None
    brand = None

    def __init__(self, product_id, product_name, description, category_id, price, quantity, brand):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._category_id = category_id
        self._price = price
        self._quantity = quantity
        self._brand = brand

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        self._product_name = product_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @staticmethod
    def from_row(row):
        return Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def create_product(self, db):
        self._product_id = int(input("ID: "))
        self._product_name = input("Nombre: ")
        self._description = input("Descripción: ")
        self._category_id = int(input("ID de categoría: "))
        self._price = float(input("Precio: "))
        self._quantity = int(input("Cantidad: "))
        self._brand = input("Marca: ")
        query = "INSERT INTO product (product_id, product_name, description, category_id, price, quantity, brand) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (self._product_id, self._product_name, self._description, self._category_id, self._price, self._quantity, self._brand)
        db.execute_query(query, params)

    def select_products(self, db):
        query = "SELECT * FROM product"
        result = db.execute_query(query)
        if result:
            products = []
            for row in result:
                product = Product.from_row(row)
                products.append(product)
                print(f"ID: {row[0]}, Nombre: {row[1]}, Descripción: {row[2]}, ID de Categoría: {row[3]}, Precio: {row[4]}, Cantidad: {row[5]}, Marca: {row[6]}")
            return products
        else:
            print("Productos no encontrados")
            return []

    def delete_product(self, db, product_id):
        query = "DELETE FROM product WHERE product_id = %s"
        db.execute_query(query, (product_id,))

    def update_product(self, db):
        product_id = int(input("Ingrese el ID del producto a actualizar: "))
        print("Ingrese los nuevos datos del producto (deje en blanco para mantener el valor actual):")
        new_name = input("Nuevo nombre: ").strip()
        new_description = input("Nueva descripción: ").strip()
        new_category_id = input("Nuevo ID de categoría: ").strip()
        new_price = input("Nuevo precio: ").strip()
        new_quantity = input("Nueva cantidad: ").strip()
        new_brand = input("Nueva marca: ").strip()

        query = "UPDATE product SET "
        params = []

        if new_name:
            query += "product_name = %s, "
            params.append(new_name)
        if new_description:
            query += "description = %s, "
            params.append(new_description)
        if new_category_id:
            query += "category_id = %s, "
            params.append(int(new_category_id))
        if new_price:
            query += "price = %s, "
            params.append(float(new_price))
        if new_quantity:
            query += "quantity = %s, "
            params.append(int(new_quantity))
        if new_brand:
            query += "brand = %s, "
            params.append(new_brand)

        if params:
            query = query.rstrip(", ")  # Remove trailing comma and space
            query += " WHERE product_id = %s"
            params.append(product_id)
            db.execute_query(query, tuple(params))
        else:
            print("No se realizaron cambios, todos los valores estaban vacíos.")

