import csv
import os

def export_data(students):
    with open('estudiantes.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribir encabezados
        writer.writerow(["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias", "Promedio"])
        
        # Escribir los datos de cada estudiante
        for student in students:
            # Convertir los atributos del objeto Student a una lista
            writer.writerow([
                student.name, 
                student.section, 
                student.spanish, 
                student.english, 
                student.socials, 
                student.sciences, 
                student.average
            ])
    print("Datos exportados a estudiantes.csv.")

def import_data(students):

    from actions import Student

    if os.path.exists('estudiantes.csv'):
        with open('estudiantes.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar los encabezados
            for row in reader:
                # Convertir cada fila del CSV en un objeto Student
                name = row[0]
                section = row[1]
                spanish = float(row[2])
                english = float(row[3])
                socials = float(row[4])
                sciences = float(row[5])
                average = float(row[6])

                # Crear un objeto Student y agregarlo a la lista de estudiantes
                my_student = Student(name, section, spanish, english, socials, sciences)
                students.append(my_student)

        print("Datos importados desde estudiantes.csv.")
    else:
        print("No hay un archivo 'estudiantes.csv' previamente exportado.")
