#2. Cree una clase de `Bus` con:
#    1. Un atributo de `max_passengers`.
#    2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). 
#   "Este solo debe agregar pasajeros si lleva menos de su máximo."" Sino, debe mostrar un mensaje de que el bus está lleno.
#    3. Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengersList = []

    def add_passenger(self, person):
        if len(self.passengersList) < self.max_passengers:
            self.passengersList.append(person)
            print(f"{person} ha subido al bus.")
        else:
            print("El bus está lleno, no se puede agregar más pasajeros.")
        
    def drop_passagers(self, Person):
        if Person in self.passengersList:
            self.passengersList.remove(Person)
            print(f"{Person} se ha bajado del Bus.")
        else:
            print("{Person} no está en el Bus.")

class Person:
    def __init__(self,name):
     self.name = name

    def __str__(self):
        return self.name 

Persona1 = Person("Esperanza")
Persona2 = Person("Fabián")
Persona3 = Person("Nestor")

my_bus = Bus(2)

my_bus.add_passenger(Persona1)
my_bus.add_passenger(Persona2)
my_bus.add_passenger(Persona3)

my_bus.drop_passagers(Persona1)
my_bus.drop_passagers(Persona2)

my_bus.add_passenger(Persona3)

