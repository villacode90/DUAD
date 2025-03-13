#Cree un decorador que haga print de los parámetros y retorno de la función que decore.
def print_result(func):
    def wrapper(*args,**kwargs):

        #Print Parameters
        print(f'Parameters: {args}, {kwargs}')
        
        #Execute the function decorated
        result = func(*args,**kwargs)

        #Print the return of the function
        print(f'Return: {result}')
        return result
    return wrapper

@print_result
def create_driver(name,last_name):
    fullname = name + ' ' + last_name
    return fullname


create_driver('Fabian','Villa')
