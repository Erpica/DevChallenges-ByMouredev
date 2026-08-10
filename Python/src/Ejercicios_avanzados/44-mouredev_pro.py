'''
EJERCICIO:
¡El 12 de noviembre lanzo mouredev pro!
El campus de la comunidad para estudiar programación de
manera diferente: https:mouredev.pro

Crea un programa que funcione como una cuenta atrás.

- Al inciarlo tendrás que indicarle el día, mes, año, 
  hora, minuto y segundo en el que quieres que finalice.
- Deberás transformar esa fecha local a UTC.
- La cuenta atrás comenzará y mostrará los días, horas, 
  minutos y segundos que faltan.
- Se actualizará cada segundo y borrará la terminal en
  cada nueva representación del tiempo restante.
- Una vez finalice, mostrará un mensaje.
- Realiza la ejecución, si el lenguaje lo soporta, en
un hilo independiente.
'''

from datetime import datetime, timedelta
import subprocess


def clear_screen():
    print("\033c", end="")

#the_end = input("Introduce el momento en que finaliza la cuenta atrás (dd/mm/aa - hh:mm:ss): ")
the_end = "10/08/2026 - 17:20:00"

the_end_time = datetime.strptime(the_end, "%d/%m/%Y - %H:%M:%S")
countdown = the_end_time - datetime.now()


print(type(countdown))
#countdown = datetime.strftime("%d/%m/%Y - %H:%M:%S")

#print(the_end_time.strftime("%d/%m/%Y - %H:%M:%S"))
#countdown = datetime.strptime(countdown, "%d/%m/%Y - %H:%M:%S")
print(countdown)

