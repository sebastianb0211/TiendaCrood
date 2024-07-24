from Product import Product
from Conexion import Conexion



conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()
product = Product(None, None, None, None, None, None, None)
product.create_product(conexion)