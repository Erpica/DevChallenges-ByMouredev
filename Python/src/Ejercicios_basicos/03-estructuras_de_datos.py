"""
Estructuras

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *

"""
import random

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
random.shuffle(my_list) # Deordenar random. Desordena la lista original
unsorted_list = random.sample(my_list, len(my_list)) # Crea una nueva lista desordenando la original. Hay que especificarle el tamaño.
print(my_list)
print(type(my_list))    # Enumerar los elementos de una lista:

random_number = random.randint(1,5) # Número aleatorio entre 1 y 5 (ambos inclusive)
print(random_number)



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
#Un diccionario en Python es una estructura de datos que almacena elementos en parejas de clave: valor.
'''
📋 Características principales
- Mutables: Puedes añadir, modificar o eliminar elementos después de crearlo.
- Claves únicas: No puede haber claves duplicadas (si repites una clave, el último valor machaca al anterior).
- Indexados por clave: En lugar de usar una posición numérica (como las listas), se accede a los datos a través 
de su clave.
- Ordenados: Mantienen el orden de inserción de los elementos.
- Métodos: keys(), values(), items(), update(), clear()
'''
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
print("    - items -")
print(type(my_dict.items()))
print(my_dict.items())
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

print(my_dict.get("name"))
print(my_dict.get("names"))
print(my_dict.get("names", "No está"))

# Creando un diccionario enumerando una lista:
#print({indice: valor for indice, valor in enumerate(my_list, start=1)})
my_list_again: list = ["Anto", "Brais", "Midu", "Trovalds"]
diccionario = {indice: valor for indice, valor in enumerate(my_list_again, start=1)}
print (diccionario)

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


#my_agenda_Brais()


"""  * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa. """

def phone_book():
    my_phone_book: dict = {}
    # my_phone_book = {} # Mejor

    def insert_contact():
        name = input("\n - Introduce el nombre del conacto a añadir: ")
        if name in my_phone_book:
            print(f"El contacto {name} esta en la agenda y su teléfono es {my_phone_book[name]}")
        else:
            telephone = input(f" - Introduce el teléfono de {name}: ")
            # * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
            if (telephone.isdigit and telephone.len > 11):
                my_phone_book[name] = telephone
                print ("\nContacto añadido correctamente")
            else:
                print("\nEl teléfono es erróneo, debe ser numérico y de 11 dígitos")

    while True:
        print('''
                    ##########################
                    #    Agenda de ErPica    #
                    #  --------------------  #
                    # 1. Buscar contacto     #
                    # 2. Insertar contacto   #
                    # 3. Actualizar contacto #
                    # 4. Eliminar contacto   #
                    # 5. Mostrar contactos   #
                    # 6. Salir               #
                    ########################## 
        ''')

        option = input("\nIntroduce una opción: ")

        match option:
            case "1":
                name = input("\nIntroduce el nombre del contacto a buscar: ")
                if name in my_phone_book:
                    print(f"\n\nEl contacto {name} esta en la agenda y su teléfono es {my_phone_book[name]}")
                else:
                    print(f"\nEl contacto \"{name}\" no está en la agenda. \nIntroduce la opción 2 si deseas añadirlo.")
            case "2":
                insert_contact()
            case "3": 
                name = input("\nIntroduce el nombre del contacto a buscar: ")
                if name in my_phone_book:
                    my_phone_book[name] = input(f"Introduce el teléfono de {name}: ")
                else:
                    print(f"\nEl contacto \"{name}\" no está en la agenda. \nIntroduce la opción 2 si deseas añadirlo.")
            case "4": 
                name = input("\nIntroduce el nombre del contacto a buscar: ")
                if name in my_phone_book:
                    del(my_phone_book[name])
                    print(f"\nEl contacto {name} ha sido eliminado correctamente.")
                else:
                    print(f"\nEl contacto \"{name}\" no está en la agenda.")
                
            case "5": 
                for name in my_phone_book:
                    print(f"\n{name}: {my_phone_book[name]}")
            case "6":
                print("\nGracias por usar el programa. Nos vemos pronto.\n")
                break
            case _:
                print("Introduce una opción correcta (del 1 al 5).")


phone_book()

""" 
other_phone_book = {
    "Anto": "999999999",
    "Pic": "666666666"
}
name ="Anto"
if name in other_phone_book:
    print(name + ": " + other_phone_book[name])
else:
    print("No") """













