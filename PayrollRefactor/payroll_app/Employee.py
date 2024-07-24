from payroll_app.User import User


class Employee(User):

    rol = None
    salary = None

    # comment



    def __init__(self, employee_id, name_employee, last_name_employee, email, password,rol, salary):
        super().__init__(employee_id, name_employee, last_name_employee, email, password )
        self._rol = rol
        self._salary = salary


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary


    #employees = []

    def create_user(self):
        #employee = []
        super().create_user()
        self._rol = input("Rol")
        #employee.append(self._rol)
        self._salary = input("Salario")
        #employee.append(self._salary)

        self.employees.append([self._employee_id , self._name_employee , self._last_name_employee, self._email, self._password, self._rol,self._salary])

        #User.employees.append(employee)

    def list_employee_data(self):
        for item in self.employees:
            print(item)
