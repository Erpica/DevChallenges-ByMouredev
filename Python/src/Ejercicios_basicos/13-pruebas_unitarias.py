import unittest
from datetime import datetime, date

# la librería por excelencia sin rebuscar mucho: unittest


def sum (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser números")
    return a + b

# Para poder ejecutar un test hay que crear una función
# Si la función empieza por test se convierte en una función de test
# lo que quiere decir que, cuando yo le diga al ide vamos a ejecutar los test,
# se pondrá a buscar todas las funciones que empiezan por test

# En Python, para que se ejecute el test tiene que estar dentro de una clase
# que hereda de unittest.TestCase
# Una buena práctica es que la clase empiece por Test

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 4.1), 6.6)
        self.assertEqual(sum(2.5, 4.1), 6.6)
        #self.assertEqual(sum("2.5", 4.1), 6.6) # Error 

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 2)
        with self.assertRaises(ValueError):
            sum("5", "2")
        with self.assertRaises(ValueError):
            sum("a", 2)
        with self.assertRaises(ValueError):
            sum(None, 2)


'''
# Dificultad extra:
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de programación]
Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducidos son correctos.

'''



class TestApp (unittest.TestCase):

    def setUp(self) -> None:
        self.my_dict = {
            "name": "Anto",
            "age": 45,
            "birth_date": datetime.strptime("15-06-80", "%d-%m-%y").date(),
            "programming_languages": ["HTML", "CSS", "Javascript", "Python"]
        }

    def test_exist(self):
        self.assertIn("name", self.my_dict)
        self.assertIn("age", self.my_dict)
        self.assertIn("birth_date", self.my_dict)
        self.assertIn("programming_languages", self.my_dict)

    def test_my_dict_data_is_correct(self):
        # self.assertEqual(self.data["name"], "Anto") # Si supíeramos exactamente los datos
        self.assertIsInstance(self.my_dict["name"], str)
        self.assertIsInstance(self.my_dict["age"], int)
        self.assertIsInstance(self.my_dict["birth_date"], date)
        self.assertIsInstance(self.my_dict["programming_languages"], list)

unittest.main()