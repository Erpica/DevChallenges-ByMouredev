""" 
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
 """

class User:
    list_of_users = []
    ID = 0
    def __init__(self, username):
        self.username = username
        User.list_of_users.append({"username": username})
        User.ID += 1


while True:
    
    print('''
    \n\n
            ##########################################################
            |            Welcome to Bluesky_Pic.                     |
            ----------------------------------------------------------
            |   1 - Crear cuenta / acceder.                          |
            |   2 - + Seguir.                                        |
            |   3 - Crear un post.                                   |
            |   4 - Eliminar un post.                                |
            |   5 - Like.                                            |
            |   6 - Publicaciones de un usuario.                     |
            |   7 - Publicaciones de los que sigue un usuario.       |
            |   8 - Sair.                                            |
            ##########################################################
    ''')

    option = input ("Introduce una de las opciones para interactuar con la app:")

    match option:
        case "1":
            one_user = User("pica")
            print(one_user.ID, one_user.username)
            other_user = User("anto")
            print(other_user.ID, other_user.username)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            print("Gracias por usar el programa.")
            break
        case _:
            print("Introduce una opción correcta.\n")

