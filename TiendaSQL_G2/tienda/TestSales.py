from Sales import Sales
from Conexion import Conexion


conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()
sale = Sales(None, None, None, None, None, None, None, None)
sale.update_sale(conexion)
