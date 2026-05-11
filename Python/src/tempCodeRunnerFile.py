""" 
Modo,   Leer,   Escribir,   ¿Borra el contenido?,   ¿Crea si no existe?
r        ✅       ❌              No                     ❌ (Error)
w        ❌       ✅              SÍ                     ✅
a        ❌       ✅              No                     ✅
r+       ✅       ✅              No                     ❌ (Error)
"""


import os
print(os.getcwd())

file_name = "erpica.txt"



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
    file.seek(0) 
    file.write("prueba")