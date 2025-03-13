# Cree una clase de `User` que:
# - Tenga un atributo de `date_of_birth`.
# - Tenga un property de `age`.

# Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date
import numbers

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth


    def checkAge(func):
        def wrapper(*args,**kwargs):
                if any([arg for arg in args if isinstance(arg, numbers.Number) and arg > 18]):
                    pass
                else :
                    raise ValueError(f"No se puede completar el proceso ya que el usuario es menor de edad")
                
                func(*args,**kwargs)
        return wrapper


    @property
    def age(self):
        # Debemos calcular la edad cada vez que la usemos
        # ya que va a variar dependiendo de la fecha actual
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    @checkAge
    def printMessage(self, age):
        print(f'Función completada, ya que el User tiene: {age} años.')

my_user = User(date(1990, 11, 7))
userAge = my_user.age
my_user.printMessage(userAge)


