# 1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

File_list = []

def open_and_read_file(path):
    try:
        with open(path) as file:
            for line in file.readlines():
                File_list.append(line)
                File_list.sort()
        with open(file2_path,'a') as file:
            file.writelines(File_list)
            print('Complete')
    except Exception as error:
        print(f'Ha ocurrido un error:{error}')

file1_path = "Lista1.txt"
file2_path = "Lista2.txt"


open_and_read_file(file1_path)

