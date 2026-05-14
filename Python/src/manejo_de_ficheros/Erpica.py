import os

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
    print ("############################")
    print ("#    CRM - PICA            #")
    print ("#    ----------            #")
    print ("#   1. Añadir              #")
    print ("#   2. Consultar           #")
    print ("#   3. Actualizar          #")
    print ("#   4. Eliminar            #")
    print ("#   5. Venta por producto  #")
    print ("#   6. Venta total         #")
    print ("#   7. Salir               #")
    print ("############################")
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
            try:
                with open(sales_file, "r") as my_file:
                    my_file.seek(0)
                    the_lines = (my_file.readlines())
                    if not the_lines:print("El archivo está vacío")
                    else:
                        for line in the_lines:
                            a_product = line.split()
                            #print(line.strip())
                            print(f"Producto: {a_product[0]}, cantidad: {a_product[1]} y precio: {a_product[2]}")
            except Exception as e:
                print("Primero debes crear el archivo")

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
            while True:
                edit_option = input("Introduce el número del producto a editar: ")
                try:
                    real_edit_option = int(edit_option)
                    if ((real_edit_option <= 0) or len(file_content(my_file) < real_edit_option)):
                        print("Introduce una opción correcta")
                        continue
                    break
                except Exception as e:
                    print("Introduce una opción correcta")
                

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

        case 5: #Suma de un producto
            sum = 0
            print (f"Has introducido 5")
            with open(sales_file, "r") as my_file:
                my_file.seek(0)
                the_lines = (my_file.readlines())
                if not the_lines:print("El archivo está vacío")
                else:
                    i = 1
                    for line in the_lines:
                        print(f"{i}: {line.strip()}")
                        i += 1
            edit_option = 0
            while True:
                edit_option = input("Introduce el número del producto a editar: ")
                try:
                    real_edit_option = int(edit_option)
                    if ((real_edit_option <= 0) or (len(the_lines) < real_edit_option)):
                        print("Introduce una opción correcta")
                        continue
                    break
                except Exception as e:
                    print("Introduce una opción correcta")

            the_product = the_lines [real_edit_option-1]
            data = the_product.split()
            print (f"Total del productu {data[0]} es: {float(data[1]) * float(data[2])}")

        case 6: #Suma de todo
            sum = 0
            with open (sales_file, "r") as my_file:
                for a_line in my_file.readlines():
                    #print(type(a_line))
                    the_product = (a_line.split())
                    #print (the_product)
                    the_product = int(the_product[1]) * float(the_product [2])
                    sum += the_product
            print (f"La suma total asciende a: {sum} €")
            

            
        case 7:
            os.remove(sales_file)
            break


        case _:
            print(f"Has introducido {option}. Debes introducir un número del 1 al 5\n\n")
            

print("Gracias por usar el programa")

""" 
#########################################################################################################
file_name = "Python/src/manejo_de_ficheros/Erpica.txt"
open(file_name, "a")



# Extra por Brais:

while True:
    print("\n\n\n1. Añadir un producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Calcular venta total")
    print("6. Añadir un producto")
    print("7. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        name = input("Nombre: ")
        quantity = input ("Cantidad: ")
        price = input ("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
    elif option == "2":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Nombre: ")
        quantity = input ("Cantidad: ")
        price = input ("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
                    
    elif option == "4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())
    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(line.split(", ")[1])
                price = float(line.split(", ")[2])
                total += quantity * price
            print(total)
    elif option == "7":
        os.remove(file_name) # Esto, para hacer las pruebas se comenta
        break
    else:
        print ("Debes introducir una opción correcta.")
 """