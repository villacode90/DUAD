#2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
#    2.  Intente accesar a una variable global desde una función y cambiar su valor.

#1.Las variables definidad dentro una función solo puede ser accesible dentro de la función.

#Ejemplo:

# def Imprimir():
#     Mensaje = "Este es un mensaje de prueba"
#     print(Mensaje)

# def Main():
#     print(Mensaje)

# Imprimir()
# Main()

#En este ejemplo se puede ver que la función Main no puede acceder a la variable Mensaje declarada en la Función Imprimir. 
#Para lograr hacer que la función Main pueda acceder a la variable Mesnaje debemos de hacerla Global, es decir, declararla fuera de la función.

#Ejemplo:
# Mensaje = "Este es un mensaje de prueba"
  
# def Imprimir():    
#     print(Mensaje)

# def Main():
#     print(Mensaje)

# Imprimir()
# Main()


#2.

my_list_A = [1,2,3,4]
my_list_B = [5,6,7,8]

def First_Function():
    print(f'La Lista A era: {my_list_A}')
    my_list_A.extend(my_list_B)
    print(f'Ahora la Lista A es: {my_list_A}')

First_Function()