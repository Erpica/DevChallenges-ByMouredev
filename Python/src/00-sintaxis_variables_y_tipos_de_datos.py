'''
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 '''

# URL del sitio web oficial de Python: https://www.python.org/
# Comentario de una línea

"""
Comentario de varias líneas
"""

'''
Otro comentario de varias líneas
'''

# Variable
my_var =  "Hola, soy una variable"


# Constante
MY_CONST = "Hola, soy una constante"


# Tipos de datos primitivos
'''
"tipos de datos primitivos" no es una categoría formal en la documentación de Python. 
En su lugar, se habla de "tipos incorporados" (built-in types)
'''
my_integer = 42
my_float = 3.14
my_complex = 1 + 2j #  Número complejo con partes real e imaginaria (flotantes) 
my_boolean = True
my_string = "Hola, soy una cadena de texto"
my_tuple = (1, 2, 3) # Tupla, una colección ordenada e inmutable
my_none_type = None # Representa la ausencia de valor

my_lenguaje = "Python"
print(f"¡Hola, {my_lenguaje}!")