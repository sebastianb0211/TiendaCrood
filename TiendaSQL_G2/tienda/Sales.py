from Conexion import Conexion


class Sale:
    sale_id = None
    sale_date = None
    customer_id = None
    product_id = None
    price = None
    quantity = None
    total = None
    employee_id = None

    def __init__(self, sale_id, sale_date, customer_id, product_id, price, quantity, total, employee_id):
        self._sale_id = sale_id
        self._sale_date = sale_date
        self._customer_id = customer_id
        self._product_id = product_id
        self._price = price
        self._quantity = quantity
        self._total = total
        self._employee_id = employee_id

    @property
    def sale_id(self):
        return self._sale_id

    @sale_id.setter
    def sale_id(self, sale_id):
        self._sale_id = sale_id

    @property
    def sale_date(self):
        return self._sale_date

    @sale_date.setter
    def sale_date(self, sale_date):
        self._sale_date = sale_date

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

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
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @staticmethod
    def from_row(row):
        return Sale(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    def create_sale(self, db):
        self._sale_id = int(input("ID de venta: "))
        self._sale_date = input("Fecha de venta (YYYY-MM-DD HH:MM:SS): ")
        self._customer_id = int(input("ID de cliente: "))
        self._product_id = int(input("ID de producto: "))
        self._price = float(input("Precio: "))
        self._quantity = int(input("Cantidad: "))
        self._total = self._price * self._quantity
        self._employee_id = int(input("ID de empleado: "))
        query = "INSERT INTO sale (sale_id, sale_date, customer_id, product_id, price, quantity, total, employee_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (self._sale_id, self._sale_date, self._customer_id, self._product_id, self._price, self._quantity, self._total, self._employee_id)
        db.execute_query(query, params)

    def select_sales(self, db):
        query = "SELECT * FROM sale"
        result = db.execute_query(query)
        if result:
            sales = []
            for row in result:
                sale = Sale.from_row(row)
                sales.append(sale)
                print(f"ID de venta: {row[0]}, Fecha de venta: {row[1]}, ID de cliente: {row[2]}, ID de producto: {row[3]}, Precio: {row[4]}, Cantidad: {row[5]}, Total: {row[6]}, ID de empleado: {row[7]}")
            return sales
        else:
            print("Ventas no encontradas")
            return []

    def delete_sale(self, db, sale_id):
        query = "DELETE FROM sale WHERE sale_id = %s"
        db.execute_query(query, (sale_id,))