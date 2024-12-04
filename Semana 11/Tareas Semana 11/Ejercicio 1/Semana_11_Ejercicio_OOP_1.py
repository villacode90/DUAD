#1. Cree una clase de `Circle` con:
#    1. Un atributo de `radius` (radio).
#    2. Un método de `get_area` que retorne su área.

import math

class Circle():
	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		 return math.pi * (self.radius ** 2)


circle_area = int(input("Ingrese el radio del circulo, para conocer su área: "))

my_circle = Circle(circle_area) 

area = my_circle.get_area()

print(f"El área del circulo es: {area}")


