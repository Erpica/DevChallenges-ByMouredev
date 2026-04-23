# Recursividad
# Que se llame a sí misma y lo más importante el "hasta cuando"

def list_of_numbers(my_number = 100):
    if (my_number >=0):
        print(my_number)
        list_of_numbers(my_number - 1)

my_number = 10
list_of_numbers(my_number) 

""" 
# Así lo había hecho yo
def list_of_numbers(my_number = 100):
    if (my_number >=0):
        print(my_number)
        my_number -= 1
    else:
        return
    list_of_numbers(my_number)    

my_number = 10

list_of_numbers(my_number) """

""" 
# EXTRA:
Utiliza el concepto de recursividad para:
- Calcula el factorial de un número concreto (la función recibe ese número).
- Calcula el valor de un elemento concreto (según su posición) en la 
sucesión de Fibonacci (La función recibe la posición)
 """

""" # Así lo había hecho yo
def factorial_func (one_number: int):
    count = 0
    if (count == 0):
        product = one_number
        count += 1
        factorial_func(one_number - 1)
    else:
        if (one_number >= 1):
            product = one_number * factorial_func(one_number - 1)
        else:
            print(product)

factorial_func (3) """


def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial (number - 1)



print(factorial(5))



def fibonacci (number: int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else: 
        return fibonacci(number - 1) + fibonacci(number - 2)
    
print(fibonacci(8))

