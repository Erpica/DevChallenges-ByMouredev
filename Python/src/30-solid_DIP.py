'''
* El principio se divide en dos reglas fundamentales:
- Las clases de alto nivel (la lógica de tu negocio) no deben depender de las clases de bajo nivel 
(los detalles técnicos como la base de datos, las APIs o los frameworks). Ambas deben depender de abstracciones (interfaces o clases abstractas).
- Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.
'''

# Sin DIP:
# La clase Switch solo funcionará para la lámpara, el día de la mañana hay que crear uno para la tele, para el horno...
# Solo podemos evolucionar cambiando el código
class Switch:
    def turn_on(self):
        print("Enciende la lámpara")
    def turn_off(self):
        print("Apaga la lámpara")

class Lamp:
    def __init__(self):
        self.switch = Switch()

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp = Lamp()
lamp.operate("on")
lamp.operate("off")

# Con DIP

class AbstractSwitch:
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class LampSwitch(AbstractSwitch):
    def turn_on(self):
        print("Enciende la lámpara")
    def turn_off(self):
        print("Apaga la lámpara")

class Lamp:
    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        elif command == "off":
            self.switch.turn_off()

lamp = Lamp(LampSwitch())
lamp.operate("on")
lamp.operate("off")


'''
EXTRA:
Crea un sistema de notificaciones.
Requisitos:
1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
2. El sistema de notificaciones no puede depender de las implementaciones específicas.
Instrucciones:
1. Crea la interfaz o clase abstracta.
2. Desarrolla las implementaciones específicas.
3. Crea el sistema de notificaciones usando el DIP.
4. Desarrolla un código que compruebe el principio.
'''
from abc import ABC, abstractmethod

class NotificationSytem(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass

class EmailNotification(NotificationSytem):
    def send_message(self, message):
        self.message = message
        print(f"Email {self.message} enviado con éxito.")        

class PUSHNotification(NotificationSytem):
    def send_message(self, message):
        self.message = message
        print(f"PUSH {self.message} enviado con éxito.")      

class SMSNotification(NotificationSytem):
    def send_message(self, message):
        self.message = message
        print(f"SMS {self.message} enviado con éxito.")      

class NotificationService:
    def __init__(self, notifier: NotificationSytem) -> None:
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send_message(message)
        
#service = NotificationService(EmailNotification())
#service = NotificationService(PUSHNotification())
service = NotificationService(SMSNotification())
service.notify("Hola notificador")



