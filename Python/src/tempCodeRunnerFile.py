def phone_book():
    my_phone_book: dict = {}
    # my_phone_book = {} # Mejor

    def insert_contact():
        name = input("\n - Introduce el nombre del conacto a añadir: ")
        if name in my_phone_book:
            print(f"El contacto {name} esta en la agenda y su teléfono es {my_phone_book[name]}")
        else:
            telephone = input(f" - Introduce el teléfono de {name}: ")
            my_phone_book[name] = telephone
            print ("\nContacto añadido correctamente")

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
                    print(f"\nEl contacto {name} esta en la agenda y su teléfono es {my_phone_book[name]}")
                else:
                    print(f"\nEl contacto {name} no está en la agenda. \nIntroduce la opción 2 si deseas añadirlo.")
            case "2":
                insert_contact()
            case "3": 
                pass
            case "4": 
                pass
            case "5": 
                for name in my_phone_book:
                    print(f"{name}: {my_phone_book[name]}")
            case "6":
                print("\nGracias por usar el programa. Nos vemos pronto.\n")
                break
            case _:
                print("Introduce una opción correcta (del 1 al 5).")


phone_book()
