'''
Operaciones:

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
'''

s1 = "Hola"
s2 = "Python"
s3 = "Mi nombre es Anto, ErPica"
s4 = "Anto Pic @erpica.es"

# Concaternación
print(s1 + ", " + s2 + "!")

# Repetición
print (s1 + s1 + s1)
print (s1 * 3)

# Idenxación
print(s1[0] + s1[1]+ s1[2]+ s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:5])
print(s2[2:])
print(s2[:2])

# Búsqueda
print("a" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas y minúsculas
print(s1.upper())
print(s1.lower())
print(s3.title())
print(s3.capitalize())

# Eliminación de espacios al principio y al final
print(" Er Pica ".strip())

# Búsqueda al principio y al final
print (s1.startswith("Ho"))
print (s1.endswith("Ho"))

# Búsqueda de posición
print("Anto Pic @erpica.es".find("Pic"))

# Búsqueda de ocurrencias
print(s3.lower().count("a"))

# Formateo e interpolación
print("Saludo: {}, lenguaje: {}!".format(s1, s2))
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
s5 = [s1, ", ", s2, "!"]
print("-".join(s5))
print("".join(s5))

# Transformaciones numéricas
s4 = "123456"
s4= int(s4)
print(s4)

# Comprobaciones varias
print(s1.isalnum())
print(s1.isalpha())
print(s1.isnumeric())

# reverse: le da la vuelta a la lista original
# list2 = list(reversed(list1)) => le doy la vuelta y la meto en la variable list2 pero dejo intacta la original
# list2 = list1[::-1] = la mejor forma de darle la vuelta

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas: mismas letras, diferente orden
 * - Isogramas: palabra en la que no se repite ninguna letra
 */
'''

# string1 = input(" - Introduce una palabra: ")
# string2 = input(" - Introduce otra palabra: ")
string1 = "amor"
string2 = "roma"

def check_words(string1, string2):
    def is_isogram (mystring):
        isograma = True
        for caracter in mystring:
            if (mystring.lower().count(caracter) > 1):
                isograma = False
        if (isograma == True):
            print(f"\nLa palabra {mystring} es un isograma")
    if (string1.lower() == string2.lower()):
        print(" - Las palabras son iguales - ")
    elif (len(string1) == len(string2) and list(string1.lower())[::-1] == list(string2.lower())):
        print(f"Las parlabras {string1} y {string2} son palíndromas")
        anagrama = True
        for caracter in string1:
            if (string1.lower().count(caracter) == string2.lower().count(caracter)):
                pass
            else:
                anagrama = False
        if (anagrama):
            print(f"\nLas palabras {string1} y {string2} son también anagrama. ")
        else:
            print(f"\nLas palabras {string1} y {string2} no son anagrama. ")
        is_isogram(string1)
        is_isogram(string2)

check_words(string1, string2)