#2. Cree una clase abstracta de `Shape` que:
#    1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#    2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#    3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.
import math
from abc import ABC, abstractmethod

# Clase abstracta Shape
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

# Clase Circle que hereda de Shape
class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

# Clase Square que hereda de Shape
class Square(Shape):
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        self.side_length = side_length
    
    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def calculate_area(self):
        return self.side_length ** 2

# Clase Rectangle que hereda de Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("El ancho y la altura deben ser números positivos.")
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height

# Ejemplo de uso
try:
    circle = Circle(5)
    print(f"Perímetro del círculo: {circle.calculate_perimeter()}")
    print(f"Área del círculo: {circle.calculate_area()}")

    square = Square(4)
    print(f"Perímetro del cuadrado: {square.calculate_perimeter()}")
    print(f"Área del cuadrado: {square.calculate_area()}")

    rectangle = Rectangle(3, 6)
    print(f"Perímetro del rectángulo: {rectangle.calculate_perimeter()}")
    print(f"Área del rectángulo: {rectangle.calculate_area()}")
    
except ValueError as e:
    print(f"Error: {e}")
