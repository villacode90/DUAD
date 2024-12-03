# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
nombre = str(input("Favor ingrese el nombre del Usuario: "))
apellido = str(input("Favor ingrese el apellido del Usuario: "))
edad = int(input("Favor ingrese el edad del Usuario: "))

if (edad < 1):
 print(f'El usuario {nombre} {apellido} es un: Bebé')
elif(edad > 1 and edad < 3):
 print(f'El usuario {nombre} {apellido} es un: Niño')
elif(edad > 5 and edad < 12):
 print(f'El usuario {nombre} {apellido} es un: Preadolesente')
elif(edad > 12 and edad < 18):
 print(f'El usuario {nombre} {apellido} es un: Adolecente')
elif(edad > 18 and edad < 21):
 print(f'El usuario {nombre} {apellido} es un: Adulto Joven')
elif(edad > 21 and edad < 65):
 print(f'El usuario {nombre} {apellido} es un: Adulto') 
else:
 print(f'El usuario {nombre} {apellido} es un: Adulto Mayor')