'''
# Una clase no debería estar obligada a implementar interfaces que no utiliza. 
- Sirve para que se diseñen interfaces específicas para cada tipo de lógica. 
En lugar de una interface general con distintos tipos de métodos, que después las empezamos a asociar a cada clase

* Interface: Especie de contrato que debe seguir una clase. Especifica los métodos que debe implementar pero no se implementan en la interface
'''

# Importamos abstract basic class
from abc import ABC, abstractmethod


# Sin ISP
class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Human(WorkerInterface):

    def work(self):
        print("Trabajando.")

    def eat(self):
        print("Comiendo.")

class Robot(WorkerInterface):

    def work(self):
        print("Trabajando.")

    def eat(self):
        # Los robots no comen. Ya estamos violando el principio ISP
        pass


robot = Robot()
robot.eat() # Para nosotros es un error


# Con ISP
class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

class EatInterface(ABC):

    @abstractmethod
    def eat():
        pass

class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando.")

    def eat(self):
        print("Comiendo.")

class Robot(WorkInterface):

    def work(self):
        print("Trabajando.")

    # Ya no hay que meter la función eat 

'''
# EJERCICIO:
Crear un gestor de impresoras.
Requisitos:
1. Algunas impresoras solo imprimen en blanco y negro.
2. Otras solo a color.
3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
1. Implementa el sistema con los diferentes tipos de impresoras y funciones.
2. Aplica el ISP a la implementación.
3. Desarrolla un código que compruebe que se cumple el principio.
'''

class PrinterManager(ABC):
    @abstractmethod
    def printing_something(self):
        pass

class PrintInColour(ABC):
    @abstractmethod
    def using_colours(self):
        pass

class ScanInterface(ABC):
    @abstractmethod
    def scanning(self):
        pass

class FaxInterface(ABC):
    @abstractmethod
    def faxing(self):
        print("enviando fax.")

class BlackAndWhitePrinter(PrinterManager):
    def printing_something(self):
        print("Estoy imprimiendo en blanco y negro.")

class ColorPrinter(PrintInColour):
    def using_colours(self):
        print("Estoy imprimiendo a color.")

class MultifunctionPrinter(PrinterManager, PrintInColour, ScanInterface, FaxInterface):
    def printing_something(self):
        print("Estoy imprimiendo en blanco y negro.")

    def using_colours(self):
        print("Estoy imprimiendo a color.")

    def scanning(self):
        print("Estoy escaneando.")

    def faxing(self):
        print("Estoy enviando un fax.")

printer_b_and_w = BlackAndWhitePrinter()
printer_b_and_w.printing_something()


def test_printers():
    printer = BlackAndWhitePrinter()
    color_printer = ColorPrinter()
    multifunctionPrinter = MultifunctionPrinter()

    printer.printing_something()
    color_printer.using_colours()
    multifunctionPrinter.using_colours()
    multifunctionPrinter.faxing()
    multifunctionPrinter.printing_something()
    multifunctionPrinter.scanning()

test_printers()