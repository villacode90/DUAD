# Dada n cantidad de notas de un estudiante, calcular:
# a. Cuantas notas tiene aprobadas(mayor a 70)
# b.Cuantas notas tiene desaprobadas(menor a 70)
# c.El promerdio de todas.
# d.El promedio de aprobadas.
# e. El promedio de las desaprobadas.

contador_de_nota = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas__desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

total_de_notas = int(input("Ingrese la cantidad de notas: "))

while contador_de_nota <= total_de_notas:
    nota_actual = int(input(f"Ingrese la nota número: {contador_de_nota} "))
    if nota_actual < 70:
        cantidad_de_notas__desaprobadas = cantidad_de_notas__desaprobadas + 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
        contador_de_nota = contador_de_nota + 1
    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
        contador_de_nota = contador_de_nota + 1

promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)

promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas__desaprobadas
promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas

print(f"El estudiante tiene está cantidad de notas aprobadas: {cantidad_de_notas_aprobadas}")
print(f"Esté es el promedio de notas aprobadas: {promedio_de_notas_aprobadas}")
print(f"El estudiante tiene está cantidad de notas desaprobadas: {cantidad_de_notas__desaprobadas}")
print(f"Esté es el promedio de notas desaprobadas: {promedio_de_notas_desaprobadas}")