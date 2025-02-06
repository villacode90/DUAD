def es_primo(num):
    """Verifica si un número es primo."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def filtrar_primos(lista):
    """Filtra y retorna una lista con los números primos de la lista dada."""
    return [num for num in lista if es_primo(num)]

# Lista de ejemplo
lista = [1, 4, 6, 7, 13, 9, 67]

# Usar la función para obtener los números primos
primos = filtrar_primos(lista)
print(primos)
