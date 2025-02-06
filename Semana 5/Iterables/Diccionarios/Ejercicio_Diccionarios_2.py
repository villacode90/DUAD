# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#     1. Ejemplos:
#     2. `list_a = ['first_name', ‘last_name', ‘role']`
#     `list_b = ['Alek', ‘Castillo', ‘Software Engineer']`
#     → `{'first_name': ‘Alek', ‘last_name': ‘Castillo', ‘role': ‘Software Engineer'}`


#Forma facil.
#Utulizando el metodo dict para crear el diccionario y el metodo zip, para emparejar cada elemento de la list_a con el elemento de la list_b
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
#name_information = dict(zip(list_a,list_b))

#print(name_information)

#Forma Compleja
#En este caso recorro una de las dos listas y le vamos a añadir parejas keys valor, cuyas keys seran el indice i de la lista_a y el valor el indice i de la lista_b 

name_information = {}

for i in range(len(list_a)):
    name_information[list_a[i]] = list_b[i]

print(name_information)    

