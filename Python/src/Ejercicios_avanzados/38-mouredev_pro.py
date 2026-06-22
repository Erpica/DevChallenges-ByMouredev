'''
He presentado mi proyecto más importante del año: mouredev pro.
Un campus para la comunidad, que lanzaré en octubre, donde estudiar
programación de manera diferente.
Cualquier persona suscrita a la newsletter de https://mouredev.pro
accederá a sorteos mensuales de suscripciones, regalos y descuentos.

Desarrolla un programa que lea los registros de un fichero .csv y 
seleccione de manera aleatoria diferentes ganadores.
Requisitos:
1. Crea un .csv con tres columnas: id, email y status con valor "activo"
   o "inactivo" (y datos ficticios).
   Ejemplo: 1 | test@test.com | activo
            2 | test2@test.com | inactivo
   (El .csv no debe subirse como parte de la correción)
2. Recupera los datos desde el programa y selecciona email aleatorios.
Acciones:
1. Accede al fichero .csv y selecciona de manera aleatoria un email
   ganador de una suscripción, otro ganador de un descuento y un último
   ganador de un libro (solo si tiene status activo y no está repetido).
2. Muestra los emails ganadores y su id.
3. Ten en cuenta que la primera fila (con el nombre de las columnas)
   No debe tenerse en cuenta.
'''
import os
import random

# print("Directorio del script:", os.path.dirname(__file__))
# print("Directorio de trabajo actual:", os.getcwd())

file_csv = ".\Python\src\Ejercicios_avanzados\students.csv"

# Así se puede comprobar si existe el fichero y crearlo con algunos registros para probar:
def file_exists(my_file):
    try:
        with open(my_file, "r", encoding="utf-8") as file:
            contenido = file.read().strip()
            return bool(contenido)   # True si hay algo, False si está vacío
    except:
        return False

def inicialice_file(my_file):
    columns = ["ID", "EMAIL", "STATUS"]
    files = [
        {"ID": 1, "EMAIL": "test@test.com", "STATUS": "activo"}, 
        {"ID": 2, "EMAIL": "test2@test.com", "STATUS": "inactivo"},
        {"ID": 3, "EMAIL": "test3@test.com", "STATUS": "activo"},
        {"ID": 4, "EMAIL": "test4@test.com", "STATUS": "activo"}, 
        {"ID": 5, "EMAIL": "test5@test.com", "STATUS": "inactivo"},
        {"ID": 6, "EMAIL": "test6@test.com", "STATUS": "activo"}
    ]
    try:
        with open(my_file, "w", encoding="utf-8") as file:
            # Escribimos los encabezados:
            file.write(",".join(columns) + "\n")

            # Escribimos los registros:
            for register in files:
                one_register = ",".join(str(register.get(col, "")) for col in columns)
                file.write(one_register + "\n")
            print("Archivo inicializado correctamente.")

    except Exception as e:
        print("Error al crear el archivo.")

def get_mails(my_file):
    try:
        with open(my_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Saltamos la primera línea (cabeceras)
            registros = lines[1:]
            result = []
            for line in registros:
                one_register = line.strip().split(",")
                #print(f"Un registro: {line.strip().split(",")}")
                # Evitar errores si la línea está incompleta
                #print (len(one_register))
                if len(one_register) < 3:
                    continue
                id_ = one_register[0].strip()
                email = one_register[1].strip()
                status = one_register[2].strip()
                
                if status != "activo":
                    continue
                
                result.append((id_, email))
 
            return result
    except Exception as e:
        print("Error obeniendo los emails.")

if not file_exists(file_csv):
    inicialice_file(file_csv)

if file_exists(file_csv):
    participantes = get_mails(file_csv)
    random.shuffle(participantes)

    print("## GANADORES ##")
    print(f"1 Suscripción: {participantes[0][1]}")
    print(f"2 Descuento:   {participantes[1][1]}")
    print(f"3 Libro:       {participantes[2][1]}")
    

        