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
    def __init__(self, name: str, velocity: int, atack: int, deffense: int, healthy=100):
        self.velocity = velocity
        self.name = name
        self.atack = atack
        self.deffense = deffense
        self.healthy = healthy

    def reset_health(self):
        self.healthy = 100


class Fight_oponents:
    def __init__(self, fighter_one: Fighter, fighter_two: Fighter):
        self.fighter_one = fighter_one
        self.fighter_two = fighter_two
        print(f"\n⚔️  {self.fighter_one.name} VS {self.fighter_two.name}")
        self.winner = self.fight(self.fighter_one, self.fighter_two)

    def swap_turns(self):
        self.attacker, self.defender = self.defender, self.attacker

    def fight(self, fighter_one, fighter_two):
        # 1. Decidimos quién empieza según la velocidad
        if fighter_one.velocity >= fighter_two.velocity:
            self.attacker, self.defender = fighter_one, fighter_two
        else:
            self.attacker, self.defender = fighter_two, fighter_one

        # 2. Bucle de combate
        while self.attacker.healthy > 0 and self.defender.healthy > 0:
            
            # ¿Esquiva? (20% de probabilidad)
            if random.random() < 0.20:
                print(f"  💨 ¡{self.defender.name} esquiva el golpe!")
                self.swap_turns()
                continue

            # Cálculo del daño
            if self.attacker.atack > self.defender.deffense:
                damage = self.attacker.atack - self.defender.deffense
            else:
                damage = self.attacker.atack * 0.10

            # Aplica daño
            self.defender.healthy -= damage
            print(f"  💥 {self.attacker.name} ataca a {self.defender.name} e inflige {damage:.1f} de daño. (Vida restante: {max(0, self.defender.healthy):.1f})")

            # Comprobar si el defensor ha caído
            if self.defender.healthy <= 0:
                print(f"  ✨ ¡{self.attacker.name} WINS!")
                return self.attacker

            # Cambiamos el turno
            self.swap_turns()


class Tournament:
    def __init__(self):
        self.list_of_players = []

    def add_player(self, player: Fighter):
        # Evitamos duplicados comprobando el nombre
        if not any(p.name == player.name for p in self.list_of_players):
            self.list_of_players.append(player)

    def show_players(self):
        print("\nPor el momento se han inscrito en el torneo:")
        for player in self.list_of_players:
            print(f"- {player.name}")

    def begin_tournament(self):
        n = len(self.list_of_players)
        
        # Validar potencia de 2
        if not (n > 0 and (n & (n - 1)) == 0):
            print(f"❌ El torneo no es válido: hay {n} participantes y debe ser una potencia de 2.")
            return

        print(f"\n🔥 ¡Comienza el Torneo con {n} participantes! 🔥")
        round_number = 1

        while len(self.list_of_players) > 1:
            print(f"\n==================== RONDA {round_number} ====================")
            winners = []
            
            # Mezclar para parejas aleatorias
            random.shuffle(self.list_of_players)

            while len(self.list_of_players) > 0:
                p1 = self.list_of_players.pop()
                p2 = self.list_of_players.pop()

                combat = Fight_oponents(p1, p2)
                winner = combat.winner
                
                winner.reset_health()
                winners.append(winner)

            self.list_of_players = winners
            round_number += 1

        champion = self.list_of_players[0]
        print(f"\n🏆 ¡EL GANADOR ABSOLUTO DEL TORNEO ES {champion.name}! 🏆")


# --- PRUEBA DEL PROGRAMA ---
fighter_one = Fighter("Goku", 90, 90, 90)
fighter_two = Fighter("Krilin", 50, 70, 70)
fighter_three = Fighter("Piccolo", 70, 80, 90)
fighter_four = Fighter("Cell", 100, 95, 95)

tournament = Tournament()
tournament.add_player(fighter_one)
tournament.add_player(fighter_two)
tournament.add_player(fighter_three)
tournament.add_player(fighter_four)

tournament.show_players()
tournament.begin_tournament()






""" def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(4)) """