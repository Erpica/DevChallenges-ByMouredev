from datetime import datetime, date, timedelta
import calendar



fecha = datetime(2026, 6, 23, 14, 30)
fecha_2 = datetime.strptime("2026, 6, 23, 14, 30", "%Y, %m, %d, %H, %M")
print(type(fecha))
print(type(fecha_2))


# _today = datetime.today() # Más antigüo, se usa mejor .now()

_today = datetime.now()
_tomorrow = _today + timedelta(days=1)
_yesterday = _today - timedelta(days=1)

print(f"Ayer: {_yesterday}\nHoy: {_today}\nY mañana: {_tomorrow}")

# print(_today.weekday()) # Número del día de la semana entre el 0 y el 6

_year = "2026"
_month = "9" # Septiembre
day_one_september = (datetime.strptime(f"{_year}, {_month}, 1", "%Y, %m, %d"))

# Buscando el último día del mes con timedelta:
last_day = datetime(int(_year), int(_month)+1, 1) - timedelta(days=1)
last_day = int(last_day.strftime("%d"))


print("\n\t\t\tCalendario\n")
print("\tL\tM\tMx\tJ\tV\tS\tD")

number_of_day_to_paint = 1
day_one_of_week = day_one_september.weekday()

while number_of_day_to_paint <= last_day:
    if number_of_day_to_paint == 1:
        print("\t" * day_one_of_week, end="")
    elif (number_of_day_to_paint -1 + day_one_of_week) % 7 == 0:
        print()
    print(f"\t{number_of_day_to_paint}", end="")
    number_of_day_to_paint +=1


print("\n\n\n\nPracticando un poco con el módulo calendar:")
# Calculador de meses:
primer_dia_semana, total_dias = calendar.monthrange(2026, 9)
print(primer_dia_semana, total_dias)
print(calendar.monthrange(2026, 9))

# Comprobar si un año es bisiesto
print(calendar.isleap(2026))  # Devuelve False
print(calendar.isleap(2028))  # Devuelve True

print("Bisiestos: ", end="")
for i in range (1980, 2000):
    if calendar.isleap(i):
        print(f"{i}", end=", ")
print()

# Días de la semana en listas (una por semana)
semanas = calendar.monthcalendar(2026, 9)
print(semanas)

for nombre in calendar.day_name:
    print(nombre, end=", ")  # Imprime: lunes, martes, miércoles...

# Calenadrio de un mes:
print(calendar.month(2026, 9))

# print(calendar.calendar(2026)) # -> Imprime el calentario del año.

# print(calendar.weekday(2026, 9, 9)) # -> Imprime el número del día de la semana: Lunes 0, domingo 6

# Nombre de un día concreto
one_day_name = calendar.weekday(2026, 9, 9)
print(calendar.day_name[one_day_name])
# ... y si lo quiero en castellano:
import locale
locale.setlocale(locale.LC_TIME, 'spanish') # Para Windows
# locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Linux/Mac
one_day_name = calendar.weekday(2026, 9, 9)
print(calendar.day_name[one_day_name])  # miércoles


# Obtener el número de días que tiene un mes:
days = calendar.monthrange(2026, 2)[1]
print(f"Febrero tiene {days} días.")

'''
🧠 Resumen visual
Función	        ¿Qué hace?
month()	        Calendario de un mes
calendar()	    Calendario de un año
weekday()	    Día de la semana de una fecha
isleap()	    ¿Año bisiesto?
leapdays()	    Nº de bisiestos entre años
monthrange()	Día del primer día y total de días
TextCalendar()	Calendario personalizado en texto
HTMLCalendar()	Calendario en HTML

🚫 Lo que NO hace calendar (y que está en otros módulos)
- No maneja operaciones aritméticas con fechas (eso es para datetime y timedelta).
- No trabaja con zonas horarias (eso es para pytz o zoneinfo).
- No convierte strings a fechas (eso es para datetime.strptime).
'''