from datetime import datetime, date, timedelta

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

day_one_september = (datetime.strptime("2026, 9, 1", "%Y, %m, %d"))
print(day_one_september.weekday())

print("\tL\tM\tMx\tJ\tV\tS\tD")






'''
Vamos a imprimir que día de la semana es el 01 de septiembre este año (entre 1 y 7) -> 1, por lo que es martes
Vamos a imprimirlo a modo calendario:
    Vamos a poner arriba L, M, Mx...
    Vamos a colocar el primer día en su lugar asociado a una de las 7 letras
        Dos bucles for: uno del 1 al 6 y otro del 0 al 6 para los días de la semana
        En el primero tengo que ver si el número

    Vamos a hacer dos bucles para rellenar el resto
'''



'''
EJERCICIO:
Cada año se celebra el Batman Day durante la tercera semana de septiembre...
¡Y este año cumple 85 años! Te propongo un reto doble:

# Reto 1:
Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
su 100 aniversario.
'''


