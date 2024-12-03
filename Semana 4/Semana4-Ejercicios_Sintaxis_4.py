#Cree un programa que le pida tres números al usuario y muestre el mayor.
numero_mayor = 0
contador = 1
while contador <= 3:
    numero_usuario = int(input(f"Favor ingrese el número: {contador} "))
    
    if numero_mayor < numero_usuario:
        numero_mayor = numero_usuario
        contador = contador + 1
#        print(contador)
    else:
        contador = contador + 1
print(f"El número mayor es: {numero_mayor}")        
