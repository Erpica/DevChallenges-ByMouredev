print("\nDiccionario:")
my_dict: dict = {
    "name": "Anto",
    "surname": "Erpica",
    "alias": "@Antodev",
    "age": "45"
}
my_dict["email"] = "Antodev@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
print("    - items -")
print(type(my_dict.items()))
print(my_dict.items())
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

print(my_dict.get("name"))
print(my_dict.get("names"))
print(my_dict.get("names", "No está"))