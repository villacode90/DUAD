# 3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#     1. Ejemplos:
#     2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`

mylist = [4,3,6,1,7]

print(mylist)

first_position = mylist[0]
last_position = mylist[-1]

mylist[0] = last_position
mylist[-1] = first_position

print(mylist)
