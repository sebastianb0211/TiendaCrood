



user_name = "Pepito"

users = ["Pepito", "Maria", "Juan", "Laura", "Pedro"]

print(type(users))

print(len(users))

print(users[0])

users[2] = "Cesar"

print(users[2])

#Esto es Slicing 
print(users[1:3])

print(users[0:])

print(users[:5])

for user in users:
    print(user)

for i in range(5):
    print(users[i])    
