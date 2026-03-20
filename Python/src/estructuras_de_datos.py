"""
Estructuras
"""

# Listas
my_list: list = ["Anto", "Brais", "Midu", "Trovalds"]
print(my_list)
my_list.append("Guido")  # Inserción
my_list.append("Guido")
print(my_list)
my_list.remove("Midu")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "GuidoPython"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Anto", "Erpica", "@erpica", "45")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Anto", "Erpica", "@erpica", "45"}
print(my_set)
my_set.add("anto@erpica.es")  # Inserción
my_set.add("anto@erpica.es")
print(my_set)
my_set.remove("Anto")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
    "name": "Anto",
    "surname": "Erpica",
    "alias": "@Antodev",
    "age": "45"
}
my_dict["email"] = "Antodev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

"""
Extra
"""


def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El nÃºmero de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()