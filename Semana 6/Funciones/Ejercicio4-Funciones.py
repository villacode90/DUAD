#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”


def Tranformar(mensaje):
    cadena_invertida = mensaje[::-1]
    return cadena_invertida

Mensaje = Tranformar("Hola Mundo")
print (Mensaje)


