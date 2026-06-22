import re

def find_numbers(text: str) -> list:
    # Así podríamos llegar a ello:
    # return re.findall(r"[0-9]+", text)
    # Pero ya hay una para los números:
    return re.findall(r"\d+", text)

print(find_numbers("Este es el ejercicio 16 realizado el 16/05/2026."))



# Practicando un poco


'''
# Metacaractéres:
- "." -> Cualquier carácter individual (como letra, número, símbolo o espacio), excepto un salto de línea. Ej: "ca.a" -> casa, cama, caja, ca3a...
- []  -> Si no me vale cualquier carácter, puedo meter dentro un grupo específico (o un rango con guión en medio). Ej p[ae]lo -> palo y pelo (pero no polo). También [0-9] o [a-z]
- {}  -> Es un cuantificador. Es lo mismo [0-9][0-9][0-9] que [0-9]{3}. Si no pongo nada (ni las llaves si quiera) es 1
- {}  -> Rango explícito {min, max}. Entre dos y cuatro letras minúsculas de la a a la z: [a-z]{2,4}. Importante: Aquí no se puede poner espacio {2, 4} interpreta como que busque un espacio.
- ()  -> Agrupa una parte del patrón y se aplica, por ejemplo, un cuantificador a todo el conjunto.
- "$" -> Dice "y aquí finaliza". Ej: [a-z][0-9] -> encuentra la coincidencia en a3 y en a55. Si es [a-z][0-9]$ ya no vale el a55
- "^" -> Dice "aquí empieza". Ej: [a-z][0-9]$ -> encuentra a0 y aa0. Si es ^[a-z][0-9]$ ahora si empieza por una sola letra, luego un solo número y nada más.
- "*" -> Cero o más veces
- "+" -> Una o más veces
- "|" -> Fuera de los corchetes es un OR pero dentro es literalmente el carácter "|". Para decir mayúsculas o minúsculas es [a-zA-Z]
- Secuencias de escape o atajos (no hay que meterlos en corchetes. Ej: r"^\w*$):
    - \d -> dígito: [0-9]
    - \w -> palabra: [a-zA-z0-9_]
    - \s -> Cualquier espacio en blanco, tabulador (\t) o salto de línea (\n)
- Modificadores o flags (re.IGNORECASE, re.MULTILINE, re.DOTALL, re.VERBOSE):
    - re.IGNORECASE o re.I: Ignora mayúsculas y minúsculas.
    - re.MULTILINE o re.M: Cambia el comportamiento de ^ y $ para que coincidan con el inicio y el final de cada línea, en lugar de solo el inicio y el final de toda la cadena.
    - re.DOTALL o re.S: Permite que el metacarácter "." coincida con cualquier carácter, incluyendo saltos de línea.
    - re.VERBOSE o re.X: Permite escribir expresiones regulares más legibles al permitir espacios en blanco y comentarios dentro del patrón.
- Valores literales: Se escriben con una barra invertida. Por ejemplo: "\." para buscar un punto.
    


# Funciones más utilizadas del módulo re:
Función                             ¿Qué hace?                                                      ¿Qué devuelve?
re.search(patron, texto)            Busca el patrón en CUALQUIER PARTE del texto.                   El PRIMER OBJETO coincidencia (Match) que encuentra, o None.
re.match(patron, texto)             Busca el patrón solo al PRINCIPIO del texto.                    UN OBJETO Match si empieza ahí, o None.
re.findall(patron, texto)           Busca TODAS las coincidencias en el texto.                      Una LISTA de cadenas con los textos encontrados.
re.finditer(patron, texto)          Busca TODAS las coincidencias de forma eficiente.               Un ITERADOR con objetos Match (ideal para bucles for).
re.sub(patron, reemplazo, texto)    REEMPLAZA las coincidencias encontradas por un texto nuevo.     Una nueva CADENA de texto modificada.
re.split(patron, texto)             DIVIDE el texto usando el patrón como separador.                Una LISTA de cadenas de texto.


















'''

import re

texto = "El gato toma leche."
patron = "g[aeiou]to"  # Busca 'g', luego una vocal, luego 'to'

if re.search(patron, texto):
    print("¡Coincidencia encontrada! 🐾")
else:
    print("No se encontró el patrón. ❌")


# Devuelve una clase
print (type(re.search(patron, texto)))


product_code = "F50"
regex = r"^[A-Z]{1}[0-9]*$"

if re.search(regex, str(product_code)):
    print("Encontrado")
else:
    print("No válido")


regex_user_name = r"^[a-zA-Z]\w*$"

# El flag re.IGNORECASE hace el trabajo por nosotros para no tener que poner [a-zA-Z]
regex = r"^[a-z]\w*$"
if re.search(regex, "Usuario_123", re.IGNORECASE):
    print("¡Nombre de usuario válido! 👤")



















'''
# Extra:
Crea tres expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una URL.


'''

# Validad un email:
'''
- Entre 6 y 30 caracteres (parte local)
- Solo letras, números y puntos
- Solo una @ (tras la parte local)
'''
email = "erpica@gmail.com"

def check_email(email: str) -> None:
    regex_check_email = r"^[\w]{6,30}@[\w]+\.\w{2,8}$"
    # By Brais:
    # r"[\w.+-]+@[\w]+\.[a-zA-z]+" # permite antes de la @ el . el + y el -
    if re.match (regex_check_email, email):
        print("Email válido")
    else:
        print("Email no válido")


check_email(email)

def validate_telephone_number (telephone_number: str) -> bool:
    if re.match(r"^\d{9}$", telephone_number):
        # By Brais:
        # r"^\+?\d\s{3,}$" # {3,} dice mínimo 3 dígitos, por si te llaman de un número super largo. El \s por si lo escribe 901 90 90 90. +? -> el más cero o una vez (es decir, opcional)
        return True
    else:
        return False

if validate_telephone_number(str(956222000)):
    print("Teléfono ok")
else:
    print("Teléfono incorrecto")

def url_validator (url: str) -> bool:
    if re.match(r"^\w{2,63}\.\w+(\.\w+){0,3}$", url):
        # By Brais:
        # r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$" -> La s es opcional [s]?
        return True
    else:
        return False

if url_validator("erpica.es.yo.re"):
    print("URL OK")
else: 
    print ("URL KO")