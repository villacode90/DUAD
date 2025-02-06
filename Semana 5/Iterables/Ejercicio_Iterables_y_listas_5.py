# 5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#     1. Ejemplos:
#     2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.


myList = []

numero_mayor = 0
contador = 1
while contador <= 10:
    numero_usuario = int(input(f"Favor ingrese el número: {contador} "))
    
    myList.append(numero_usuario)

    if numero_mayor < numero_usuario:
        numero_mayor = numero_usuario
        contador = contador + 1
#        print(contador)
    else:
        contador = contador + 1
print(f'{myList}, el número mayor de la lista es el: {numero_mayor}')