


class User:


    employee_id = None
    emp_name = None
    emp_last_name = None
    email = None
    password = None


    def __init__(self, employee_id, emp_name, emp_last_name, email, password):
        self._employee_id = employee_id
        self._emp_name = emp_name
        self._emp_last_name = emp_last_name
        self._email = email
        self._password = password


    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def emp_name(self):
        return self._emp_name

    @emp_name.setter
    def emp_name(self, emp_name):
        self._emp_name = emp_name

    ##Getters and setters




    def create_user(self):
        self._employee_id = input("Id:")
        self._emp_name = input("Nombre")
        self._emp_last_name = input ("Apellido")
        self._email = input("Email")
        self._password = input("Contraseña")




