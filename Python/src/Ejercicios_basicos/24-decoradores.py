# Los decoradores también son patrones de diseño

# Es una función que se utiliza para modificar o extender la funcionalidad de una función 
# pero sin modificar la función a la que le aplicamos el decorador.
# "decora" o modifica el resultado pero no cambia la función a la que se lo aplicamos.
# Un decorador en Python, por norma estricta, solo puede recibir un único parámetro en su función externa: la función que va a decorar.

def print_call(function):
    def print_function():
        print(f"La función '{function.__name__}' ha sido llamada.")
        return function
    return print_function

@print_call
def example_function():
    pass
    
@print_call
def example_function_2():
    pass

@print_call
def example_function_3():
    pass
    

example_function()
example_function_2()
example_function_3()

# Extra
'''
Crea un decorador que sea capaz de contabilizar cuántas veces
se ha llamado a una función y aplícalo a una función de tu elección
'''

def haw_many(function): # se le llama función externa
    count = 0
    def print_function(*args): # sería la función interna
        nonlocal count
        count += 1
        print(f"La función {function.__name__} se ha llamado {count} veces")
        return function(*args) # Siempre retornamos la función interna
    return print_function

    

@haw_many
def sum(a, b):
    return a + b

@haw_many
def example_function_4():
    pass

print(sum(2, 3))
print(sum(3, 4))
print(sum(1, 2))
example_function_4() # Cada decorador tiene su propio contador
print(sum(1, 2))