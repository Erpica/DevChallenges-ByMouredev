""" 
Modo,   Leer,   Escribir,   ¿Borra el contenido?,   ¿Crea si no existe?
r        ✅       ❌              No                     ❌ (Error)
w        ❌       ✅              SÍ                     ✅
a        ❌       ✅              No                     ✅
r+       ✅       ✅              No                     ❌ (Error)
"""

'''
🗝️ Claves para manejar rutas en Python
Usa la librería pathlib 🛠️: Es el estándar moderno en Python. En lugar de unir textos con barras / o \, usas el operador / entre objetos Path, lo cual funciona en cualquier sistema operativo (Windows, Linux, Mac).
Basa las rutas en la ubicación del archivo (__file__) 🎯: La variable especial __file__ representa la ubicación de tu script actual. Si usas Path(__file__).parent, Python siempre sabrá dónde está el script, sin importar desde qué carpeta abras la terminal.
Crea carpetas automáticamente 📂: Con el método .mkdir(parents=True, exist_ok=True), le pides a Python que cree las carpetas intermedias si no existen antes de intentar guardar algo.
Ejemplo de cómo construir la ruta usando pathlib:

from pathlib import Path

# Obtiene la carpeta donde está este script (.py)
BASE_DIR = Path(__file__).parent 
print(f"Directorio Base:\n{BASE_DIR}\n")

# Construye la ruta final sin importar desde dónde ejecutes la terminal
#my_zip_file = BASE_DIR / "my_file.zip"

'''

import os
print(f"getcwd(): {os.getcwd()}")

file_name = "erpica.txt"


# with open (file_name, "w", encoding="utf-8") as file: # => Podría solucionar el tema de las tildes
try:
    with open(file_name, "r") as file:
        print(len(file.readlines()))
        print(len(file.readlines()))
        file.seek(0) 
        print(len(file.readlines()))
except Exception as e:
    print("El fichero no existe")



with open(file_name, "w") as file:
    file.write("Anto\n")
    file.write("46\n")
    file.write("Python\n")

with open(file_name, "a") as file:
    file.seek(0) # al estar abierto con "a" añade al final independientemente de donde está el puntero
    file.write("prueba")

print("\nReadlines:")
with open(file_name, "r") as file:
    print(file.readlines())




if os.path.exists(file_name):
    print("\nSí existe el archivo")

with open(file_name, "r") as file:
    print(f"type(file.readlines()): {type(file.readlines())}")  # Readlines se usa siempre sin argumentos, devuelve una lista con cada línea del archivo como un elemento de la lista
    file.seek(0) # porque el readlines de antes dejó el cabezal al final. Si no pongo esto no devuelve ninguna línea
    print(f"file.readlines(): {file.readlines()}")
    file.seek(0) # porque el readlines de antes dejó el cabezal al final. Si no pongo esto no devuelve ninguna línea
    the_list_of_lines = file.readlines()
    lines_ok = []
    for line in the_list_of_lines:
        lines_ok.append(line.strip())
    print (lines_ok)

    # Para solo leer una línea:
    file.seek(0)
    print(f"readline(): {file.readline()}")

""" 
# Así me cargo lo que haya de antes:
with open(file_name, "w") as file:
    file.write("Antonio\n") """
    
with open(file_name, "r") as file:
    print(file.readlines())


with open(file_name, "r") as file:
    total_lines = sum(1 for lines in file)
print (f"Número de líneas: {total_lines}")


print("\nEjercicios con Path")
print(os.path.exists(file_name))
print(os.path.exists("Python/src/manejo_de_ficheros/prueba.txt"))
os.remove(file_name)
print(os.path.exists(file_name))



