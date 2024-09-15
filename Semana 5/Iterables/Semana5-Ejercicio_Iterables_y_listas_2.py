# 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#     1. Pista: investigue de que otras maneras se puede usar el `range`.
#     2. Ejemplos:
#     3. `my_string = ‘Pizza con piña’` → 
#     a
#     ñ
#     i
#     p
    
#     n
#     o
#     c
    
#     a
#     z
#     z
#     i
#     p

my_string = "Pizza con piña"

#Una forma sencilla es usando el reversed para imprimir la cadena a la inversa.
#for char in reversed(my_string):
#	print(char)
	
for char in range(len(my_string)-1,-1,-1):
	print(my_string[char])