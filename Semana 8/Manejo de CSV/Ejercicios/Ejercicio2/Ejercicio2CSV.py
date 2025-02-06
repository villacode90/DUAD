# 2.Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
# Ejemplo de archivo final:
# nombre	genero	desarrollador	clasificacion
# Grand Theft Auto IV	Accion	Rockstar Games	M
# The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
# Tony Hawk's Pro Skater 2	Deportes	Activision	T

import csv

def agregar_datos():
    print("\n")
    nombre = input("Ingrese el nombre del videojuego: ")
    genero = input("Ingrese el genero del videojuego: ")
    desarrollador = input("Ingrese el nombre del desarrolador de videojuego: ")
    clasificacion_esrb = input("Ingrese la clasificación ESRB del videojuego: " )
    return[nombre,genero,desarrollador,clasificacion_esrb]

def guardarCSV(nombre_archivo, dic_videojuegos):
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Nombre','Género','Desarrollador','Clasificación ESRB'])
        writer.writerows(dic_videojuegos)


def main():
    nombre_archivo = './videogames.csv'

    dic_videojuegos = []

    numero_video_juegos = int(input(('¿Cuántos videojuegos vas a ingresar? ')))
    
    for i in range(numero_video_juegos):
        info_videojuegos = agregar_datos()
        dic_videojuegos.append(info_videojuegos)

    guardarCSV(nombre_archivo, dic_videojuegos)
    print(f"Se han guardado {numero_video_juegos} videojuegos en el archivo '{nombre_archivo}'.")

main()

