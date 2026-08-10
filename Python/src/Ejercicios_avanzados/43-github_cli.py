'''
EJERCICIO:
¡Me voy de viaje al GitHub Universe 2024 de San Francisco!

Desarrolla un CLI (Command Line Interface) que permita
interactuar con Git y Github de manera real desde terminal.

El programa debe permitir las siguientes opciones:
1. Establecer el directorio de trabajo
2. Crear un nuevo repositorio
3. Crear una nueva rama
4. Cambiar de rama
5. Mostrar ficheros pendientes de hacer commit
6. Hacer commit (junto con un add de todos los ficheros)
7. Mostrar el hitorial de commits
8. Eliminar rama.
9. Establecer repositorio remoto
10. Hacer pull
11. Hacer push
12. Salir

Notas: Todo irá dentro de github_folder
'''


from pathlib import Path
import subprocess
import os

current_directory = Path(__file__).parent
working_directory = current_directory / "github_folder"
os.chdir(working_directory)


def establish_proyect_folder():
    '''
    Comprueba si la carpta está creada (siempre dentro de "github_folder").

    Si está creada va a la carpeta superior a esa carpeta y, si no , 
    la crea y entra en la carpeta superior a ella.
    '''
    #proyect_folder = input("Introduce el directorio de trabajo de tu proyecto: ")
    proyect_folder = "prueba" # Mientras programo evito el input
    new_folder = working_directory / proyect_folder # creo el objeto en memoria de Python
    if new_folder.exists():
        print("-----------")
        print(f"\nEl directorio {new_folder} ya existe.")
    else:
        #print(f"Path: {Path.cwd()}")
        new_folder.mkdir()         # Le digo a Windows que cree la carpeta
        print(f"Has creado correctamente el directorio de trabajo: {proyect_folder}")
        os.chdir(new_folder.parent)
        #print(f"Path: {Path.cwd()}")
        #execute_command(["cd", proyect_folder])
    return new_folder

def execute_command(command):
    '''
    Recibe un comando como un str o como una lista si consta de varias palabras.
    
    Devuelve solo la salida. 
    '''
    #current_repository = input("Introduce el nombre del repositorio de tu proyecto: ")
    current_repository = "my_repository" # De momento evito el input
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout.split())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


while True:
    print('''
    \t\t------------------------------------------
    \t\t|  Bienvenido al CLI de GitHub de ErPica |
    \t\t------------------------------------------

    \t\t1. Establecer el directorio de trabajo
    \t\t2. Crear un nuevo repositorio
    \t\t3. Crear una nueva rama
    \t\t4. Cambiar de rama
    \t\t5. Mostrar ficheros pendientes de hacer commit
    \t\t6. Hacer commit (junto con un add de todos los ficheros)
    \t\t7. Mostrar el hitorial de commits
    \t\t8. Eliminar rama.
    \t\t9. Establecer repositorio remoto
    \t\t10. Hacer pull
    \t\t11. Hacer push
    \t\t12. Salir
    ''')
    try:
        proyect_folder
        print(f"Estás en el directorio de trabajo: {proyect_folder}\n")
    except NameError:
        print(f"Estás en el directorio de trabajo: {working_directory}\n")

    option = input("Introduce una opción: ")

    match option:
        case "1":
            #print("Has elegido la opción 1")
            proyect_folder = establish_proyect_folder()
            
        case "2":
            print("\n\n")
            #current_repository = input("introduce el nombre del nuevo repositorio")
            current_repository = "prueba"
            if Path.exists("prueba"):
                pass
            else:
                print(f"Se ha creado la carpeta y el repositorio {current_repository}.")
            print("-----------")
            execute_command(f"git init {current_repository}")
            
        case "3":
            print("-----------")
            #new_branch = input("Introduce el nombre de la rama")
            new_branch = "feature1"
            execute_command(f"git branch {new_branch}")

        case "4":
            print("-----------")
            new_branch = "feature1"
            execute_command(f"git switch {new_branch}")
            
        case "5":
            print("-----------")
            execute_command("git status")
            
        case "6":
            print("-----------")
            execute_command("git add .")
            print("Guardando ficheros...\n")
            #message = input("Introduce el mensage para el commit")
            message = "Mensaje de prueba"
            execute_command(f'git commit -m "{message}"')
            

        case "7":
            print("-----------")
            execute_command("git log --online")
            
        case "8":
            print("-----------")
            #delete_branch = input("Introduce el nombre de la rama a eliminar: ")
            delete_branch = "feature1"
            execute_command(f"git branch -d {delete_branch}")
        case "9":
            print("-----------")
            #url_remote = input("Introduce la URL remota: ")
            remote_url = "https://example.com"
            execute_command(f"git remote remove origin")
            execute_command(f"git remote add origin {remote_url}")
            execute_command(f"git push -u origin main")

        case "10":
            print("-----------")
            execute_command("git pull")

        case "11":
            print("-----------")
            execute_command("git push")
            
        case "12":
            break
        case _:
            print("Introduce una opción correcta.")






print("\n\n")




'''
Notas:
# Otra forma menos moderna de llegar al path:
# import os
# print(f"{'os.getcwd():':<25} {os.getcwd()}")

# Comprueba si existe.
#print(working_directory.exists())

# Comprueba si es un archivo.
#print(working_directory.is_file())

# Comprueba si es una carpeta.
#print(working_directory.is_dir())

# Directorio padre del directorio en el que estoy trabajando:
#print(f"{'Path(__file__).parent:':<25} {Path(__file__).parent}")
'''