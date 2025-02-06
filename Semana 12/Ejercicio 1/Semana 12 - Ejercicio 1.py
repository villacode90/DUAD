
#1. Cree una clase de `BankAccount` que:
#    1. Tenga un atributo de `balance`.
#    2. Tenga un método para ingresar dinero.
#    3. Tengo un método para retirar dinero.
#    
#    Cree otra clase que herede de esta llamada `SavingsAccount` que:
#    
#    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#    2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`.

#Clase Bank Account
class BankAccount:
    def __init__(self, initial_balance=0):

        self.balance = initial_balance

#Método para depositar dinero en la cuenta.
#Si el monto a depositar es 0 o negativo se imprimipra un mensaje del error.
#Sino se realizara la transacción y se notificara del nuevo balance.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depósito exitoso: ${amount}. Nuevo balance: ${self.balance}")
        else:
            raise ValueError("El monto del depósito debe ser positivo.")

#Método para retirar dinero de la cuenta.
#Si el monto a retirar es 0 o negativo se notificara del error.
#Si el monto a retirar es superior al monto disponible en la cuenta se notificara del error.
#Sino se realizara la transaccion y se notificata el nuevo monto.
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto de retiro debe ser positivo.")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        
        self.balance -= amount
        print(f"Retiro exitoso: ${amount}. Nuevo balance: ${self.balance}")

#Clase que herede de la clase BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, min_balance=0):

        super().__init__(initial_balance)
        self.min_balance = min_balance

#Método Heredado de la Clase BankAccount. 
#Ver linea 19 para definición.
    def withdraw(self, amount):
    
        if self.balance - amount < self.min_balance:
            raise ValueError(f"No se puede retirar, el balance no puede ser inferior a ${self.min_balance}.")
        
        super().withdraw(amount) 


#Pruebas del ejercicio.
#Se crea iniciarmente una cuenta con $1000 dolares y un balance minimo de 100
try:

    savings = SavingsAccount(1000, 100)

#Prueba Deposito
    savings.deposit(200)

#Prueba Retiro correcto
    savings.withdraw(950)  

#Prueba Retiro excesivo.
    savings.withdraw(250)  

except ValueError as e:
    print(f"Ha sucedido un error: {e}")
