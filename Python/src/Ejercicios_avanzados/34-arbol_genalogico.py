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
        self.parents = []
        Person.my_id += 1

    def agree_couple(self, couple: Person):
        if not self.couple:
            print("La pareja se ha añadido correctamente.")
        else:
            print("Tu pareja ha sido modificada")
        self.couple = couple
        couple.couple = self
        #couple.agree_couple(self)

    def show_couple(self):
        print(f"La pareja de {self.name} es {self.couple.name}")

    def agree_child(self, child: Person):
        if child not in self.childs:
            self.childs.append(child)
        else:
            print(f"{child.name} ya fue añadido anteriormente.")

    def show_child(self):
        if self.childs:
            print(f"\nEl/los hijos/as de {self.name} es/son:")
            for one_child in self.childs:
                print(f"{one_child.name}")
        else:
            print(f"{self.name} no tiene aún ningún niño declarado.")

    def agree_parent(self, parent: Person):
        if len(self.parents) >= 2:
            print("Debe haber algún error, nadie puede tener más de dos padres...")
        else:    
            self.parents.append(parent)
            print(f"Ahora {self.name} es hijo de {parent.name}")
    
    def show_parents(self):
        print(f"\nEl/los padres de {self.name} es/son:")
        for one_parent in self.parents:
            print(one_parent.name)


class Tree:
    def show_tree(self):
        print("Mostrando el árbol completo:")
        print(Tree.all_tree)

    def add_to_tree(self, name, relation):
        pass
    
        
person0 = Person("Papá")
person1 = Person("Mamá")
person2 = Person("Antonio")
person3 = Person("Pablo")
person4 = Person("Laura")
person5 = Person("Irene")
person6 = Person("Anto")
person6 = Person("Alba")
person6 = Person("Sara")
print (person4.my_id, person4.name)

person1.agree_couple(person0)
person1.show_couple()

person1.agree_child(person2)
person1.agree_child(person3)
person1.agree_child(person4)
person0.agree_child(person2)
person0.agree_child(person3)
person0.agree_child(person4)
person1.show_child()
person0.show_child()
person6.show_child()

person2.agree_parent(person0)
person2.agree_parent(person1)
person2.agree_parent(person2)
person2.show_parents()

# my_tree = Tree(person0.name)
# my_tree.show_tree()

