

employee_list = []

def register_employee():
    id = input("Id")
    employee_list.append(id)
    emp_name = input("Name")
    employee_list.append(emp_name)
    emp_lastname = input("Lastname")
    employee_list.append(emp_lastname)
    email = input("Email")
    employee_list.append(email)
    password = input("Password")
    employee_list.append(password)
    salary = int(input("Ingrese su salario"))
    employee_list.append(salary)

  

def print_employee_data():
    for emp in employee_list:
        print(emp)

print(employee_list)    



minimum_salary = 1300000

trans_aid = 162000

def calculate_health_discount(salary):
    healht_discount = salary * 0.04
    return healht_discount


def calculate_mortage_discount(salary):
    morgate_discount = salary * 0.04
    return morgate_discount


def calculate_net_salary(salary, minimum_salary , trans_aid):
    healt_discount = calculate_health_discount(salary)
    mortage_discount = calculate_mortage_discount(salary)
    if salary > 2*minimum_salary:
        net_salary = salary - healt_discount - mortage_discount
        
    else:
        net_salary = salary - healt_discount - mortage_discount + trans_aid 

    return net_salary





def init_user_menu(init_session):
    if init_session == True:
        print("1.Data Employee\n 2. Employee Net Salary")
        opc = int(input("Seleccione una opc"))
        match opc:
            case 1: 
                print("Employee Data")
                print_employee_data()
            case 2:
                print("Employee net salary")
                salary = employee_list[5]
                print(calculate_net_salary(salary, minimum_salary , trans_aid))
            case _:
                print("Seleccione una opcion valida")
    else:
        print("Valide sus credenciales")            






def init_session():
    email = input("Email")
    password = input("password")
    if email == employee_list[3] and password == employee_list[4]:
        return True
    else: 
        return False
    

#init_session = init_session()    


def menu_app():

    opc = int(input("1.Registrarse\n 2. Iniciar Sesion\n 3. Salir"))

    match opc:
        case 1:
            print("1. Registro")
            register_employee()  
        case 2:
            print("2. Iniciar Sesion")
            init_user_menu(init_session()) 
        case 3:
            print("Salir") 
            init = 0
        case _:
            print("Ingrese una opcion Valida")           


def app():
    init = input("Presione 1 para inicializar")
    while init != 0:
        menu_app()

app()        
    