#Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar "Correcto". Sino, mostrar "incorreccto".
#Ejemplos:
#23,30,768 = Correcto
#10,15,5 = Correcto
#35,56,2 = Incorrecto

primer_numero = int(input("Favor ingrese el primer numero: "))
segundo_numero = int(input("Favor ingrese el segundo numero: "))
tercer_numero = int(input("Favor ingrese el tercer numero: "))
suma_total = 0
suma_total = primer_numero + segundo_numero + tercer_numero

if primer_numero == 30:
    print("Correcto!")
elif segundo_numero == 30:
    print("Correcto!")
elif tercer_numero == 30:
    print("Correcto!")    
elif suma_total == 30:
    print("Correcto!")
else:
    print("Incorrecto!")