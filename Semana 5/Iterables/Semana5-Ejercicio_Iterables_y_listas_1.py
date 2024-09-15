# 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#     1. Ejemplos:
#     2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
#     `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
#     Hay casos
#     en los
#     que la
#     iteracion por
#     indice es
#     muy util

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']


#En Python, la función zip devuelve un iterador de tuplas donde cada tupla contiene los valores de la misma posición de dos o más elementos iterables, como las listas.
#for f, s in zip(first_list, second_list):
#    print(f, s)
    
for indice in range(0, len(first_list)):
	print(first_list[indice], second_list[indice])

