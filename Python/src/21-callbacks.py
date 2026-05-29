# callback es una función que llama a otra función
# Se utilizan, sobre todo, en programación asíncrona
# Por ejemplo: Ejecútate cuando acabe el proceso de pago.

# Las callback functions son funciones de primera clase. Lo que significa:
# - Se pueden asignar a variables
# - Se pueden pasar como argumentos a otras funciones
# - Pueden devolver otra función como resultado
# - Se pueden almacenar en estructuras de datos como listas o diccionarios

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

'''
Crea un simulador de pedidos de un restaurante utilizando callbacks.
Estará formado por una función que procesa pedidos.
Debe aceptar el nombre del plato, una callback de confirmación, una de listo y otra de entrega.
- Debe imprimir una confirmación cuando empiece el procesamiento.
- Debe simular un tiempo aleatorio entre 1 a 10 segundos entre  prcesos
- Debe invocar a cada callback siguiente un orden de procesado.
- Debe notificar que el plato está listo o ha sido entregado.


'''

print(greeting_process.__doc__)