import zipfile

'''
compression=zipfile.ZIP_DEFLATED # -> Para que comprima (que ocupe menos). Por defecto no lo hace.
'''

with zipfile.ZipFile("my_file.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write("students.csv", arcname="compressed_students.csv")