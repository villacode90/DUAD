# 1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#     1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
#     *Los errores son oportunidades de aprendizaje.*
#     2. Por ejemplo:
#         1. string + string → ?
#         2. string + int → ?
#         3. int + string → ?
#         4. list + list → ?
#         5. string + list → ?
#         6. float + int → ?
#         7. bool + bool → ?

#1 string + string → 
variable_A = str('Hola')
variable_B = str('Mundo')

resultado1 = variable_A + variable_B

print(resultado1) #Se concatenan la variable A con la Variable B

#2 string + int →
variable_A = str('Hola')
variable_B = int(1)

resultado2 = variable_A + variable_B 

print(resultado2) #Da error por que no se puede sumar un string con un integer. Lo correcto seria resultado2 = f'{variable_A}{variable_B}'

# #3 int + string →
variable_A = str('Hola')
variable_B = int(1)

resultado3 = variable_B + variable_A

print(resultado3) #Da error por que no se puede sumar un integer con un string. Lo correcto seria resultado3 = f'{variable_B}{variable_A}'

# #4 list + list → 
variable_A = [1,2,3,4]
variable_B = [5,6,7,8]

resultado4 = variable_A + variable_B

print(resultado4) # El resiltado es [1, 2, 3, 4, 5, 6, 7, 8]

#5 string + list →
variable_A = str('Hola')
variable_B = [1,2,3]

resultado5 = variable_B + variable_A # Da error no se puede sumar un string con una lista. Lo ideal seria resultado5 = f'{variable_A}{variable_B}'

#print(resultado5) 

#6 float + int →
variable_A = float(10.5)
variable_B = int(7)

resultado6 = variable_B + variable_A  

print(resultado6) #Resultado 17.5

#7 bool + bool → 
variable_A = bool(True)
variable_B = bool(False)

resultado7 = variable_B + variable_A  

print(resultado7) #Resultado 1
