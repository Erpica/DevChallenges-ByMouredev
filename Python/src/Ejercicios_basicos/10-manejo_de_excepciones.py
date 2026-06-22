
try:
    #print(10/0)

    my_list = [1, 2, 3, 4]
    print(my_list[4])
except Exception as e:
    print(f"Se ha producido un error {e}\n\n")

try:
    print(10/1)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error, descripción: {e} (y tipo: {type(e).__name__})")

'''
# Extra
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.

'''

class Personaliced_error(Exception):
    print ("Mi error presonalizado")

def parameter_function (num1: int, num2: int):
    result = num1/num2
    my_list = num1, num2
    item = my_list[5]

    if (num1 == num2):
        raise Personaliced_error("Mensaje: Los números son iguales")

    print("La función se ha ejecutado correctamente")

try:
    parameter_function(4, 0)
except ZeroDivisionError:
    print(f"No se puede dividir por cero")
except IndexError:
    print(f"No se puede acceder al elemento")
except Personaliced_error:
    print ("Mi error presonalizado")
else: 
    print("No se encontraron errores.")
finally:
    print("Ejercicio completado")



# Extra por Brais:


class StrTypeError(Exception):
    pass

def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError("Se necesitan al menos 3 parámetros.")
    elif parameters[1] == 0:
        raise ZeroDivisionError("El segundo parámetro no puede ser cero.")
    elif type(parameters[2]) == str:
        raise StrTypeError("Excepción personalizada: El tercer parámetro no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1, 2, "hola", 2])
except IndexError as e:
    print(f"Error de índice: {e}")
except ZeroDivisionError as e:
    print(f"Error de división por cero: {e}")
except StrTypeError as e:
    print(f"Error personalizado: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("La función se ejecutó sin errores.")
finally:
        print("Ejecución finalizada.")