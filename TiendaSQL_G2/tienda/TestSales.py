from Sales import Sale
from Conexion import Conexion


conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()
sale = Sale(None, None, None, None, None, None, None, None)
sale.create_sale(conexion)
