from MyPayrolllApp.User import User


class Employee(User):


    salary = None
    position = None

    def __init__(self, employee_id, emp_name, emp_last_name, email, password, salary, position):
        super().__init__(employee_id, emp_name, emp_last_name, email, password)
        self._salary = salary
        self._position = position


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self.salary = salary


    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    employees = []

    def create_user(self):
        super().create_user()
        self._salary = input("Salario")
        self._position = input("Cargo")
        self.employees.append([self._employee_id, self._emp_name, self._emp_last_name, self._email, self._password, self._salary, self._position])
    


    def list_employees(self):
        for emp in self.employees:
            print(emp)