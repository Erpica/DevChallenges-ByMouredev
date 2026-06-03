'''
# LSP significan Liskov Substitution Principle (en español: Principio de Sustitución de Liskov).
- Una clase hija debe poder sustituir a su clase padre sin que el programa se rompa ni haga cosas raras.
- Para cumplir el principio LSP, la regla de oro es: la clase hija no puede exigir más ni ofrecer menos que la clase padre. 
Por lo tanto, una función hija puede tener argumentos diferentes siempre y cuando cualquiera que use la clase padre pueda 
seguir llamando a la función exactamente igual sin que el código explote.
Por ejemplo: Añadir argumentos opcionales (con valores por defecto): El hijo puede aceptar más cosas, 
siempre que tengan un valor predeterminado. Así, si alguien usa el hijo pensando que es el padre, el código funcionará perfectamente.

En las aves el error es que, cuando creas el pinguino, te das cuenta que necesitas dos clases intermedias:
AveQueVuela y AveQueNoVuela
'''

# Incorrecto

class Bird:
    def fly(self):
        return "Flying"
    
class Chicken(Bird):
    def fly(self):
        # raise Exception("Los pollos no vuelan")
        pass
    
bird = Bird()
bird.fly()
chicken = Chicken()
chicken.fly()

# Correcto:
class Bird:
    def move(self):
        return "moving"
    
class Chicken(Bird):
    def move(self):
        return "walking"
    
'''
Así sería lo natural
bird = Bird()
print(bird.move())
chicken = Chicken()
chicken.move()
print(chicken.move())
'''
# Y así vamos a comprobar si se cumple el principio de Liskov
bird = Chicken() # Cambio instancia padre por hija
print(bird.move())
chicken = Bird() # Cambio instancia hija por padre
chicken.move()
print(chicken.move())

# EXTRA:
'''
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como 
complir el LSP.
Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.
'''

""" class Vehicle1:

    def acelerate(self):
        print("estoy acelerando")

    def brake(self):
        print("estoy frenando")

class Car1 (Vehicle1):
    def acelerate(self):
        print(f"Soy un coche y ", end="")
        super().acelerate()

    def brake(self):
        print(f"Soy un coche y ", end="")
        super().brake()

class Motorcycle1 (Vehicle1):
    pass

class Truck1 (Vehicle1):
    pass

my_vehicle1 = Vehicle1()
my_vehicle1.acelerate()

my_car1 = Car1()
my_car1.acelerate()
my_car1.brake()


my_car2 = Vehicle1()
my_car2.acelerate()
my_car2.brake() """


print("\n\n # BY BRAIS:\n")
class Vehicle:
    def __init__(self, speed = 0):
        self.speed = speed

    def acelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")

class Car(Vehicle):
    def acelerate(self, increment):
        print("El coche está acelerando")
        super().acelerate(increment)
    
    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)

class Bicycle(Vehicle):
    def acelerate(self, increment):
        print("La bicicleta está acelerando")
        super().acelerate(increment)
    
    def brake(self, decrement):
        super().brake(decrement)
        print("La bicicleta está frenando")

class Motorcycle(Vehicle):
    def acelerate(self, increment):
        print("La motocicleta está acelerando")
        super().acelerate(increment)
    
    def brake(self, decrement):
        print("La motocicleta está frenando")
        super().brake(decrement)

def test_vehicle(vehicle):
    vehicle.acelerate(2)
    vehicle.brake(1)

car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)