#Cree un programa que pida al usuario 100 números y muestre el mayor de todos.

numero_mayor = 0
contador = 1
while contador <= 100:
    numero_usuario = int(input(f"Favor ingrese el número: {contador} "))
    
    if numero_mayor < numero_usuario:
        numero_mayor = numero_usuario
    contador = contador + 1
print(f"El número mayor es: {numero_mayor}")      