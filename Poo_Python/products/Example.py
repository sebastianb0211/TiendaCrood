


# {:}
num:int = 1

my_dict = { "id": num , "Nombre": "Maria"}


my_dict["Apellido"] = "Castro"

print(my_dict)

my_dict.update({"Salary" : 1300000})

print(my_dict)

for x, y in my_dict.items():
  print(x, y)
