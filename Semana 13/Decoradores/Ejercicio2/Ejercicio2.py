#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def checkValues(func):
    def wrapper(*args, **kwargs):
        # Check if all the values are numbers
        for i in args:
            #If the value is number going to pass and move it to the next one
            if isinstance(i, (int, float)):
                pass
            else: 
                #If a value is not a number going to print the exception
                raise ValueError(f"Valor no válido: {i}. Todos los valores deben ser números o números con decimales.")
        
        #calling the function
        return func(*args, **kwargs)  
    
    return wrapper

@checkValues
def printMessage(*args,**kwargs):
    print("Función ejecutada con éxito.")


#printMessage(1, 2, 3, 'Fabian', 4)  # Llamada con un string
printMessage(1, 2, 3, 4.5)  # Llamada correcta sin errores



