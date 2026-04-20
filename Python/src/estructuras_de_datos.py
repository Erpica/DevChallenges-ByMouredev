"""
Estructuras

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *

"""

# Listas []
print("Listas:")
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

# Tuplas (): Inmutables, cuando la creo ya se lo que va a tener
print("\nTuplas:")
my_tuple: tuple = ("Anto", "Erpica", "@erpica", "45")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación: sorted devuelve una lista y todos sus elementos tienen que ser del mismo tipo
print(my_tuple)
print(type(my_tuple))

# Sets {}: Desordenados, sin duplicados
print("\nSets:")
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
print("\nDiccionario:")
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


def my_agenda_Brais():

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
                        f"El número de teléfono de {name} es {agenda[name]}.")
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


#my_agenda()


"""  * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa. """

def my_agenda_Pic():
    my_agenda: dict = {}

    print('''

                ##########################
                #    Agenda de ErPica    #
                #  --------------------  #
                # 1. Buscar contacto     #
                # 2. Insertar contacto   #
                # 3. Actualizar contacto #
                # 4. Eliminar contacto   #
                # 5. Salir               #
                ##########################
        
    ''')

    option = input("\nIntroduce una opción: ")
    def search_contact():
        contact = input("Introduce el nombre del conacto a buscar: ")
        for one_conctact in my_agenda.values:
            if one_conctact == contact:
                print (f"El contacto {contact} sí está en la agenda")
                break
            print (f"El contacto {contact} no está en la agenda")

    def insert_contact():
        contact = input("Introduce el nombre del conacto a añadir")
        for one_conctact in my_agenda["name"]:
            if one_conctact == contact:
                print (f"El contacto {contact} ya está en la agenda")
                break
        telephone = input("Introduce el teléfono del conacto a añadir")
        my_agenda["name"] = contact
        my_agenda["telephone"] = telephone

    def update_contact():
        pass

    def delete_contact():
        pass


    match option:
        case "1":
            search_contact()
        case "2":
            insert_contact()
        case "3": 
            update_contact()
        case "4": 
            delete_contact()
        case "5":
            print("\nGracias por usar el programa. Nos vemos pronto.\n")
        case _:
            print("Introduce una opción correcta (del 1 al 5).")


my_agenda_Pic()












