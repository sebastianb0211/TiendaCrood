from Employee import Employee
from Conexion import Conexion

conexion = Conexion(host='localhost', port=3306, user='root', password="", database='surabasedatos')

conexion.connnect_db()


employee = Employee(None, None, None, None, None, None, None)
employee.create_employee(conexion)