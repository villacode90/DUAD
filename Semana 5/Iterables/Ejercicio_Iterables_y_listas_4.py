# 4. Cree un programa que elimine todos los números impares de una lista.
#     1. Ejemplos:
#     2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Lista sin cambios: {my_list}')  
for num in my_list:
    if num % 2 != 0:
        my_list.remove(num)
print(f'Lista sin números impares: {my_list}')  

