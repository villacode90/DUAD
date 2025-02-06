# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def Conversion(string):
    #Convierto el string a Lista
    NuevaLista = list(string.split("-"))

    #Ordeno la Lista Alfabeticamente
    NuevaLista.sort()

    #Convierto la lista a string separando cada palabra con un "-"
    ListaToString = '-'.join([str(elem) for elem in NuevaLista])

    #Retorno el String convertido
    return ListaToString

#Defino la variable e imprimo lo que me devuelve la funcion Conversion
string = "python-variable-funcion-computadora-monitor" 
print(Conversion(string))