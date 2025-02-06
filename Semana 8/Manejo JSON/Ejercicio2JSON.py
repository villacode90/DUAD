# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def leer_archivo(nombre_archivo):
# Lee el contenido de un archivo JSON y lo devuelve como una lista de diccionarios
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")
        return []

def guardar_archivo(nombre_archivo, datos):
# Guarda la lista de diccionarios en el archivo JSON
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)

def obtener_datos():
# Solicita al usuario la información del nuevo Pokémon y la devuelve como un diccionario
    nombre_ingles = input("Nombre en inglés del Pokémon: ")
    tipo = input("Tipo del Pokémon (separado por comas): ").split(',')
    tipo = [t.strip() for t in tipo]  # Limpia los espacios en blanco
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    return {
        "name": {
            "english": nombre_ingles
        },
        "type": tipo,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

def agregar_pokemon_a_archivo(nombre_archivo):
    """Agrega un nuevo Pokémon al archivo JSON existente."""
    pokemons = leer_archivo(nombre_archivo)
    nuevo_pokemon = obtener_datos()
    pokemons.append(nuevo_pokemon)
    guardar_archivo(nombre_archivo, pokemons)
    print("¡Nuevo Pokémon agregado exitosamente!")

# Nombre del archivo JSON
nombre_archivo = './pokemons.json'

# Ejecutar la función para agregar un nuevo Pokémon
agregar_pokemon_a_archivo(nombre_archivo)