'''
Valor y referencia
'''

# Tipos de dato por valor
# Los tipos de datos primitivos suelen ser por valor
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
print (my_int_a)
print (my_int_b)
print()

# Tipos de dato por referencia
# No copian su valor, heredan su posición de memoria
# En python son todos los tipos de datos que no son primitivos: entero, float, cadena de texcto ni booleano
# No serían primitivos: lista, tupla, diccionario, set
my_list_a = [10, 20]
my_list_b = my_list_a # ya my_list_b apunta al espacio de memoria que apuntaba my_list_a (las dos apuntan al mismo sitio)
my_list_b.append(30)
print(my_list_a)
print(my_list_b)
print()

# Funciones con datos por valor
my_int_c = 10

def my_int_func(my_int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia
my_list_c =[10, 20]

def my_list_func(my_list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)
    
    print(my_list)
    print(my_list_d)

print(my_list_c)
my_list_func(my_list_c)
print(my_list_c)

'''
Dificultad extra:
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables 
anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por 
referencia.

Estos parámetros los intercambia entre ellos en su interior, los retorna y su retorno 
se asigna a dos variables diferentes a las originales. A continuación, imprime el valor 
de las variables originales y las nuevas, comprobando que se ha invertido su valor 
en las segundas. 
Comprueba también que se ha conservado el valor original en las primeras.

'''

my_int_value1 = 1
my_int_value2 = 2
my_list_ref1 = [1, 2]
my_list_ref2 = [2, 1]

def value_func(int_value1: int, int_value2: int):
    int_value3 = int_value1
    int_value1 = int_value2
    int_value2 = int_value3
    return int_value1, int_value2

my_int_value4, my_int_value5 = value_func(my_int_value1, my_int_value2)

print("\nOriginales:")
print(f"my_int_value1: ", my_int_value1, "\nmy_int_value2: ", my_int_value2)
print("\nNuevas:")
print(f"my_int_value4: ", my_int_value4, "\nmy_int_value5: ", my_int_value5)

def ref_func(list_ref1: list, list_ref2: list):
    list_ref3 = list_ref1
    list_ref1 = list_ref2
    list_ref2 = list_ref3
    return list_ref1, list_ref2

my_list_ref4, my_list_ref5 = ref_func(my_list_ref1, my_list_ref2)

print("\nOriginales:")
print(f"my_list_ref1: {my_list_ref1}\nmy_list_ref2: {my_list_ref2}")
print("\nNuevas:")
print(f"my_list_ref4: {my_list_ref4}\nmy_list_ref5: {my_list_ref5}")