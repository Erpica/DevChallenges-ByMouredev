# Estructura de Árbol (Tree Structure)
#Para hacer un repaso completo y directo, 
# vamos a ver cómo se realizan las operaciones 
# CRUD (Crear, Leer, Actualizar y Borrar) 
# utilizando las clases ElementTree y Element. 🛠️


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

# Buscamos el producto
prod = root.find("producto")
print(f"ID: {prod.attrib["id"]}")
print(f"Producto: {prod.find("nombre").text}")

# 3. Actualización (Update) 🔄
# ACTUALIZAR: Buscamos y cambiamos el texto
nombre_prod = root.find(".//nombre") # El .// busca en cualquier nivel
if nombre_prod is not None:
    nombre_prod.text = "Teclado mecánico RGB"

# Guardamos los cambios
tree.write(xml_file, encoding="utf-8", xml_declaration=True)

# 4. Borrado (Delete) ❌
# Para eliminar un elemento, necesitamos usar el método remove() 
# aplicado directamente sobre el nodo padre del elemento que queremos borrar.
# BORRAR: Eliminamos el producto de la raíz
# Comentamos estas dos líneas para no borrar el producto:
#if prod is not None:
#    root.remove(prod)

# Guardamos el archivo ya vacío de productos (comentamos también para no borrar)
#tree.write(xml_file, encoding="utf-8", xml_declaration=True)

# Resumen de Clases Clave 🧠
# ElementTree: Representa el archivo entero. Es el contenedor que se encarga de leer parse() y escribir write().
# Element: Representa cada etiqueta o nodo del mapa. Tiene las propiedades .tag, .text, .attrib y los métodos para buscar.

import xml.etree.ElementTree as xml

archivo = "Python/src/xml_json/resumen_xml_file.xml"

root = xml.Element("bbdd")

cita1 = xml.SubElement(root, "cita")
numerodecita1 = xml.SubElement(cita1, "numerodecita")
nombre1 = xml.SubElement(cita1, "nombre")
fecha1 = xml.SubElement(cita1, "fecha")
numerodecita1.text = "1 de mayo"
nombre1.text = "Anto"
fecha1.text = "19/05/2026"

cita2 = xml.SubElement(root, "cita")
numerodecita2 = xml.SubElement(cita2, "numerodecita")
nombre2 = xml.SubElement(cita2, "nombre")
fecha2 = xml.SubElement(cita2, "fecha")
numerodecita2.text = "2 de mayo"
nombre2.text = "Pic"
fecha2.text = "20/05/2026"

print(numerodecita1.text)
print(nombre1.text)
print(fecha1.text)
print(numerodecita2.text)
print(nombre2.text)
print(fecha2.text)

arbol = xml.ElementTree(root)
arbol.write(archivo, encoding="utf-8", xml_declaration=True)


