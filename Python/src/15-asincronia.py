import datetime
import time
import asyncio

'''
Crea un programa capaz de ejecutar de manera asíncrona una función que tardará en finalizar
un número concreto de segundos parametrizables. También debes poder asignarle un nombre.
La función imprime su nombre, cuándo empieza, el tiempo que durará su ejecución y cuando finaliza.
'''

# async para tener la capacidad de ejecutar la función de manera asíncrona
async def task(name: str, duration: int):
    print (
        f"Tarea: {name}. Duración: {duration}s. Inicio: {datetime.datetime.now()}")
    #time.sleep(duration) # Esto bloquea la asincronía
    await asyncio.sleep(duration)
    print (
        f"Tarea: {name}. Fin: {datetime.datetime.now()}")

# asuncio.run para ejecutar la función de manera asíncrona. Si no no se ejecuta porque se definió con async. 
asyncio.run(task("1", 2))


'''
# Extra
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
- Una función C que dura 3 segundos.
- Una función B que dura 2 segundos.
- Una función A que dura 1 segundos.
- Una función D que dura 1 segundos.
- Las funciones C, B y A se ejecutan en paralelo.
- La función D comienza su ejecución cuando las 3 anteriores han finalizado.
'''



async def async_tasks():
    # Para ejecutar en paralelo varias tareas, usamos asyncio.gather, que recibe una lista de tareas a ejecutar.
    # await para que las vaya poniendo en segundo plano. Tiene que estar dentro de una función async, porque si no no se puede usar await.
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

asyncio.run(async_tasks())