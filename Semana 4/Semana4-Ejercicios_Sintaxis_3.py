#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
import random
numero_secreto = random.randint(1, 10)
print(numero_secreto)
acierto = False
while acierto == False:
    numero_usuario = int(input("Adivina el número secreto! Ingrese un número entre 1 y 10" ))
    if numero_usuario != numero_secreto:
        print("Incorrecto! Favor intenta nuevamente.")
        acierto = False
    else:
        print("Felicidades, has acertado")
        acierto = True
    