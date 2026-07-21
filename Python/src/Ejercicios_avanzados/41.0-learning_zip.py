import zipfile
import os

'''
compression=zipfile.ZIP_DEFLATED # -> Para que comprima (que ocupe menos). Por defecto no lo hace.
Para manejo de ficheros siempre es mejor importar os. Así evitamos FileNotFoundError y podemos trabajar con rutas.
'''

BASE_DIR = "Python/src/Ejercicios_avanzados/"
my_zip_file = f"{BASE_DIR}my_file.zip"

with zipfile.ZipFile(my_zip_file, "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write(f"{BASE_DIR}students.csv", arcname="compressed_students.csv")
    my_zip.write(f"{BASE_DIR}subs.csv", arcname="compressed_subs.csv")

with zipfile.ZipFile(my_zip_file, "r") as my_zip:
    #print(my_zip.namelist()) # -> Para ver los archivos que tiene el zip sin descomprimir
    my_zip.extractall(path=f"{BASE_DIR}zip_folder")