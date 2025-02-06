#Cree un programa que le pida 5 números al usuario y muestre el mayor.
#Ejemplos:
#4,76,43,6,8 = 76
#1,2,3,6,7 = 7
#2132,4355,1132,2323,1214,1214 = 4355
numero_mayor = 0
contador = 1
while contador <= 5:
    numero_usuario = int(input(f"Favor ingrese el número: {contador} "))
    
    if numero_mayor < numero_usuario:
        numero_mayor = numero_usuario
        contador = contador + 1
#        print(contador)
    else:
        contador = contador + 1
print(f"El número mayor es: {numero_mayor}")  