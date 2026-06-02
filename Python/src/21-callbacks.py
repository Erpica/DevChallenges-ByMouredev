# callback es una función que llama a otra función
# Se utilizan, sobre todo, en programación asíncrona
# Por ejemplo: Ejecútate cuando acabe el proceso de pago.

# Las callback functions son funciones de primera clase o de primer orden o de orden superior. Lo que significa:
# - Se pueden asignar a variables
# - Se pueden pasar como argumentos a otras funciones
# - Pueden devolver otra función como resultado
# - Se pueden almacenar en estructuras de datos como listas o diccionarios

from functools import reduce

def greeting_process(name: str, callback):
    '''
    Función callback que simula un proceso de saludo. Recibe un nombre y una función callback que se ejecutará al finalizar el proceso.

    Parámetros:
    name (str): El nombre de la persona a saludar.
    callback (function): La función callback que se ejecutará al finalizar el proceso de saludo.

    Devuelve:
    None
    '''
    print("Ejecutando el proceso de saludo")
    callback(name)

def greet_callback(name: str):
    print(f"Hola, {name}!")



# greeting_process(greet_callback("Anto")) # Error, para pasar la función tiene que hacerse como si fuera un parámetro, es decir, sin argumentos.
greeting_process("Anto", greet_callback)


# Para imprimir la documentación que previamente hemos puesto en la función
print(greeting_process.__doc__)

# Deberíamos seguir por aquí:
# https://www.youtube.com/watch?v=TbcEqkabAWU&t=1s


### Built-oin Higher Order Functions: ###

numbers = [2, 5, 10, 21]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))  # devuelve el listado de solo los que la función dió True
print(list(filter(lambda number: number > 10, numbers)))

# reduce
def sum_two_values(a, b):
    print(f"Valor uno: {a}")
    print(f"Valor dos: {b}")
    print("Acumulado y ", end="")
    return a + b


print(reduce(sum_two_values, numbers))



'''
Callback, ejemplo coche que frena fuerte, flojo o solo pita, según la velocidad que lleva

'''
import time

# --- 1. Definimos los Callbacks (Las acciones) ---
def accion_lenta(distancia):
    print(f"🛑 [ACCIÓN] Frenando suavemente a {distancia} metros y encendiendo luces de emergencia.")

def accion_rapida(distancia):
    print(f"🚨 [ACCIÓN]  a {distancia} metros ¡FRENAZO DE EMERGENCIA! Tensando cinturones de seguridad.")

def accion_aparcamiento(distancia):
    print(f"🔊 [ACCIÓN] Pitido continuo: ¡BEEP BEEP BEEP! Estás  a {distancia} metros, demasiado cerca.")


# --- 2. Definimos la Función Principal ---
# Fíjate que recibe un parámetro llamado 'funcion_callback'
def detectar_obstaculo(funcion_callback):
    print("\n🔍 Sensor activado... Escaneando la carretera y la distancia...")
    time.sleep(1.5)  # Simulamos que pasa un pequeño tiempo de escaneo
    distancia = 5
    print("⚠️ ¡OBSTÁCULO DETECTADO!")
    
    # Aquí ejecutamos el callback que nos hayan pasado. ¡Aquí sí lleva paréntesis!
    funcion_callback(distancia)



detectar_obstaculo(accion_lenta)
detectar_obstaculo(accion_rapida)
detectar_obstaculo(accion_aparcamiento)

























'''
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estará formado por una función que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmación, una de listo y otra de entrega.
- Debe imprimir una confirmación cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre  prcesos
- Debe invocar a cada callback siguiente un orden de procesado.
- Debe notificar que el plato está listo o ha sido entregado.


'''
import time
import random

def confirmation_function(name):
    # time.sleep(random.randint(1, 10)) @ esto es lo que pide literalmente
    time.sleep(1.5)
    print(f"OK, your {name} is now ordered")

def ready_function(name):
    time.sleep(1.5)
    print(f"OK, your {name} is now ready")

def delivered_function(name):
    time.sleep(1.5)
    print(f"OK, your {name} is been delivering")


def your_order_my_command (name, callback_function):
    # print(f"OK, your {name} is now ordered")
    callback_function(name)
    
    

your_order_my_command("Coffe", confirmation_function)
your_order_my_command("Coffe", ready_function)
your_order_my_command("Coffe", delivered_function)

# EXTRA BRAIS:

import time
import random
import threading

def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    def process():
        confirm_callback(dish_name)
        time.sleep(random.randint(1, 10))
        ready_callback(dish_name)
        time.sleep(random.randint(1, 10))
        delivered_callback(dish_name)
    threading.Thread(target = process).start()

def confirm_callback(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido realizado.")

def ready_callback(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido enviado.")

def delivered_callback(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado.")


order_process("Pizza Barbacoa", confirm_callback, ready_callback, delivered_callback)
order_process("Pizza 4 Quesos", confirm_callback, ready_callback, delivered_callback)
order_process("Pizza Margarita", confirm_callback, ready_callback, delivered_callback)
order_process("Pizza con Piña", confirm_callback, ready_callback, delivered_callback)