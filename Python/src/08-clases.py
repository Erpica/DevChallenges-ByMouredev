class Programmer:

    surname = ""

    def __init__(self, name: str, age: int, languajes: list):
        self.name = name
        self.age = age
        self.languajes = languajes

    def print(self):
        print(
        f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languajes}")

my_programmer = Programmer("Anto", 45, ["Python", "Java", "Javascript"])
my_programmer.print()
my_programmer.surname = "Pica"
my_programmer.print()
my_programmer.age = 46
my_programmer.print()



'''
# EJERCICIO EXTRA: #
Implementa dos clases que representen las estructuras de Pila y Cola
- Deben poder inicializarse y disponer de operaciones para añadir, elminiar, 
retornar el número de elementos e imprimir todo su contenido.
'''

class My_Stack:
    items = []

    def __init__(self, items: list):
        self.items = items

    def add_item(self, item: str):
        self.items.append(item)

    def add_item(self, item: int):
        self.items.append(item)

    def del_item(self):
        if self.count_items() > 0:
            self.items.pop()
        else:
            print("No hay elementos en la pila")

    def count_items(self):
        return len(self.items)

    def show_items(self):
        print(self.items)

one_stack = My_Stack(["file1", "file2"])
one_stack.show_items()
one_stack.add_item(3)
one_stack.show_items()
one_stack.del_item()
one_stack.del_item()
one_stack.del_item()
one_stack.del_item()
one_stack.show_items()



class My_Queue:
    items = []

    def __init__(self, items: list):
        self.items = items

    def add_item(self, item: str):
        self.items.append(item)

    def add_item(self, item: int):
        self.items.append(item)

    def del_item(self):
        if (len(self.items) > 0):
            del(self.items[0])

    def show_items(self):
        print(self.items)

one_queue = My_Queue(["file1", "file2"])
one_queue.show_items()
one_queue.add_item(3)
one_queue.show_items()
one_queue.del_item()
one_queue.show_items()



"""
Extra por Brais


# LIFO


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

# FIFO


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
"""