
# Incorrecto: Tiene dos responsabilidades: guarda en la base de datos y enviar mail

class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def save_to_database(self):
        pass

    def send_email(self):
        pass


# Correcto:
class UserOK:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class UserService:

    def save_to_database(self, user):
        pass

class EmailService:

    def send_email(self, email, message):
        pass

# EXTRA
'''
Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
manejar diferentes aspectos como el registro de libros, la gestión de usuarios
y el procesamiento de préstamos de libros.
Rquisitos:
1. Registrar libros: El sistema debe permitir agregar nuevos libros con
información básica como título, autor y número de copias disponibles.
2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
información básica como nombre, número de identificación y correo electrónico.
3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
tomar prestados y devolver libros.
Instrucciones:
1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje los tres aspectos y procesamiento de préstamos.
2. Refactoriza el código: Separa las responsabilidades en diferentes clases
siguiendo el Principio de Responsabilidad Única.
'''

class Library:

    def __init__(self):
        self.books = []
        self.users = []
        self.user_id = 0

    def register_book(self, title, author, copys):
        self.books.append({"title": title, "author": author, "copys": copys})

    def register_user(self, name, email):
        self.users.append({"name": name, "id": self.user_id, "email": email})
        self.user_id += 1

    def book_circulation(self, title, action):
        if action == "Borrow":
            have_any = False
            
            for book in self.books:
                if book["title"] == title:
                    have_any = True  # ¡Lo encontramos!
                    if book["copys"] >= 1:
                        book["copys"] -= 1  # CORREGIDO: Resta guardada con éxito
                        print(f"Se asigna el libro {book['title']}")
                    else:
                        print(f"En este momento no disponemos de ninguna copia de {book['title']}")
                    break  # Dejamos de buscar porque ya encontramos el título
            
            if have_any == False:
                print(f"No disponemos de ningún título llamado {title}")

    def show_books(self):
        print (self.books)

one_libray = Library()
one_libray.register_book("El Quijote", "Miguel de Cervantes", 1)
one_libray.register_book("Think Python", "Allen B. Downey", 2)

print("\nMostrando libros:")
one_libray.show_books()

one_libray.register_user("Anto", "anto@anto.anto")
one_libray.register_user("Pica", "pica@pica.pica")

print(f"\nUsuarios:{one_libray.users}")


print()
one_libray.book_circulation("El Quijote", "Borrow")



class NewLibrary:

    def __init__(self):
        self.books = []

    def register_book(self, title, author, copys):
        self.books.append({"title": title, "author": author, "copys": copys})

    def show_books(self):
        print (self.books)

class NewUsers:

    def __init__(self):
        self.users = []
        self.user_id = 0

    def register_user(self, name, email):
        self.users.append({"name": name, "id": self.user_id, "email": email})
        self.user_id += 1

class NewBookCirculation:

    def __init__(self, library: NewLibrary):
        self.library = library


    def book_circulation(self, title, action):
        if action == "Borrow":
            have_any = False
            
            for book in self.library.books:
                if book["title"] == title:
                    have_any = True  # ¡Lo encontramos!
                    if book["copys"] >= 1:
                        book["copys"] -= 1  # CORREGIDO: Resta guardada con éxito
                        print(f"Se asigna el libro {book['title']}")
                    else:
                        print(f"En este momento no disponemos de ninguna copia de {book['title']}")
                    break  # Dejamos de buscar porque ya encontramos el título
            
            if have_any == False:  # CORREGIDO: Uso de == para comparar
                print(f"No disponemos de ningún título llamado {title}")


print("\n\nNew Library")
# 1. Creamos las bases de datos independientes
biblioteca = NewLibrary()
gestion_usuarios = NewUsers()

# 2. Registramos libros y usuarios en sus respectivas clases
biblioteca.register_book("El Quijote", "Miguel de Cervantes", 1)
biblioteca.register_book("Think Python", "Allen B. Downey", 2)
gestion_usuarios.register_user("Anto", "anto@pica.es")

# 3. Creamos el gestor de préstamos INYECTANDO la biblioteca que creamos antes
gestor_prestamos = NewBookCirculation(biblioteca)

# 4. Probamos el sistema
print("--- Estado inicial de los libros ---")
biblioteca.show_books()

print("\n--- Procesando un préstamo ---")
gestor_prestamos.book_circulation("El Quijote", "Borrow")

print("\n--- Estado final de los libros (comprobando que bajó la copia) ---")
biblioteca.show_books()