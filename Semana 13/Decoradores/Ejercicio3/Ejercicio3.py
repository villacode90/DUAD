# Cree una clase de `User` que:
# - Tenga un atributo de `date_of_birth`.
# - Tenga un property de `age`.

# Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date
import functools

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

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
    
def checkAge(func):
    functools.wraps(func)
    def wrapper(user: User,*args,**kwargs):
            if user.age < 18:
                raise ValueError(f"No se puede completar el proceso ya que el usuario es menor de edad")
            
            return func(user, *args, **kwargs)
    return wrapper
    
@checkAge
def printMessage(user: User):
    print(f'Función completada, ya que el User tiene: {user.age} años.')

my_user = User(date(1990, 11, 7))
printMessage(my_user)


