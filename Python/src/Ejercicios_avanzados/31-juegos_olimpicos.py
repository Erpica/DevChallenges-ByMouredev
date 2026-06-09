'''
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (golden, silver y bronze) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 '''



import random

class Deportist:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

class Event:
    '''
    Clase que representa un evento deportivo. 

    Recibe de el nombre del deporte y una lista con los participantes

    Devuelve una lista con el orden de los participantes, 
    siendo los tres primeros los que reciben medallas.
    '''
    def __init__(self, nombre_deporte: str):
        self.nombre_deporte = nombre_deporte
        self.participants = []
    
    def add_participant(self, deportist: Deportist):
        self.participants.append(deportist)

class MasterRegister:
    def __init__(self):
        self.list_of_deportists = []
        self.list_of_events = []        

    def add_deportist(self, deportist: Deportist):
        existing_names = [d.name for d in self.list_of_deportists]

        if deportist.name not in existing_names:
            self.list_of_deportists.append(deportist)
            #print("Añadido con éxito")
        else:
            print("Este deportista ya está en la lista")

    def add_event(self, event: Event):
        if event not in self.list_of_events:
            self.list_of_events.append(event)
        else:
            print ("Ese evento ya se ha agregado anteriomente.")

class OlympicSimulator:
    def event_simulation(self, event: Event):
        if len(event.participants) < 3:
            print("Para realizar el evento se necesitan, al menos, tres participantes.")
        else:
            random.shuffle(event.participants)
            firts_clasificated = event.participants[0]
            second_clasificated = event.participants[1]
            third_clasificated = event.participants[2]

            return {
                "golden": firts_clasificated,
                "silver": second_clasificated,
                "bronze": third_clasificated
            }
    

class MedalHistory:
    def __init__(self):
        self.medal_history = []
    
    def save_result(self, event: Event, simulator_result: OlympicSimulator):
        self.medal_history.append([event, simulator_result])

    def show_medals(self):
        for a_result in self.medal_history:
            evento = a_result[0]
            ganadores = a_result[1]
            print(f"Evento: {evento.nombre_deporte}")
            print(f"1º -   Oro : {ganadores['golden'].name} ({ganadores['golden'].country})")
            print(f"2º -  Plata: {ganadores['silver'].name} ({ganadores['silver'].country})")
            print(f"3º - Bronce: {ganadores['bronze'].name} ({ganadores['bronze'].country})")
        
    def show_country_ranking(self):
        number_of_countries = {} # Diccionario vacío para acumular medallas
        
        for registro in self.medal_history:
            winners = registro[1]

            country_gold = winners['golden'].country
            country_silver = winners['silver'].country
            country_bronze = winners['bronze'].country
            
            if country_gold not in number_of_countries:
                number_of_countries[country_gold] = 1
            else:
                number_of_countries[country_gold] += 1
                
            # 3. Sumamos la medalla de PLATA al diccionario
            if country_silver not in number_of_countries:
                number_of_countries[country_silver] = 1
            else:
                number_of_countries[country_silver] += 1
                
            # 4. Sumamos la medalla de BRONCE al diccionario
            if country_bronze not in number_of_countries:
                number_of_countries[country_bronze] = 1
            else:
                number_of_countries[country_bronze] += 1

        # Al final, imprimimos el ranking total acumulado
        print("\n--- RANKING DE PAÍSES POR MEDALLAS ---")
        for country, medals in number_of_countries.items():
            print(f"{country}: {medals} medallas")



class OlympicMenu:
    def __init__(self, register: MasterRegister, simulator: OlympicSimulator, history: MedalHistory):
        self.register = register
        self.simulator = simulator
        self.history = history

    def start(self):
        while True:
            print("\n--- MENÚ JUEGOS OLÍMPICOS ---")
            print("1. Registrar evento deportivo")
            print("2. Registrar participante")
            print("3. Simular evento")
            print("4. Crear informes (Medallas y Ranking)")
            print("5. Salir")
            
            option = input("Selecciona una opción: ")
            
            if option == "1":
                deporte = input("Nombre del deporte: ")
                nuevo_evento = Event(deporte)
                self.register.add_event(nuevo_evento)
                print(f"Evento de {deporte} registrado.")
                
            elif option == "2":
                datos = input("Introduce el nombre y el país del deportista (separados por una coma): ")
                name, country = datos.split(",")
                
                # .strip() elimina espacios en blanco invisibles que se queden en los lados
                one_deportist = Deportist(name.strip(), country.strip())
                self.register.add_deportist(one_deportist)
                
                sport = input("¿A qué evento deportivo quieres apuntarlo?: ").strip()
                
                # Buscamos si el evento ya existe en el registro global
                evento_encontrado = None
                for ev in self.register.list_of_events:
                    if ev.nombre_deporte.lower() == sport.lower():
                        evento_encontrado = ev
                        break
                
                if evento_encontrado:
                    evento_encontrado.add_participant(one_deportist)
                    print(f"Atleta {one_deportist.name} apuntado con éxito a {sport}.")
                else:
                    print(f"El evento de {sport} no existe. Regístralo primero en la opción 1.")
            elif option == "3":
                sport = input("¿Qué evento deseas simular?: ").strip()
                evento_encontrado = None
                for ev in self.register.list_of_events:
                    if ev.nombre_deporte.lower() == sport.lower():
                        evento_encontrado = ev
                        break
                
                if evento_encontrado:
                    resultado = self.simulator.event_simulation(evento_encontrado)
                    if resultado: # Si la simulación fue exitosa (mínimo 3 participantes)
                        self.history.save_result(evento_encontrado, resultado)
                        print(f"¡Simulación completada! Se han asignado las medallas de {evento_encontrado.nombre_deporte}.")
                else:
                    print("Ese evento no existe en el registro.")
                    
            elif option == "4":
                self.history.show_medals()
                self.history.show_country_ranking()
            elif option == "5":
                print("¡Gracias por participar en París 2024!")
                break

# --- INICIACIÓN DEL PROGRAMA (Inyección de dependencias) ---
registro_global = MasterRegister()
simulador_olimpico = OlympicSimulator()
historial_medallas = MedalHistory()

menu = OlympicMenu(registro_global, simulador_olimpico, historial_medallas)
menu.start()









'''
entes:                                                      clases:
eventos deportivos                                          Eventos (nombre_deporte) // ListaDeEventos().añadir_evento()
participantes (con nombre y país)                           participante (nombre, país, deporte: list)
simular eventos -aleatorio- (participantes: mínimo 3)       DiaDePartido(evento, Deportistas)
asignar medallas (en función del resultado del evento)      
mostrar ganadores (por evento)                              
ranking de paises (por medallas)                            


'''