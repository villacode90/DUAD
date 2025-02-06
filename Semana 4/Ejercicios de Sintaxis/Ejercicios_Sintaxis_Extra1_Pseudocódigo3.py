#Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.
numero_usuario = int(input("Ingrese un numero por favor: "))
contador = 0
suma_total = 0
suma_contador = 0
proceso = True


while contador < numero_usuario:
        suma_contador = suma_contador + 1
        suma_total = suma_total + suma_contador
        contador = contador + 1
print(f"La suma de todos los números de 1 hasta el número ingresado es: {suma_total}")
