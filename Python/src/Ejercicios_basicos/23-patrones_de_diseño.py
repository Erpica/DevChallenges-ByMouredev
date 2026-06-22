# Es una manera de resolver problemas o necesidades comunes
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

print(singleton1 is singleton2)

'''
# EXTRA
Utiliza el patrón de diseño "singleton" para representar una clase que
haga referencia a la sesión de usuario de una aplicación ficticia.
La sesión debe permitir asignar un usuario (id, username, nombre y email),
recuperar los datos del usuario y borrar los datos de la sesión.
'''

class Session_Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Session_Singleton, cls).__new__(cls)
            cls._instance.id = None
            cls._instance.username = None
            cls._instance.name = None
            cls._instance.email = None
        return cls._instance
    
    def asign_user(self, id: int, username: str, name: str, email: str):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def show_user_data(self):
        if self.id == None:
            print("No se ha iniciado la sesión.")
        else:
            print(f"Id: {self.id}\nNombre de usuario: {self.username}\nNombre: {self.name}\nEmail: {self.email}")

    def erase_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
        print("Datos borrados correctamente")


# session_singleton11 = Session_Singleton # Esto solo crearía un alias. No crea el objeto
# session_singleton12 = Session_Singleton() # al poner los paréntesis si llama a new y crea el objeto
# Al crear un objeto siempre hace el __new__ antes del __init__ solo lo usamos para singleton

app_login = Session_Singleton()
app_login.asign_user(1, "erpica", "Anto", "anto@pica.es")

app_perfil = Session_Singleton()
app_perfil.show_user_data()

app_perfil.erase_user()
app_login.show_user_data()


