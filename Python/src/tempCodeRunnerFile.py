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
