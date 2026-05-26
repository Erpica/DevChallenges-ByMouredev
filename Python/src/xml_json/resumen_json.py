import json

# tips: 
# En json no hay int, double, float... todos son number
# True y False son true y false
# None es null

usuario = {
    "id": 1,
    "nombre": "Anto",
    "activo": True
}

# 1 CREAR LA ESTRUCTURA
# Con dump metemos el diccionario de Python en un archivo .json
# Una estructura más compleja (Diccionario con listas y sub-diccionarios)
inventario_tienda = {
    "tienda": "Zona Gamer",
    "fecha_actualizacion": "2026-05-20",
    "videojuegos": [
        {
            "id": 101,
            "titulo": "Cyberpunk Adventure",
            "precio": 59.99,
            "generos": ["RPG", "Sci-Fi"],
            "disponible": True
        },
        {
            "id": 102,
            "titulo": "Pixel Dungeon",
            "precio": 14.50,
            "generos": ["Roguelike", "Indie"],
            "disponible": False
        }
    ]
}

with open ("Python/src/xml_json/resumen_json_file.json", "w", encoding="utf-8") as archivo:
    json.dump(inventario_tienda, archivo, indent=4)

# 2 LEER. load
# Recuperamos la información del archivo y lo convertimos en un diccionario con load
with open ("Python/src/xml_json/resumen_json_file.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print (datos)

'''
Existe otra pareja de funciones muy famosa que la mayoría de la gente usa todo el tiempo. 
Se llaman json.dumps y json.loads (la "s" al final significa string). 
No sirven para archivos físicos, sino para trabajar con strings.

Si tenemos un texto con formato JSON que nos llega desde internet:
json.loads => para transformarlo en un diccionario de Python (load string)
json.dumps => coge un diccionario de Python y lo convierte en una sola cadena de texto.
'''


# 3 Update
import json
with open ("Python/src/xml_json/resumen_json_file.json", "r", encoding="utf-8") as my_file:
    data = json.load(my_file)

data["videojuegos"][0]["precio"] = 75

with open ("Python/src/xml_json/resumen_json_file.json", "w", encoding="utf-8") as my_file:
    json.dump(data, my_file, indent=4)


# 4 Delete
import json
with open ("Python/src/xml_json/resumen_json_file.json", "r", encoding="utf-8") as my_file:
    data = json.load(my_file)

del data["videojuegos"][0]

'''
🏁 ¡CRUD Completado y Repaso Final!
Operaciones básicas en un archivo:
Create (Crear): json.dump() al escribir por primera vez.
Read (Leer): json.load() para cargar los datos en Python.
Update (Actualizar): Modificar el diccionario en memoria y usar json.dump().
Delete (Borrar): Usar del en la lista y volver a usar json.dump().
'''