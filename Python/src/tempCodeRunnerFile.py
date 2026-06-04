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
        
service = NotificationService(EmailNotification())
service.notify("Hola notificador")
