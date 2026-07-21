'''
Crea un programa capaz de comprimir un archivo
en formato .zip (o el que tú quieras).
- No subas el archivo o el zip
'''

import zipfile

BASE_DIR = "Python/src/Ejercicios_avanzados/"
my_zip_file = f"{BASE_DIR}zip_folder/learning.zip"

with zipfile.ZipFile(my_zip_file, "w", compression=zipfile.ZIP_DEFLATED) as my_file:
    my_file.write(
        filename=f"{BASE_DIR}students.csv", 
        arcname="compressed_students.csv"
    )