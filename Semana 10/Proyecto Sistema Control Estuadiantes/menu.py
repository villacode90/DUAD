import sys
import actions
import data


def menu_program():
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
    7.Salir
    **********************************************
    '''

while True:
    print(menu) 
    try:
        option = int(input("Favor ingrese una opción: "))
        if option == 1:
           actions.add_students()
        elif option == 2:
           actions.view_students()                         # Seleccionar para Ver la información ingresada en el sistema.
        elif option == 3:
          actions.top_students()                           # Seleccionar para ver el top 3 de estudiantes.
        elif option == 4:
          actions.average_grade()                          # Ver el promedio entre las notas de todos los estudiantes.
        elif option == 5:
           data.export_data()
        elif option == 6:
           data.import_data()                              # Exportar a un .csv la información ingresada en el sistema.                                                                   # Importar la información desde un .csv previamente exportado. 
        elif option == 7:                       
            sys.exit()                                     # Salir del Sistema
        else:
            print("Favor ingresar una opción valida.")
    except ValueError:
        print("ERROR!! Ingrese solo números.")