# Pila / Stack (LIFO)
stack = []

# push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)
print(stack)

print(stack.pop())
print(stack)

# Cola / Queue (FIFO)

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print (queue)

print(queue.pop(0))
print (queue)

'''
EJERCICIO EXTRA 1:
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como 
el nombre de una nueva web.
'''




def web_browser() -> str:
    history = []
    index = 0
    page =""
    print (f"\n ## Bienvenido al navegador de Pica: ##{page}\n")
    while True:
        page = input("Introduce la página web que deseas visitar <atrás> <adelante> <salir>: ")
        match page:
            case "atrás":
                if (history[0]):
                    index -= 1
                    if (index > 0):
                        page = history[index-1]
                        print (f"\n\nBienvenido a la página web {page}:\nContenido de la web\n\n")
                    else:
                        print("    <<< Estás navegando en la página incial.>>>")
                else:
                    print("Estás en la página inicial")
            case "adelante":
                index +=1
                print (f"\n\nBienvenido a la página web {page}:\nContenido de la web\n\n")
            case "salir":
                print (f"\n\nGracias por usar el navegador, nos vemos pronto.\n\n")
                break
            case _:
                history.append(page)
                index += 1
                print (f"\n\nBienvenido a la página web {page}:\nContenido de la web\n\n")
            

web_browser()


'''
EJERCICIO EXTRA 2:
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una 
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
imterpretan como nombres de documentos.
'''

def my_printer():
    queue_docs = []
    index = 0

    while True:
        my_file = input ("Esperando archivo... (o imprimir/salir): ")
        match my_file:
            case "imprimir":
                if (len(queue_docs) > 0):
                    print(f"Imprimiendo {queue_docs[0]}")
                    del(queue_docs[0])
                    index -= 1
                    print(queue_docs)
                else:
                    print("No queda ningún elemento para imprimir en la caché de la impresora.")
            case "salir":
                print("Gracias por utilizar mi impresora.")
                break
            case _:
                queue_docs.append(my_file)
                index += 1
                print(f"El archivo {queue_docs[index-1]} ha sido añadido a la cola:\n{queue_docs}")



my_printer()

