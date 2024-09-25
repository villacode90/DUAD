import sys

num1 = 0
numactual = 0

menu = '''
**********************************************
1.Ingresar Información de Estudiantes
2.Ver Información de Estudiantes
3.Top 3 Estudiantes
4.Promedio
5.Exportar
6.Importar
**********************************************
'''

while True:
    print(menu)
    try:
        opcion = int(input("Favor ingrese una opción: "))
        if opcion == 1:
           print # numactual = Sumar(numactual)      # Seleccionar para ingresar información de n cantidad de estudiantes al sistema.
        elif opcion == 2:
           print# numactual = Restar(numactual)      # Seleccionar para Ver la información ingresada en el sistema.
        elif opcion == 3:
           print# numactual = Multiplicar(numactual) # Seleccionar para ver el top 3 de estudiantes.
        elif opcion == 4:
           print# numactual = Dividir(numactual)     # Ver el promedio entre las notas de todos los estudiantes.
        elif opcion == 5:
           print#numactual = Limpiar(numactual)      # Exportar a un .csv la información ingresada en el sistema. 
        elif opcion == 6:                            # Importar la información desde un .csv previamente exportado. 
           print#
        elif opcion == 7:                       
            sys.exit()                               # Salir del Sistema
        else:
            print("Favor ingresar una opción valida.")
    except ValueError:
        print("ERROR!! Ingrese solo números.")