from payroll_app.User import User


class Costumer(User):


    type = None
    points = None

    def __init__(self, employee_id, name_employee, last_name_employee, email, password, type, points):
        super().__init__(employee_id, name_employee, last_name_employee, email, password)
        self._type = type
        self._points = points


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points



    #costumers = {}


    def create_user(self):
        super().create_user()
        self._type = input("Tipo de cliente")
        self._points = int(input("Puntos"))

        self.costumers[self._employee_id]=  {"nombre": self._name_employee, "Apellido": self._last_name_employee, "correo": self._email, "contraseña": self._password, "Tipo Cliente": self._type, "Puntos": self._points}

    def list_costumers(self):
        for item in self.costumers.items():
            print(item)
