#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41

def Operacion(La_Lista):   
    total = sum(La_Lista)
    return total

SumaDeTodoLosElementos = Operacion([4,6,2,29])
print(SumaDeTodoLosElementos)


