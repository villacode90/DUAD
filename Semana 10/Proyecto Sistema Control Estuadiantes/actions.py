from data import students  # Importar la lista de estudiantes

def add_students():
    n = int(input("Ingrese la cantidad de estudiantes a registrar: "))
    
    for _ in range(n):
        name = input("Ingrese el nombre completo del estudiante: ")
        section = input("Ingrese la sección del estudiante (ejemplo: 11B): ")

        notes = {}
        for grade in ["español", "inglés", "sociales", "ciencias"]:
            while True:
                try:
                    note = float(input(f"Ingrese la nota de {grade} (0-100): "))
                    if 0 <= note <= 100:
                        notes[grade] = note
                        break
                    else:
                        print("Nota no válida. Debe estar entre 0 y 100.")
                except ValueError:
                    print("Entrada no válida. Debe ingresar un número.")

        average = sum(notes.values()) / len(notes)
        student_data = {
            "name": name,
            "section": section,
            "spanish": notes["español"],
            "english": notes["inglés"],
            "socials": notes["sociales"],
            "sciences": notes["ciencias"],
            "average": average
        }
        students.append(student_data)

def view_students():
    for student in students:
        print(f"{student['name']} - {student['section']} - "
              f"Español: {student['spanish']}, Inglés: {student['english']}, "
              f"Sociales: {student['socials']}, Ciencias: {student['sciences']} - "
              f"Promedio: {student['average']}")

def top_students():
    sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)[:3]
    print("Top 3 estudiantes:")
    for student in sorted_students:
        print(f"{student['name']} - Promedio: {student['average']}")

def average_grade():
    if students:
        overall_average = sum(student['average'] for student in students) / len(students)
        print(f"Nota promedio entre todos los estudiantes: {overall_average}")
    else:
        print("No hay estudiantes registrados.")
