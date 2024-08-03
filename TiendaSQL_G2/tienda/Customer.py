from Conexion import Conexion



class Customer:
    def __init__(self, customer_id, customer_name, customer_last_name, email, customer_password, customer_type, points):
        self._customer_id = customer_id
        self._customer_name = customer_name
        self._customer_last_name = customer_last_name
        self._email = email
        self._customer_password = customer_password
        self._customer_type = customer_type
        self._points = points

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name

    @property
    def customer_last_name(self):
        return self._customer_last_name

    @customer_last_name.setter
    def customer_last_name(self, customer_last_name):
        self._customer_last_name = customer_last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def customer_password(self):
        return self._customer_password

    @customer_password.setter
    def customer_password(self, customer_password):
        self._customer_password = customer_password

    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, customer_type):
        self._customer_type = customer_type

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points

    @staticmethod
    def from_row(row):
        return Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    def create_customer(self, db):
        self._customer_id = int(input("ID: "))
        self._customer_name = input("Nombre: ")
        self._customer_last_name = input("Apellido: ")
        self._email = input("Email: ")
        self._customer_password = input("Contraseña: ")
        self._customer_type = input("Tipo: ")
        self._points = int(input("Puntos: "))
        query = "INSERT INTO customer (customer_id, customer_name, customer_last_name, email, customer_password, customer_type, points) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (self._customer_id, self._customer_name, self._customer_last_name, self._email, self._customer_password, self._customer_type, self._points)
        db.execute_query(query, params)

    def select_customers(self, db):
        query = "SELECT * FROM customer"
        result = db.execute_query(query)
        if result:
            customers = []
            for row in result:
                customer = Customer.from_row(row)
                customers.append(customer)
                print(f"ID: {row[0]}, Nombre: {row[1]}, Apellido: {row[2]}, Email: {row[3]}, Tipo: {row[5]}, Puntos: {row[6]}")
            return customers
        else:
            print("Clientes no encontrados")
            return []

    def delete_customer(self, db, customer_id):
        query = "DELETE FROM customer WHERE customer_id = %s"
        db.execute_query(query, (customer_id,))

    def update_customer(self, db):
        customer_id = int(input("Ingrese el ID del cliente a actualizar: "))
        print("Ingrese los nuevos datos del cliente (deje en blanco para mantener el valor actual):")
        new_name = input("Nuevo nombre: ").strip()
        new_last_name = input("Nuevo apellido: ").strip()
        new_email = input("Nuevo email: ").strip()
        new_password = input("Nueva contraseña: ").strip()
        new_type = input("Nuevo tipo: ").strip()
        new_points = input("Nuevos puntos: ").strip()

        query = "UPDATE customer SET "
        params = []

        if new_name:
            query += "customer_name = %s, "
            params.append(new_name)
        if new_last_name:
            query += "customer_last_name = %s, "
            params.append(new_last_name)
        if new_email:
            query += "email = %s, "
            params.append(new_email)
        if new_password:
            query += "customer_password = %s, "
            params.append(new_password)
        if new_type:
            query += "customer_type = %s, "
            params.append(new_type)
        if new_points:
            query += "points = %s, "
            params.append(int(new_points))

        if params:
            query = query.rstrip(", ")  # Remove trailing comma and space
            query += " WHERE customer_id = %s"
            params.append(customer_id)
            db.execute_query(query, tuple(params))
        else:
            print("No se realizaron cambios, todos los valores estaban vacíos.")