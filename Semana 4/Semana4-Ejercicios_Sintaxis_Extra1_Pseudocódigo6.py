#Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer y 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
#Ejemplo:
#1,1,1,2,2,2 = 50% Mujeres y 50% Hombres
#1,1,2,2,2,2 = 33.3% Mujeres y 66% Hombres
#1,1,1,1,1,2 = 84.4 Mujeres y 16.6 Hombres

cantidad_de_personas = 6
porcentaje_sexo_femenino = 0
porcentaje_sexo_masculino = 0
cantidad_de_hombres = 0
cantidad_de_mujeres = 0
contador = 1
while contador <= cantidad_de_personas:
    sexo = int(input(f"Ingrese un sexo, 1 para Mujer y 2 para Hombre. Favor ingrese el sexo número: {contador} "))
    if sexo == 1:
        cantidad_de_mujeres = cantidad_de_mujeres + 1
    else:
        cantidad_de_hombres = cantidad_de_hombres + 1
    contador = contador + 1

porcentaje_sexo_femenino = (cantidad_de_mujeres / cantidad_de_personas) * 100
porcentaje_sexo_masculino = (cantidad_de_hombres / cantidad_de_personas) * 100

print(f"El porcetaje de mujeres es de: {porcentaje_sexo_femenino}")
print(f"El porcentaje de hombres es de: {porcentaje_sexo_masculino}")
      