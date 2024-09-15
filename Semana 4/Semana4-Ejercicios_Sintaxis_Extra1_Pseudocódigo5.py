# Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s.
# Recuerde que 1 km == 1000 y 1 hora == 60 segundos
# Ejemplos:
# 72 = 20.27
# 50 = 13.88
# 120 = 33.33

velocidad_en_kilometros = float(input("Ingrese la velocidad en km/h: "))
metros_por_km = 1000
segundos_en_hora = 3600
metros_por_segundo = (velocidad_en_kilometros * metros_por_km/segundos_en_hora)
print(f"Los m/s son: {metros_por_segundo}")
