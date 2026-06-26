'''
EJERCICIO:
Cada año se celebra el Batman Day durante la tercera semana de septiembre...
¡Y este año cumple 85 años! Te propongo un reto doble:

# Reto 1:
Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
su 100 aniversario.
'''

import calendar

#september_calendar = calendar.month(2026, 9)
#print(september_calendar)

# 85 aniversario en 2026


def find_week(year: int) -> str:
    '''
    Calcula el sábado de la tercera semana del año que se le pasa como argumento.

    Recibe: Un int que representa el año.

    Devuelve: Un str que contiene el día que corresponde al sábado de la tercera semana del mes de septiembre del año pasado como argumento.
    '''

    first_day_month = calendar.weekday(year, 9, 1)
    name_of_day = calendar.day_name[first_day_month]

    match name_of_day:
        case "Monday":
            day_of_event = "20"
        case "Tuesday":
            day_of_event = "19"
        case "Wednesday":
            day_of_event = "18"
        case "Thursday":
            day_of_event = "17"
        case "Friday":
            day_of_event = "16"
        case "Saturday":
            day_of_event = "15"
        case "Sunday":
            day_of_event = "14"

    return f"El año {year} el envento será el sábado {day_of_event} de septiembre."

'''
# Reto 1
for year in range (2026, 2026+25):
    print(find_week(year))
'''
'''
# Reto 2:
EJERCICIO:

Crea un programa que implemente el sistema de seguridad de la Batcueva.
Este sistema está diseñado para monitorear múltiples sensores distribuidos
por Gotham, detectar intrusos y activar respuestas automatizadas.
Cada sensor reporta su estado en tiempo real y Batman necesita un programa
que procese estos datos para tomar decisiones estratégicas.
Requisitos:
- El mapa de Gotham y los sensores se representan con una cuadrícula 20x20.
- Cada sensor se identifica con una coordenada (x, y) y un nivel
  de amenaza entre 0 y 10 (número entero).
- Batman debe concentrar recursos en el área más crítica de Gotham.
- El programa recibe un listado de tuplas representando coordenadas de los
  sensores y su nivel de amenaza. El umbral de activación del protocolo de 
  seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
Acciones: 
- Identifica el área con mayor concentración de amenazas
  (sumatorio de amenazas en una cuadrícula 3x3).
- Si el sumatorio de amenazas es mayor al umbral, activa el 
  protocolo de seguridad.
- Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
  la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
- Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de 
  sus amenazas, la distancia a la Batcueva y si se debe activar el 
  protocolo de seguridad.
'''

import random



class Matrix:
    def __init__(self):
        self.matrix_dict = {}
        for x in range (1, 21):
            for y in range (1, 21):
                self.matrix_dict[x,y] = 0
                #print(self.matrix_dict[(x, y)])
    
    def show_matrix(self):
        for x in range(1, 21):
            for y in range(1, 21):
                print(f"{self.matrix_dict[(x,y)]}", end="\t ")
            print()

    def fill_theat(self, number_of_theats):
        self.number_of_threats = number_of_theats
        count = 1
        seted_threats = []

        while count <= number_of_theats:
            random_number = random.randint(1,10)
            random_x = random.randint(1,20)
            random_y = random.randint(1,20)
            if (random_x,random_y) not in seted_threats:
                self.matrix_dict[random_x,random_y] = random_number
                seted_threats.append((random_x,random_y))
                count +=1

    def count_threats(self):
        count = 0
        for x in range(1, 21):
            for y in range(1, 21):
                if self.matrix_dict[(x,y)] > 0:
                    print(f"{self.matrix_dict[(x,y)]}", end=", ")
                    count += 1
        print(f"\nTotal: {count} ataques.")
            
    def identify_zone(self):
        self.max_danger = -1
        self.zone = None
        
        for x in range(2, 20):
            for y in range(2, 20):
                # Desempaquetamos lo que nos da check_submatrix
                coordenadas, total_amenazas = self.check_submatrix(x, y)
                
                # Ahora comparamos limpiamente número contra número
                if total_amenazas > self.max_danger:
                    self.max_danger = total_amenazas
                    self.zone = (coordenadas, total_amenazas) # Guarda ((x, y), total)
                    
        return self.zone
        

    def check_submatrix(self, center_x, center_y):
        total_threat = 0
        # dx y dy van a ser -1, 0, 1. Se lo sumamos al centro para mirar alrededor.
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                total_threat += self.matrix_dict[center_x + dx, center_y + dy]
                
        # Devolvemos la coordenada (en una tupla) junto con el total
        return (center_x, center_y), total_threat
        


# 1. Creamos la matriz y metemos 20 amenazas
bat_matrix = Matrix()
bat_matrix.fill_theat(20)
bat_matrix.show_matrix()
bat_matrix.count_threats() 

# 2. Llamamos al método inteligente que busca en todo el mapa
resultado_critico = bat_matrix.identify_zone()

if resultado_critico:
    (centro_x, centro_y), suma_amenazas = resultado_critico

    # 3. Cálculos estratégicos para Batman
    distancia_batcueva = abs(centro_x) + abs(centro_y)
    protocolo_activo = "SÍ" if suma_amenazas > 20 else "NO"

    # 4. Mostrar el reporte en consola
    print("\n📡 INFORME DE INTELIGENCIA DE LA BATCUEVA")
    print("-" * 40)
    print(f"📍 Centro más amenazado: Coordenada ({centro_x}, {centro_y})")
    print(f"🔥 Sumatorio de nivel de amenaza: {suma_amenazas}")
    print(f"🚗 Distancia a la Batcueva (0,0): {distancia_batcueva} bloques")
    print(f"⚠️ ¿Activar protocolo de seguridad?: {protocolo_activo}")
    print("-" * 40)

        
""" 
# (0,0):0
# (1,0):0
# (2,0):0
my_dict = {
    (0,0): 0,
    (1,0): 1,
    (2,0): 2,
    (3,0): 3
}

print (my_dict[(3,0)])
 """