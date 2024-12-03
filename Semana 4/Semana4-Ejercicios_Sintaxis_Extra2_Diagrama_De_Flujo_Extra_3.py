#Cree un programa que pida 100 números al usuario y muestre la suma de todos

total = 0
contador = 1

while contador <= 100:
    numero_usuario = int(input(f"Por Favor, ingrese el número: {contador} "))
    total = total + numero_usuario
    contador = contador + 1
print(f"La suma de todos los números es: {total} ")
