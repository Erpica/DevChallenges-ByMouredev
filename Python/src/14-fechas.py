from datetime import datetime
import locale # por si quiero poner en castellano los días y meses

now = datetime.now()
birth_date = datetime(1980, 6, 15, 12, 0, 0)

print(now)
print(birth_date)

print(type(now))
print(type(now-birth_date))

diference = now-birth_date
print(f"Tengo {diference.days // 365} años.")

'''
# Extra:
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
(lo que se te ocurra)

'''
print(f"Día, mes y año: {birth_date.strftime("%d, %m y %y")}")
print(f"Hora, minuto y segundo: {birth_date.strftime("%h:%m:%S")}")
print(f"Día de año.: {int(birth_date.strftime("%j"))}")
print(f"Día de la semana: {birth_date.strftime("%A")}")
print(f"Nombre del mes.: {birth_date.strftime("%B")}")
print(birth_date.strptime("%d %m %y"))




print(birth_date.strftime("Yo nací el %d del mes %m, en el año %y"))



# import locale # Ya importado arriba. Lo pongo aquí para recordar que hace falta para esto:
from datetime import datetime

# 1. Configuramos el idioma del script a español
# En Windows se suele usar "es_ES" o "spanish"
# En Linux/Mac se usa "es_ES.UTF-8"
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8") # Intenta formato Linux/Mac/Universal
except locale.Error:
    locale.setlocale(locale.LC_TIME, "spanish") # Alternativa para Windows

# Tu código de prueba
birth_date = datetime(1980, 5, 1)

print(f"Día de la semana: {birth_date.strftime('%A')}")
print(f"Nombre del mes.: {birth_date.strftime('%B')}")


'''
Directiva       Significado                                                                     Ejemplo                             

%a              Día de la semana como nombre abreviado según la configuración regional.         Sun, Mon, …, Sat (en_US); So, Mo, …, Sa (de_DE)
%A              Día de la semana como nombre completo de la localidad.                          Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE)
%w              Día de la semana como un número decimal, donde 0 es domingo y 6 es sábado.      0, 1, …, 6
%d              Día del mes como un número decimal rellenado con ceros.                         01, 02, …, 31

%b              Mes como nombre abreviado según la configuración regional.                      Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE)
%B              Mes como nombre completo según la configuración regional.                       January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE)
%m              Mes como un número decimal rellenado con ceros.                                 01, 02, …, 12

%y              Año sin siglo como un número decimal rellenado con ceros.                       00, 01, …, 99
%Y              Año con siglo como número decimal.                                              0001, 0002, …, 2013, 2014, …, 9998, 9999

%H              Hora (reloj de 24 horas) como un número decimal rellenado con ceros.            00, 01, …, 23
%I              Hora (reloj de 12 horas) como un número decimal rellenado con ceros.            01, 02, …, 12

%M              Minuto como un número decimal rellenado con ceros.                              00, 01, …, 59
%S              Segundo como un número decimal rellenado con ceros.                             00, 01, …, 59
%W              Número de semana del año (lunes como primer día de la semana) como un número decimal con ceros. Todos los días de un nuevo año que preceden al primer lunes se consideran en la semana 0.           00, 01, …, 53
%j              Día del año como un número decimal rellenado con ceros.                         001, 002, …, 366

%p              El equivalente de la configuración regional de AM o PM.                         AM, PM (en_US); am, pm (de_DE)
%Z              Nombre de zona horaria (cadena de caracteres vacía si el objeto es naíf (naive)).                                               (vacío), UTC, GMT



%f              Microsegundo como número decimal, con ceros hasta 6 dígitos.                    000000, 000001, …, 999999
%z              Desplazamiento (offset) UTC en la forma ±HHMM[SS[.ffffff]] (cadena de caracteres vacía si el objeto es naíf (naive)).           (vacío), +0000, -0400, +1030, +063415, -030712.345216
%U              Número de semana del año (domingo como primer día de la semana) como un número decimal con ceros. Todos los días de un nuevo año que preceden al primer domingo se consideran en la semana 0.       00, 01, …, 53
%c              Representación apropiada de fecha y hora de la configuración regional.          Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE)
%x              Representación de fecha apropiada de la configuración regional.                 08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE)
%X              Representación de la hora apropiada de la configuración regional.               21:30:00 (en_US); 21:30:00 (de_DE)
'''