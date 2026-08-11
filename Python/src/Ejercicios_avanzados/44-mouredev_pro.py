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

NOTA: Para usar zoneinfo en Windows, tengo que instalar el paquete tzdata:
uv add tzdata
'''

from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import time
import threading

def check_var_and_types(the_end_time, the_end_time_local, countdown):
  print(f"{'- the_end_time:':<22} {str(the_end_time):<25} {type(the_end_time)}")
  print(f"{'- the_end_time_local:':<22} {str(the_end_time_local):<25} {type(the_end_time_local)}\n")
  print(f"{'type(the_end_time_local.tzinfo): ':<35}{type(the_end_time_local.tzinfo)}")
  print(f"{'type(countdown): ':<35}{type(countdown)}\n")
    


def clear_screen():
    print("\033c", end="")

def show_countdown(the_end_time, countdown):
  delta = countdown

  days = delta.days
  total_seconds = delta.seconds

  hours = total_seconds // 3600
  minutes = (total_seconds % 3600) // 60
  seconds = total_seconds % 60

  print(f"Faltan {days} días, {hours:02d} horas, {minutes:02d} minutos, {seconds:02d} segundos")
  print(f"\nLa hora \"H\" será: {datetime.strftime(the_end_time, "%d/%m/%Y - %H:%M:%S")}\n\n")

   



def countdown(target_day_utc, target_day_local):
  while True:

    # Obtenemos la hora actual del sistema explícitamente en UTC
    now_utc = datetime.now(timezone.utc)

    # Calculamos la diferencia
    delta = target_day_utc - now_utc

    now = datetime.now().replace(microsecond=0)
    target_day = the_end_time.replace(microsecond=0)
    countdown =  target_day - now

    # Si el tiempo total en segundos llega a cero o menos, se acabó
    if delta.total_seconds() <= 0:
        clear_screen()
        print("🚀 ¡Cuenta atrás finalizada! ¡Lanzamiento completado!")
        break

    clear_screen()
    show_countdown(target_day_local, delta)
    time.sleep(1)


#check_var_and_types(the_end_time, the_end_time_local, countdown)
#print(the_end_time_local.tzinfo) # Para ver la zona a la que pertenece la hora fin

#the_end = input("Introduce el momento en que finaliza la cuenta atrás (dd/mm/aa - hh:mm:ss): ")
the_end_text = "12/08/2026 - 15:00:00"
the_end_time = datetime.strptime(the_end_text, "%d/%m/%Y - %H:%M:%S")

the_end_time_local = the_end_time.replace(tzinfo=ZoneInfo("Europe/Madrid"))

# 3. Transformar a UTC
the_end_time_utc = the_end_time_local.astimezone(timezone.utc)
  

countdown_thread = threading.Thread(target=countdown, args=(the_end_time_utc, the_end_time_local))
countdown_thread.start()
countdown_thread.join()
