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

# Calculador de año bisiesto:
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
    print(nombre)  # Imprime: lunes, martes, miércoles...