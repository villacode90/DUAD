nombre = str(input('Favor ingresar el nombre: '))
apellido = str(input('Favor ingresar el apellido: '))
domino_de_empresa = str(input('Favor ingresar el dominio de la empresa: '))
#email = nombre + '.' + apellido + '@' + domino_de_empresa + '.com.'
email = f'{nombre}.{apellido}@{domino_de_empresa}.com.'
print(email)


