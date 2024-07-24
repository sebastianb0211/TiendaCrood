

phone = "3214567890"
email = "email@email.com"
password = "12345678"

user = input("Ingrese el numero de telefono o su correo")

pass_user = input("ingrese su password")

if (phone == user or email == user) and password == pass_user:
    print("Bienvenido")
else:
    print("Valide sus credenciales")    
