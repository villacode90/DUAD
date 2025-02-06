# def open_and_print_file(path):
# 	file = open(path)
# 	print(file.read())

def open_and_print_file(path):
	with open(path) as file:
		print(file.read()) 

	print("La variable 'file' ya no existe")
	print('El archivo ya no esta abierto')

open_and_print_file("D:\Fvillalobos\Estudio\Lifter\Semana 8\Test.txt")