import xml.etree.ElementTree as xml
import os
import json


data_basic = {
    "name": "Anto",
    "age": 46
}

# Defino el archivo y su raíz:
xml_file = "Python/src/xml_json/erpica.xml"
root = xml.Element("data_basic")

# Recorro el diccionario para crear los hijos y rellenar su value
for key, value in data_basic.items():
    child = xml.SubElement(root, key)
    child.text = str(value)

# Defino el árbol y lo meto en el archivo:
tree = xml.ElementTree(root)
tree.write(xml_file) # Crea el archivo y lo sobreescribe si existe

# Ahora vamos a leer el archivo:
tree = xml.parse(xml_file)  # Clase ElementTree
root = tree.getroot()       # Clase Element

print(f"El nodo principal es: {root.tag}")



print(tree.find("age").text)
tree.find("age").text = 50
print(root.find("age").text)

















data = {
    "name": "Anto Martín",
    "age": 46,
    "birth_date": "01/01/1980",
    "programming_language": ["Python", "Javascript", "HTML", "CSS"]
}


# XML
# Para ver el árbol: shift + alt + f
xml_file = "Python/src/xml_json/erpica.xml"


# Para guardar datos de dos niveles:
def save_xml():
    root = xml.Element("data") # Crea la raíz (el contenedor principal).

    for key, value in data.items():
        child = xml.SubElement(root, key) # Crea un hijo directo de la raíz (aún sin texto).
        if isinstance(value, list):
            for item in value:
                # Si uno de los "value" es una lista, creamos un tercer nivel de jerarquía con etiquetas "item"
                xml.SubElement(child, "item").text = item 
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file, encoding="utf-8")

save_xml()

with open(xml_file, "r", encoding="utf-8") as xml_data:
    print(xml_data.read())


tree = xml.parse(xml_file)
root = tree.getroot()

languages = root.find("programming_language")
for lang in languages.findall("item"):
    print(lang.text)


# os.remove(xml_file)

'''
Función    Clase            Propósito
parse()     ElementTree     Lee un archivo XML externo y lo carga en memoria.
getroot()   ElementTree     Obtiene el elemento raíz para empezar a navegar.
find()      Element         Busca el primer hijo que coincida con una etiqueta.
findall()   Element         Busca todos los hijos que coincidan con una etiqueta.
set()       Element         "Crea o actualiza un atributo (ej: <item id=""1"">)."
append()    Element         Añade un nuevo elemento hijo a un nodo existente.

Mientras que ElementTree es "el mapa", Element es "el lugar". Cada vez que haces root[0] o find(), lo que recibes es un objeto Element. Sus propiedades más usadas son:
.tag: El nombre de la etiqueta (ej: "name").
.text: El contenido escrito dentro (ej: "Anto Martín").
.attrib: Un diccionario con los atributos del nodo.
'''


# JSON:
# Para ver el árbol: shift + alt + f
json_file = "Python/src/xml_json/erpica.json"
with open (json_file, "w", encoding="utf-8") as json_data:
    # "Vuelca" el diccionario directamente al archivo. Y con indent me lo formatea para que el archivo se vea bien.
    json.dump(data, json_data, indent = 4, ensure_ascii=False) # ensure_ascii=False # Para que coja los acentos

with open(json_file, "r", encoding="utf-8") as json_data:
    print(json_data.read())

# os.remove(json_file)


'''
DIFICULTAD EXTRA:
Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.

'''

class Custom:
    pass