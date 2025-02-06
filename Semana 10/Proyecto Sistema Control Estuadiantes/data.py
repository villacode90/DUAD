import csv
import os

# Lista global de estudiantes
students = []

def export_data():
    with open('estudiantes.csv', mode='w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sección", "Español", "Inglés", "Sociales", "Ciencias", "Promedio"])
        for student in students:
            writer.writerow([
                student['name'], 
                student['section'], 
                student['spanish'], 
                student['english'], 
                student['socials'], 
                student['sciences'], 
                student['average']
            ])
    print("Datos exportados a estudiantes.csv.")

def import_data():
    if os.path.exists('estudiantes.csv'):
        with open('estudiantes.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar encabezados
            for row in reader:
                name = row[0]
                section = row[1]
                spanish = float(row[2])
                english = float(row[3])
                socials = float(row[4])
                sciences = float(row[5])
                average = float(row[6])
                students.append({
                    "name": name,
                    "section": section,
                    "spanish": spanish,
                    "english": english,
                    "socials": socials,
                    "sciences": sciences,
                    "average": average
                })
        print("Datos importados desde estudiantes.csv.")
    else:
        print("No hay un archivo 'estudiantes.csv' previamente exportado.")
