
# for
for i in range(1,11):
    print(i)

# while
i=1
while i <= 10:
    print(i)
    i += 1

# recursividad
def one_to_ten (number = 1) -> None:
    print (number)
    if number >= 10:
        return None
    else:
        return one_to_ten(number + 1)

one_to_ten()

# By Brais:
def count_ten(i=1):
    if i <= 10:
        print (i)
        count_ten(i + 1)


'''
# Dificultad extra:
Escribe el mayor número de mecanismos que posea tu lenguaje
para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?




'''

# enumerate
planetas = ["Mercurio", "Venus", "Tierra"]

for indice, planeta in enumerate(planetas, start=1):
    print(f"El planeta en la posición {indice} es {planeta}")

# List Comprehensions (comprensión de listas)
# nueva_lista = [expresion for elemento in iterable]

# forma antigua:
numeros = [1, 2, 3, 4]
cuadrados_old = []
for n in numeros:
    cuadrados_old.append(n ** 2)
# Resultado: [1, 4, 9, 16]

# Con list Comprehension:
cuadrados = [n ** 2 for n in numeros]

print(cuadrados)
print(cuadrados_old)

my_list = ["sol", "tierra", "mar"]
long_words_upper_list = [element.upper() for element in my_list if len(element) > 3]
print(long_words_upper_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n %2 == 0]
print(even_numbers)

all_even_numbers = [n if n %2 == 0 else n*2 for n in numbers ]
print(all_even_numbers)


a = 1
b = 2

a, b = b, a
print(a, b)

# zip
# Como una cremallera une dos listas en el orden que están el primer elemento con el primero...
# Acaba en cuanto la lista más corta termina
alumnos = ["Ana", "Luis", "Carlos", "pica"]
notas = [9, 8, 10]
for alumno, nota in zip(alumnos, notas):
    print(f"{alumno} ha sacado un {nota}")

print("\nImprimir directamente:")
[print(f"{student}: {grade}") for student, grade in zip(alumnos, notas)]
print("\nO lo meto en la lista y luego imprimo la lista:")
list_with_califications = [f"{student}: {grade}" for student, grade in zip(alumnos, notas)]
print(list_with_califications)
print("\nSi además se me ocurre enumerarlo:")
for i, (student, grade) in enumerate(zip(alumnos, notas), start=1):
    print (f"{i}. {student} - Nota: {grade}")


# map: sirve para aplicar una función a cada uno de los elementos de un iterable.
# Devuelve un objeto mapa. Lo podemos meter en list
precios_str = ["10.5", "20.3", "5.9"]
precios_num = list(map(float, precios_str))
print (precios_num)


# filter:
numeros = [2, 8, 3, 10, 5, 7]
mayores_que_cinco = list(filter(lambda x: x > 5, numeros))
print(mayores_que_cinco)

# .items()
# Función que usamos para recorrer diccionarios
capitales = {"España": "Madrid", "Francia": "París", "Italia": "Roma"}

for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}")

# By Brais (list comprenhension)
# * -> Operador de desempaquetado. En este ejemplo, si se lo quito, me lo imprime todo en una línea. SOLO PARA LISTAS Y TUPLAS
print(*[i for i in range (1, 11)], sep="\n")


primero, *el_resto, ultimo = [1, 2, 3, 4, 5]
# primero = 1
# el_resto = [2, 3, 4]
# ultimo = 5
print(primero)
print(el_resto)
print(ultimo)

frutas = ["manzana", "plátano"]
verduras = ["zanahoria", "tomate"]

# Combinamos ambas en una nueva lista
comida = [*frutas, *verduras] 
# Resultado: ['manzana', 'plátano', 'zanahoria', 'tomate']
print(comida)

# ** -> Operador de desempaquetado. PARA DICCIONARIOS
usuario_base = {"rol": "alumno", "activo": True}
usuario_juan = {**usuario_base, "nombre": "Juan"}
# Resultado: {'rol': 'alumno', 'activo': True, 'nombre': 'Juan'}
print(usuario_juan)

# Argmentos para print:
# Por defecto tiene el end=\n 
print("hola", end="")
print(" y adios")
# por defecto va a consola pero se puede mandar a un archivo:
'''
with open("log.txt", "w") as archivo:
    print("Este mensaje se guardará en el archivo, no en la pantalla.", file=archivo)
'''

# flush
'''
Python, por motivos de velocidad, a veces guarda los textos en una memoria temporal (búfer) antes de pintarlos en la pantalla. 
Si pones flush=True, obligas a Python a mostrar el texto de inmediato. Es súper útil para barras de carga o animaciones en la consola.
Ej:
import time
print("Cargando...", end="", flush=True)
time.sleep(2) # Se muestra "Cargando..." instantáneamente sin esperar a que termine el programa

'''

for c in "python":
    print (c)

for c in reversed([1, 2, 3, 4]):
    print (c)

for c in sorted(["P", "i", "c", "a"]):
    print (c)