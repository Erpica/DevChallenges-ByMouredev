# Funciones que pueden recibir funciones como argumento:

def apply_func(func, x):
    return func(x)

x = apply_func(len, "Erpica")
print(x)

# Puede retornar una función
def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier
    
multiplier = apply_multiplier(2)
print(multiplier(5))
print (apply_multiplier(2)(3))

# Sistema:

numbers = [1, 3, 4, 2, 5]

# map()
# Se le pasa una lista y una función sin paréntesis porque no es para que la ejecute ahora, 
# lo irá haciendo iteración por iteración y le va metiendo en un elemento iterable
def apply_double(n):
    return n * 2

print (list(map(apply_double, numbers)))

# filter
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))

# sorted
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce: acumula resultados de la forma que le diga la función (es decir el otro parámetro)
from functools import reduce


def my_sum(x, y):
    return x + y

print(reduce(my_sum, numbers))

''' 
EXTRA:
Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
lista de calificaciones), utiliza funciones de orden superior para 
realizar las siguientes operaciones de procesamiento y análisis:
- Promedio calificaciones: Obtiene una lista de estudiantes por nombre
y promedio de sus calificaciones.
- Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
que tienen calificaciones con un 9 ó más de promedio.
- Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
- Mayor calificación: Obtiene la calificación más alta de entre todas las 
de los alumnos.
- Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
'''

students = [
    {"name": "Anto", "birthday": "15/06/1980", "califications": [5, 10, 6, 8]},
    {"name": "Pepe", "birthday": "12/07/1985", "califications": [2, 4, 5, 7]},
    {"name": "Paco", "birthday": "11/09/2011", "califications": [9, 10, 9, 8]},
    {"name": "Luis", "birthday": "01/01/2000", "califications": [5, 5, 6, 6]},
    {"name": "Gera", "birthday": "31/12/1999", "califications": [1, 10, 10, 8]}
]

def califications_average():
    for one_student in students:
        count = 0
        my_sum = 0
        for calification in one_student["califications"]:
            my_sum += calification
            count += 1
        print(f"La media de {one_student["name"]} es {my_sum / count}")

def best_students():
    best_list =[]
    for one_student in students:
        for calification in one_student["califications"]:
            if calification >= 9:
                best_list.append(one_student["name"])
    print (set(best_list))

califications_average()
best_students()


''' 
EXTRA:
Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y
lista de calificaciones), utiliza funciones de orden superior para 
realizar las siguientes operaciones de procesamiento y análisis:
- Promedio calificaciones: Obtiene una lista de estudiantes por nombre
y promedio de sus calificaciones.
- Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
que tienen calificaciones con un 9 ó más de promedio.
- Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
- Mayor calificación: Obtiene la calificación más alta de entre todas las 
de los alumnos.
- Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
'''

# Extra by Brais
def average(califications):
    return sum(califications) / len(califications)

# Promedio
print(list(map(lambda student: {
    "name": student["name"], 
    "average": average(student["califications"])}, 
    students)
    )
)

# Mejores:
print(
    list(
        map(lambda student: 
        student["name"], 
        filter(lambda student: average(student["califications"]) >= 9, 
               students)
        )
    )
)

# Fecha de nacimiento
from datetime import datetime

print(sorted(students, 
             key=lambda student: datetime.strptime(student["birthday"], "%d/%m/%Y"), 
             reverse=True
             )
    )

# Calificación más alta
print(
    max(
        map(
            lambda student: max(student["califications"]), 
            students)
        )
    )