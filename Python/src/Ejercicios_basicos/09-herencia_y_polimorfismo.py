from os import name


class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        print("Este animal emite un sonido indeterminado")


class Dog (Animal):

    def sound(self):
        print("Guau!")


class Cat (Animal):

    def sound(self):
        print("Meouh!")


my_animal = Animal("animal")
my_dog = Dog("dog")
my_dog.sound()

'''
# Extra:
- Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su 
actividad, y almacena los empleados a su cargo.
'''
class Employee:
    current_id = 0

    def __init__(self, name: str):
        Employee.current_id += 1
        self.current_id = Employee.current_id
        self.name = name
        self.employees_in_charge = []

class Programmer(Employee):
    def __init__(self, name: str, languaje: str):
        super().__init__(name)
        self.languaje = languaje

    def to_program (self):
        print(f"El programador {self.name} está programando en {self.languaje}")

class Proyect_manager(Employee):
    def __init__(self, name:str, proyect_name: str, employees_in_charge: list):
        super().__init__(name)
        self.proyect_name = proyect_name
        self.employees_in_charge = employees_in_charge

    def show_employees_in_charge(self):
        print(f"La lista de empleados de {self.name} es: ")
        for employee in list(self.employees_in_charge):
            print (employee.name)

class Manager(Employee):
    def __init__(self, name: str, department: str, employees_in_charge: list):
        super().__init__(name)
        self.department = department
        self.employees_in_charge = employees_in_charge

    def manager_working(self):
        print(f"El gerente {self.name} está trabajando")

anto = Programmer("Anto", "Python")
anto.to_program()
ire = Programmer("Ire", "Javascript")
alba = Programmer("Alba", "Java")

pica = Proyect_manager("Pica", "Pica-proyect", [anto, ire, alba])
pica.show_employees_in_charge()

carlos = Manager("Carlos", "IT", [pica])
carlos.manager_working()






























'''
ME HE LIADO UN POCO, VAMOS A PROBAR DE OTRA MANERA.

class Employee:
    id = 0

    def __init__(self, name: str):
        self.name = name
        Employee.id += 1
        self.id = Employee.id
        self.employees = []
    
    def show_id (self):
        print(f"El empleado {self.name} tiene el id {self.id}")

    def add_employee(self, employee):
        self.employees.append(employee)

class Manager (Employee):
    functions = []

    def add_function(self, function: str):
        self.functions.append(function)

    def remove_function(self, function: str):
        self.functions.remove(function)
        print(f"La función, {function} ha sido eliminada")

    def show_functions(self):
        print(self.functions)

class Proyect_manager (Employee):
    def __init__(self, name: str, proyects: list):
        super().__init__(name)
        self.proyects = proyects



class programmer (Employee):

    def __init__(self, name: str, languages: list):
        super().__init__(name)
        self.languages = languages

    def code(self):
        print(f"El programador {self.name} está programando en {self.languages}")

    def add_employee(self, employee):
        print(f"El programador {self.name} no tiene empleados a su cargo")




first_employee = Employee("Anto")
first_employee.show_id()
second_employee = Employee("Anto2")
third_employee = Employee("Anto3")
fourth_employee = Employee("Anto4")
fourth_employee.show_id()

first_manager = Manager("Anto-manager")
first_manager.add_function("Python")
first_manager.add_function("Javascript")
first_manager.remove_function("Python")
first_manager.show_functions()

my_manager = Manager("Anto-manager")
my_proyect_manager = Proyect_manager("Anto-proyect-manager", ["proyecto1", "proyecto2"])
my_programmer = programmer("Anto-programmer", ["Python", "Java", "Javascript"])
my_manager.add_employee(my_proyect_manager)
print(my_manager.employees)

'''