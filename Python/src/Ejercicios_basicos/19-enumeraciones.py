from enum import Enum

'''
# Definición
Un Enum es una estructura especial en Python que te permite crear un conjunto de nombres fijos que no cambian.
Piensa en él como una lista cerrada de opciones predefinidas. En lugar de usar textos sueltos (strings) o números 
que pueden prestarse a errores de escritura, usas un Enum para agrupar esas opciones bajo un único tipo de dato.

# Uso común
Se utiliza siempre que un dato solo pueda tomar unos pocos valores específicos y conocidos de antemano. Por ejemplo:
Los días de la semana (Lunes, Martes...).
Los meses del año.
Los estados de un pedido (Pendiente, Enviado, Entregado).
- Así evitamos que enun sitio aparezca enviado y en otro Enviado, por ehemplo.

'''

# Para crear un enum en Python tenemos que crear una clase
class Weekday(Enum):
    # NOMBRE = valor
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THUESDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(number: int):
    print(f"Obejeto Weekday: {Weekday(number)}")
    print(f"Weekday (number).name: {Weekday(number).name}")
    print(f"Weekday (number).value: {Weekday(number).value}")

get_day(1)


'''
# DIFICULTAD EXTRA
Crea un pequeño sistema de gestión del estado de pedidos.
Implementa una clase que defina un pedido con las siguientes características:
- El pedido tiene un identificador y un estado.
- El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
- Implementa las funciones que sirvan para modificar el estado:
    * Pedido enviado
    * Pedido cancelado
    * Pedido entregado
    (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
- Implementa una función para mostrar un texto descriptivo según el estado actual.
- Crea diferentes pedidos y muestra como se interactúa con ellos.
'''

print("\n\n Extra \n")

class Status (Enum):
    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELED = 4


class Order:
    id = 0
    
    def __init__(self):
        self.id = Order.id
        Order.id += 1
        self.status = Status.PENDING
        print(f"Pedido #{self.id} creado con estado: {self.status.name}")

    def order_sent(self):
        if self.status == Status.PENDING:
            self.status = Status.SENT
            self.display_status()
        else:
            print(f"Error: Para enviar el pedido debe estar en estado pendiente y se encuentra: {self.status}")

    def order_delivered(self):
        if self.status == Status.SENT:
            self.status = Status.DELIVERED
            self.display_status()
        else:
            print(f"Error: Para enviar el pedido debe estar en estado pendiente y se encuentra: {self.status}")

    def order_canceled (self):
        if self.status != Status.DELIVERED:
            self.status = Status.CANCELED
            self.display_status()
        else:
            print(f"Error: el pedido {self.id} ya ha sido entregado, no puede cancelarse")

    def display_status(self):
        print (f"El estado del pedido {self.id} ha cambiado a estado: {self.status.name}")

    

order_one = Order()
order_two = Order()

order_one.order_sent()
order_one.order_sent()

order_two.order_canceled()

order_one.order_delivered()