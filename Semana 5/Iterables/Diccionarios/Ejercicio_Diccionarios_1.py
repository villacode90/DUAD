# Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# numero_de_estrellas
# habitaciones
# El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# numero
# piso
# precio_por_noche

hotel_information = {
    'nombre' : 'La Fortuna Hotel',
    'numero_de_estrellas' : '5',
    'habitaciones' : [ {
        'numero' : '01',
        'piso' : 'Piso-Inferior',
        'precio_por_noche' : '100',
    },
    {
        'numero' : '02',
        'piso' : 'Segundo-Piso',
        'precio_por_noche' : '200',
    },
    {
        'numero' : '03',
        'piso' : 'Terraza',
        'precio_por_noche' : '400',
    },
    ]
}

for keys,values in hotel_information.items():
  print(f'{keys} : {values}')