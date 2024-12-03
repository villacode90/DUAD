#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def ContadorLetras():
    string = "I love Nación Sushi"
    string_up = 0
    string_lo = 0
    for i in string:
        if i.isupper():
            string_up += 1
        elif i.islower():
            string_lo += 1
    print(f'El número de letras mayusculas es: {string_up}')
    print(f'El número de letras minusculas es: {string_lo}');

ContadorLetras()