'''
EXPLICACIÓN DE "n > 0 and (n & (n - 1)) == 0"

Para esta aplicación hemos utilizado las operaciones binarias para ver
si un número es potencia de 2:
1) Si escribimos las potencias de 2 en el sistema binario (base 2), vemos este patrón:
    decimal     binario             binario - 1
    2           10                  01
    4           100                 011
    8           1000                0111
    16          10000               01111

2) Si restamos uno nos da la columna de la derecha.
3) Si hacemos un AND lógico (&) siempre dará 0
'''




'''
¡El último videojuego de Dragon Ball ya está aquí!
Se llama Dragon Ball: Sparking! ZERO

Simula un torneo de Artes Marciales, al más puro estilo
de la saga, donde participarán diferentes luchadores, y el 
sistema decidirá quién es el ganador.

Luchadores:
- Nombre.
- Tres atributos: velocidad, ataque y defensa
  (con valores entre 0 a 100 que tú decidirás).
- Comienza cada batalla con 100 de salud.
Batalla:
- En cada batalla se enfrentan dos luchadores.
- El jugador con más velocidad comienza atacando.
- El daño se calcula restando el daño del ataque del 
  atacante menos la defensa del oponente.
- El oponente siempre tiene un 20 % de posibilidad de 
  esquivar el ataque.
- Si la defensa es mayor que el ataque, recibe un 10 %
  del daño de ataque.
- Después de cada turno y ataque, el oponente pierde salud.
- La batalla finaliza cuando un luchador pierde toda su salud.
Torneo:
- Un torneo solo es válido con un número de luchadores
  potencia de 2.
- El torneo debe crear parejas al azar en cada ronda.
- Los luchadores se enfrentan en rondas eliminatorias.
- El jugador avanza a la siguiente ronda hasta que solo
  quede uno.
- Debes mostrar por consola todo lo que sucede en el torneo, 
  así como el ganador.

PSEUDOCÓDIGO:
- Vamos a tener las siguientes clases:
  * Luchador:
    - Para iniciar: nombre, ataque, defensa y salud que se inicializa a 100
  * Torneo:
    - Método añadir participante: recibe el jugador como un diccionario
  


'''

import random

class Fighter:
    def __init__(self, name: str, atack: int, deffense: int, healthy=100):
        self.name = name
        self.atack = atack
        self.deffense = deffense
        self.healthy = healthy

class Tournament:
    list_of_players = []
    def __init__(self):
        #print("Torneo creado")
        pass

    def add_player(self, player: Fighter):
        self.player = player
        if Tournament.list_of_players:
            exists = False
            for existing_player in Tournament.list_of_players:
                #print(f"Comprobamos si {self.player.name} es igual a {existing_player.name}")
                if existing_player.name == self.player.name:
                    #print(f"Existe {self.player.name}, no hago nada y {exists} ahora es True")
                    exists = True
            if exists == False:    
                Tournament.list_of_players.append(self.player)
                #print(f"Comprobado que no existe {self.player.name} y añadido")
                return None
        else:
            Tournament.list_of_players.append(self.player)
            #print(f"Primer jugador añadido: {self.player.name}")

    def show_players(self):
        print("\nPor el momento se han inscrito en el torneo:")
        for player in self.list_of_players:
            print(player.name)

    def begin_tournament(self):
        # Si se cumple que "n > 0 and (n & (n - 1)) == 0" quiere decir que n es potencia de dos
        if  len(self.list_of_players) > 0 and (len(self.list_of_players) & (len(self.list_of_players) - 1)) == 0:
            oponent_one = random.randrange(1, len(self.list_of_players))
            Tournament.list_of_players.pop(oponent_one)
        else: 
            return False
        
'''

'''


fighter_one = Fighter("Goku", 90, 90)
fighter_two = Fighter("Krilin", 70, 70)
fighter_three = Fighter("Pikolo", 80, 90)
fighter_four = Fighter("Zell", 95, 95)
#fighter_five = Fighter("Zell", 95, 95)
#tournament.add_player(fighter_five)

tournament = Tournament()
tournament.add_player(fighter_one)
tournament.add_player(fighter_two)
tournament.add_player(fighter_three)
tournament.add_player(fighter_four)


#tournament.show_players()
print(tournament.begin_tournament())





""" def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(4)) """