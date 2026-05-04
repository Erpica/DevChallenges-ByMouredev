
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