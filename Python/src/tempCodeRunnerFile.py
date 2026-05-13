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
                    if ((real_edit_option <= 0) or len(file_content(my_file) < real_edit_option)):
                        print("Introduce una opción correcta")
                        continue
                    break
                except Exception as e:
                    print("Introduce una opción correcta")

            the_product = the_lines [real_edit_option-1]
            data = the_product.split()
            print (f"Total del productu {data[0]} es: {float(data[1]) * float(data[2])}")