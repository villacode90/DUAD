# Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menos o mayor a 10 minutos.
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre ´Mayor´

segundos_restantes = 0
tiempo_en_segundos = float(input("Por favor, ingrese el tiempo en segundos "))
if tiempo_en_segundos > 600:
    print("Mayor")
else:
    segundos_restantes = 600 - tiempo_en_segundos
    print(f"Los segundos que hacen falta para llegar a 10 minutos son: {segundos_restantes}")
