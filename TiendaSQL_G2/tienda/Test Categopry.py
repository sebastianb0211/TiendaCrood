from Category import Category
from Conexion import Conexion

conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()




category = Category(None, None)

category.update_category_name(conexion)

#category.delete_category(conexion, 1)





