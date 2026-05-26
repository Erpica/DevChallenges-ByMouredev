
# 1. Estructura y Creación (Create) 📑
# CREAR: Definimos el nodo raíz.
import xml.etree.ElementTree as xml
xml_file = "Python/src/xml_json/resumen_xml_file.xml"

# Definimos la raíz y sus hijos
root = xml.Element("catalogo")

producto = xml.SubElement(root, "producto")
producto.set("id", "101") # Atributo 🏷️
nombre = xml.SubElement(producto, "nombre")
nombre.text = "Teclado mecánico" # Contenido ✍️

# GUARDAR: Creamos el árbol y escribimos el fichero
tree = xml.ElementTree(root)
tree.write(xml_file, encoding="utf-8", xml_declaration=True)


# 2. Lectura (Read) 🔍
# LEER: Cargamos el archivo y obtenemos la raíz
tree = xml.parse(xml_file)
root = tree.getroot()