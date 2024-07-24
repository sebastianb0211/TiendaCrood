from Conexion import Conexion

conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()

conexion.disconnect()