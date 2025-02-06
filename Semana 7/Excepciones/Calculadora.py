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
num2 = 0

menu = '''
**********************************************
1.Suma
2.Resta
3.Multiplicar
4.Dividir
5.Salir
**********************************************
'''
def Sumar():
    try:
        print("Ingresa el Primer Número: ")
        num1 = float(input())
        print("Ingresa el Segundo Número: ")
        num2 = float(input())
        print("El resultado es: ", num1 + num2) 
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Sumar()

def Restar():
    try:
        print("Ingresa el Primer Número: ")
        num1 = float(input())
        print("Ingresa el Segundo Número: ")
        num2 = float(input())
        print("El resultado es: ", num1 - num2) 
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Restar()

def Multiplicar():
    try:
        print("Ingresa el Primer Número: ")
        num1 = float(input())
        print("Ingresa el Segundo Número: ")
        num2 = float(input())
        print("El resultado es: ", num1 * num2) 
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Multiplicar()

def Dividir():
    try:      
        print("Ingresa el Primer Número: ")
        num1 = float(input())
        print("Ingresa el Segundo Número: ")
        num2 = float(input())
        try:
            print("El resultado es: ", num1 / num2) 
        except ZeroDivisionError:
            print("ERROR!!No puede dividir entre 0.\n")
            Dividir()
    except ValueError:
        print("ERROR!! Ingrese solo números.\n")
        Dividir()

while True:
    print(menu)
    try:
        operacion = int(input("Favor ingrese una operación: \n"))
        if operacion == 1:
            Sumar()
        elif operacion == 2:
            Restar()
        elif operacion == 3:
            Multiplicar()
        elif operacion == 4:
            Dividir()
        elif operacion == 5:
            sys.exit()
        else:
            print("Favor ingresar una opción valida.")
    except ValueError:
        print("ERROR!! Ingrese solo números.")