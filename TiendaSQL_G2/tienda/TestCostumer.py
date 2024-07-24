from Customer import Customer
from Conexion import Conexion



conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()

customer = Customer(None, None, None, None, None, None, None)

customer.create_customer(conexion)