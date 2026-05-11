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
    file.seek(0) # al estar abierto con "a" añade al final independientemente de donde está el puntero
    file.write("prueba")

with open(file_name, "r") as file:
    print(file.readlines())




if os.path.exists(file_name):
    print("Sí existe el archivo")

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


print("Ejercicios con Path")
print(os.path.exists(file_name))
print(os.path.exists("Python/src/manejo_de_ficheros/prueba.txt"))
os.remove(file_name)
print(os.path.exists(file_name))

# Extra:
'''
Desarrolla un programa de gestión de ventas que almacene sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
[nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, 
actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
'''

sales_file = "Python/src/manejo_de_ficheros/sales_file.txt"

def file_content (file: str) -> bool | list:
    try:
        with open(file, "r") as try_file_exists:
            return try_file_exists.readlines()
    except Exception as e:
        return False


print ("Bienvenido a CRM-PICA")
while True:
    print ("########################")
    print ("#    CRM - PICA        #")
    print ("#    ----------        #")
    print ("#   1. Añadir          #")
    print ("#   2. Consultar       #")
    print ("#   3. Actualizar      #")
    print ("#   4. Eliminar        #")
    print ("#   5. Salir           #")
    print ("########################")
    option = input("Introduce un número del menú: ")
    try:
        real_option = int(option)
    except Exception as e:
        print(f"Has introducido {option}. Debes introducir un número del 1 al 5\n\n")
        continue
    else:
        pass
    match real_option:
        case 1:
            product_name = input("Introduce el nombre del producto a añadir: ")
            amount_product_solds = input("Introduce la cantidad de productos vendidos: ")
            price_product_sold = input("Introduce su precio: ")
            product_complete = (product_name + " " + amount_product_solds + " " + price_product_sold + "\n")
            with open(sales_file, "a") as my_file:
                my_file.write(product_complete)
        
        case 2:
            print (f"Has introducido 2")
            with open(sales_file, "r") as my_file:
                my_file.seek(0)
                the_lines = (my_file.readlines())
                if not the_lines:print("El archivo está vacío")
                else:
                    for line in the_lines:
                        print(line.strip())
                        # print(f"Producto: {line[0]}, cantidad: {line[1]} y precio: {line[2]}")

        case 3:
            print (f"Has introducido 3")
            with open(sales_file, "r") as my_file:
                my_file.seek(0)
                the_lines = (my_file.readlines())
                if not the_lines:print("El archivo está vacío")
                else:
                    i = 1
                    for line in the_lines:
                        print(f"{i}: {line.strip()}")
                        i += 1
            edit_option = input("Introduce la opción del producto a editar: ")
            real_edit_option = int(edit_option)
            # Pedimos los datos del producto a editar
            product_name = input("Introduce el nombre del producto a editar: ")
            amount_product_solds = input("Introduce la cantidad de productos vendidos: ")
            price_product_sold = input("Introduce su precio: ")
            product_complete = (product_name + " " + amount_product_solds + " " + price_product_sold + "\n")
            a = 1
            the_lines[real_edit_option-1] = product_complete
            with open (sales_file, "w") as my_file:
                my_file.writelines(the_lines)
                print("Producto actualizado con éxito")

        case 4:
            print (f"Has introducido 4")
            with open(sales_file, "r") as my_file:
                my_file.seek(0)
                the_lines = (my_file.readlines())
                if not the_lines:print("El archivo está vacío")
                else:
                    i = 1
                    for line in the_lines:
                        print(f"{i}: {line.strip()}")
                        i += 1
            remove_option = input("Introduce la opción del producto a eliminar: ")
            real_remove_option = int(remove_option)
            if(real_remove_option < i):
                the_lines.pop(real_remove_option-1)
                with open (sales_file, "w") as my_file:
                    my_file.writelines(the_lines)
                    print("Producto eliminado con éxito")
            else:
                print("El producto que intentas borrar no existe")


            
        case 5:
            break
        case _:
            print(f"Has introducido {option}. Debes introducir un número del 1 al 5\n\n")
            

print("Gracias por usar el programa")



