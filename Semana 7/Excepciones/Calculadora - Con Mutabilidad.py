# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

import sys

num1 = 0
numactual = 0

menu = '''
**********************************************
1.Suma
2.Resta
3.Multiplicar
4.Dividir
5.Limpiar
6.Salir
**********************************************
'''
def Sumar(number):
    try:
        num1 = float(input("Ingresa un valor: "))
        number = number + num1 
        print(f'El resultado es: {number}' )

    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Sumar(numactual)
    return number

def Restar(number):
    try:
        num1 = float(input("Ingresa un valor: "))
        number = number - num1  
        print(f'El resultado es: {number}' )
        
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Restar(numactual)
    return number

def Multiplicar(number):
    try:
        num1 = float(input("Ingresa un valor: "))
        number = number * num1  
        print(f'El resultado es: {number}' )
        
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Multiplicar(numactual)
    return number

def Dividir(number):
    try:
        num1 = float(input("Ingresa un valor: "))
        try:
            number = number / num1
            print(f'El resultado es: {number}' )
        except ZeroDivisionError:
            print("ERROR!!No puede dividir entre 0.\n")
            Dividir(numactual)
            
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Dividir(numactual)
    return number

def Limpiar(number):
    number = 0
    return number

while True:
    print(menu)
    try:
        operacion = int(input("Favor ingrese una operación: "))
        if operacion == 1:
            numactual = Sumar(numactual)
        elif operacion == 2:
            numactual = Restar(numactual)
        elif operacion == 3:
            numactual = Multiplicar(numactual)
        elif operacion == 4:
            numactual = Dividir(numactual)
        elif operacion == 5:
           numactual = Limpiar(numactual)
        elif operacion == 6:
            sys.exit()
        else:
            print("Favor ingresar una opción valida.")
    except ValueError:
        print("ERROR!! Ingrese solo números.")