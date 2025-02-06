#1.Investigue cómo leer y escribir archivos JSON en Python aquí.

import json

def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as contenido:
            pokemons = json.load(contenido)
        for pokemon in pokemons:
            print(pokemon)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")
        return []

archivo = 'pokemons.json'

cargar_datos(archivo)



