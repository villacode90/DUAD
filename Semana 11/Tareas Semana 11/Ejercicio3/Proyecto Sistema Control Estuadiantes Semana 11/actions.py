class Student:
    def __init__(self, name, section, spanish, english, socials, sciences):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.socials = socials
        self.sciences = sciences
        self.average = (spanish + english + socials + sciences) / 4


    def __repr__(self):
        return f"{self.name} - {self.section} - Español: {self.spanish}, Inglés: {self.english}, " \
               f"Sociales: {self.socials}, Ciencias: {self.sciences} - Promedio: {self.average}"


def add_students(students):
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

       
        my_student = Student(
            name=name,
            section=section,
            spanish=notes["español"],
            english=notes["inglés"],
            socials=notes["sociales"],
            sciences=notes["ciencias"]
        )
        

        students.append(my_student)

def view_students(students):
    for student in students:
        print(student)


def top_students(students):
    sorted_students = sorted(students, key=lambda x: x.average, reverse=True)[:3]
    print("Top 3 estudiantes:")
    for student in sorted_students:
        print(f"{student.name} - Promedio: {student.average}")
       
def average_grade(students):
    if students:
        # Depuración: Imprimir los valores de 'average' de los estudiantes
        for student in students:
            print(f"Promedio de {student.name}: {student.average}")

        overall_average = sum(student.average for student in students) / len(students)
        print(f"Nota promedio entre todos los estudiantes: {overall_average}")
    else:
        print("No hay estudiantes registrados.")

