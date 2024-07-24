

class User:


    employee_id = None
    name_employee = None
    last_name_employee = None
    email = None
    password = None


    # comment

    def __init__(self, employee_id, name_employee, last_name_employee, email, password):
        self._employee_id = employee_id
        self._name_employee = name_employee
        self._last_name_employee = last_name_employee
        self._email = email
        self._password = password


    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    employees = []
    costumers = {}

    def create_user(self):
        # employee = []
        self._employee_id = input("Id Empleado")
        # employee.append(self._employee_id)
        self._name_employee = input("Nombre empleado")
        # employee.append(self._name_employee)
        self._last_name_employee = input("Apellido empleado")
        # employee.append(self._last_name_employee)
        self._email = input("Email")
        # employee.append(self._email)
        self._password = input("Contraseña")
        # employee.append(self._password)
        # employees.append(employee)



    def list_employee_data(self):
        for item in self.employees:
            print(item)