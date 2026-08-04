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
# Otra forma menos moderna de llegar al path:
# import os
# print(f"{'os.getcwd():':<25} {os.getcwd()}")

from pathlib import Path
import subprocess

# Directorio padre del archivo con el que estoy trabajando:
#print(f"{'Path(__file__).parent:':<25} {Path(__file__).parent}")
current_directory = Path(__file__).parent
working_directory = current_directory / "github_folder"
#print(f"Ruta: {working_directory}")

# Comprueba si existe.
#print(working_directory.exists())

# Comprueba si es un archivo.
#print(working_directory.is_file())

# Comprueba si es una carpeta.
#print(working_directory.is_dir())

def establish_proyect_folder():
    #proyect_folder = input("Introduce el directorio de trabajo de tu proyecto: ")
    proyect_folder = "Prueba2"
    new_folder = working_directory / proyect_folder # creo el objeto en memoria de Python
    if new_folder.exists():
        pass
    else:
        new_folder.mkdir()         # Le digo a Windows que cree la carpeta
        print(f"Has creado correctamente el directorio de trabajo: {proyect_folder}")
    return new_folder

def execute_command(command): # Lo probaré para iniciar repositorio pero luego será solo para ejecutar comandos.
    #current_repository = input("Introduce el nombre del repositorio de tu proyecto: ")
    current_repository = "my_repository"
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    print("Salida: ", result.stdout)
    print("Error: ", result.stderr)
    print("Código: ", result.returncode)

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

    option = input("Introcuce una opción: ")

    match option:
        case "1":
            proyect_folder = establish_proyect_folder()
        case "2":
            execute_command("git init") # solo para probar
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
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            break






print("\n\n")

