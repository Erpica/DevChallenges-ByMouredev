# Abierto para la extensión
# código preparado para añadir cosas

# Cerrado para la modificación
# No tocar lo creado

class Form:
    def draw(self):
        pass

class Square(Form):
    def draw(self):
        print("Dibuja un cuadrado")

class Circle(Form):
    def draw(self):
        print("Dibuja un círculo")



# Extra
'''
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.
'''

class Calculator:
    def __init__(self):
        print("""
#####  Calculadora  ######
##                      ##
##    1. Sumar          ##
##    2. Restar         ##
##    3. Multiplicar    ##
##    4. Dividir        ##
##    5. Potencia       ##
##    6. Salir          ##
##                      ##
##########################
""")
        #option = input("Introduce una opción: ")

        option = 5
        if option == 1:
            my_sum_args = SumArgs()
        elif option == 2:
            my_rest = RestArgs()
        elif option == 3:
            my_multiply = MultiplyArgs()
        elif option == 4:
            my_multiply = DivArgs()
        elif option == 5:
            my_exit = PowArgs()
        elif option == 6:
            my_exit = MyExitClass()
        else: 
            print("Introduce una opción del menu.")


class SumArgs:
    def __init__(self):
        #a = input ("Introduce a")
        #b = input ("Introduce b")
        a = 1
        b = 2
        self.print_total(a, b)
    
    def print_total(self, *args):
        my_sum = 0
        for num in args:
            my_sum += num
    
        print(f"El resultado de la suma es {my_sum}.")

class RestArgs:
    def __init__(self):
        #a = input ("Introduce a")
        #b = input ("Introduce b")
        a = 1
        b = 2
        self.print_total(a, b)
    
    def print_total(self, a, b):
        print(f"El resultado de la resta es {a - b}.")

class MultiplyArgs:
    def __init__(self):
        #a = input ("Introduce a")
        #b = input ("Introduce b")
        a = 1
        b = 2
        self.print_total(a, b)
    
    def print_total(self, *args):
        my_multiply = 1
        for num in args:
            my_multiply *= num
    
        print(f"El resultado de la multiplicación es {my_multiply}.")
        
class DivArgs:
    def __init__(self):
        #a = input ("Introduce a")
        #b = input ("Introduce b")
        a = 1
        b = 2
        self.print_total(a, b)
    
    def print_total(self, a, b):
        print(f"El resultado de la división es {a / b}.")

class PowArgs:
    def __init__(self):
        #a = input ("Introduce a")
        #b = input ("Introduce b")
        a = 2
        b = 8
        self.print_total(a, b)

    def print_total(self, a, b):
        print(f"El resultado de la potencia es {a ** b}.")

class MyExitClass:
    def __init__(self):
        print("Gracias por usar la calculadora.")


my_calculator = Calculator()


# EXTRA by BRAIS:

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Operation):
    def execute(self, a, b):
        return a + b
    
class Substration(Operation):
    def execute(self, a, b):
        return a - b
    
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
class Division(Operation):
    def execute(self, a, b):
        return a / b
    
class Power(Operation):
    def execute(self, a, b):
        return a ** b
    
class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError (f"La operación {name} no está soportada.")
        return self.operations[name].execute(a, b)
    


calculator = Calculator()
calculator.add_operation("adition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

for i in calculator.operations:
    print(i)

print(calculator.calculate("adition", 10, 2))
print(calculator.calculate("substration", 10, 2))
print(calculator.calculate("multiplication", 10, 2))
print(calculator.calculate("division", 10, 2))
print(calculator.calculate("power", 10, 2))