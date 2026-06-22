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

print("Lenguajes de programación:")
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
import xml.etree.ElementTree as xml

class Custom:
    
    def __init__(self, xml_file: str):
        self.xml_file = xml_file

    def show_xml(self):
        with open (self.xml_file, "r", encoding="utf-8") as file:
            tree = xml.parse(file)
            root = tree.getroot()
            
            xml_completo = xml.tostring(root, encoding="utf-8").decode("utf-8")
            print(xml_completo)

    def update_xml(self):
        with open (self.xml_file, "r", encoding="utf-8") as file:
            tree = xml.parse(file)
            root = tree.getroot()
            
            xml_completo = xml.tostring(root, encoding="utf-8").decode("utf-8")
            print(xml_completo)

            tag_to_update = input("\nIntroduce la etiqueta que vas a actualizar: ")







XML_FILE = "Python/src/xml_json/erpica.xml"
mycustom = Custom(XML_FILE)
mycustom.show_xml()



'''
        - en una clase: -
    * para inicializarla recibe el nombre de un archivo
    * tiene dos funciones (para cada tipo) empezamos por xml
        - Leer
            1 abro el archivo en modo lectura y lo muestro
        - Transformar
            1 abro el archivo en modo lectura y lo muestro
            2 pido que item quiere transformar y por cual
            3 cambio el itel
            4 lo meto en el archivo de nuevo
        


'''

# POR BRAIS

import xml.etree.ElementTree as xml
import os
import json

xml_file = "Python/src/xml_json/erpica.xml"
class Data:
    def __init__(self, name, age, birth_date, programming_language) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_language = programming_language
        
with open(xml_file, "r") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_language = []
    for item in root.find("programming_language"):
        programming_language.append(item.text)

    xml_class = Data(name, age, birth_date, programming_language)
    print(xml_class.__dict__)       # Esto es: "Imprímelo en formato diccionario"

json_file = "Python/src/xml_json/erpica.json"
with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    """
    name = json_dict["name"]
    age = json_dict["age"]
    birth_date = json_dict["birth_date"] 
    """
    # O mejor:
    json_class = Data (
        json_dict["name"], 
        json_dict["age"], 
        json_dict["birth_date"], 
        json_dict["programming_language"]
        )
    print(json_class.__dict__)
    
    