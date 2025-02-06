#Cree un programa que le pida un numero al usuario y muestre "Fizz" si es divisible entre 3, "Buzz" si es divisible entre 5 Y "FizzBuzz" si es divisible entre ambos.
#Ejemplos:
#33 -> Fizz
#25 -> Buzz
#30 -> FizzBuzz

dividendo = int(input("Por favor, Introduzca un Número: "))
RestoA = dividendo % 3
RestoB = dividendo % 5
print(RestoA)
print(RestoB)

if RestoA == 0 and RestoB == 0:
    print("FizzBuzz")
elif RestoA == 0 and RestoB != 0:
    print("Fizz")
elif RestoB == 0 and RestoA != 0:
    print("Buzz")

