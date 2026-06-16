'''
¡La casa del dragón ha finalizado y no volverá hasta 2026!
¿Alguien se entera de todas las relaciones de parentesco
entre personajes que aparecen en la saga?
Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
Requisitos:
1. Estará formado por personas con las siguientes propiedades:
  - Idéntificador único (obligatorio)
  - Nombre (obligatorio)
  - Pareja (opcional)
  - Hijos (opcional)
2. Una persona solo puede tener una pareja (para simplificarlo).
3. Las relaciones deben validarse dentro de lo posible.
   Ejemplo: Un hijo no puede tener tres padres.
Acciones: 
1. Crea un programa que permita crear y modificar el árbol. 
  - Añadir y eliminar personas
  - Modificar pareja e hijos
  2. Podrás imprimir el árbol (de la manera que consideres).

  NOTA: Ten en cuenta que la complejidad puede ser alta si 
  se implementan todas las posibles relaciones. Intenta marcar
  tus propias reglas y límites para que te resulte asumible.
'''

class Person:
    my_id = 0
    
    def __init__(self, name):
        self.id = Person.my_id
        self.name = name
        self.couple = None
        self.childs = []
        Person.my_id += 1

    def agree_couple(self, couple: Person):
        if not self.couple:
            self.couple = couple

    def show_couple(self):
        print(Person.couple.name)

    


class Relation:
    relation_list = ["child", "parent", "couple"]
    def __init__(self, name, relation, name2):
        if relation == "child":
            name.agree_child(name2)
        elif relation == "couple":
            name.agree_couple(name2)

    def agree_child(self):
        pass






class Tree:
    level = 0
    all_tree = []

    def __init__(self, name):
        Tree.all_tree.append(name)

    def show_tree(self):
        print("Mostrando el árbol completo:")
        print(Tree.all_tree)

    def add_to_tree(self, name, relation):
        pass



    
        
person0 = Person("Papá")
person1 = Person("Mamá")
person2 = Person("Antonio")
person3 = Person("Anto")
person4 = Person("Irene")
print (person4.my_id, person4.name)

person1.agree_couple(person0)

person1.show_couple()