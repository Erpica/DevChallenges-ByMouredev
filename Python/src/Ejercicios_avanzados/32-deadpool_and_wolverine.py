'''
¡Deadpool y Wolverine se enfrentan en una batalla épica!
Crea un programa que simule la pelea y determine un ganador.
El programa simula un combate por turnos, donde cada protagonista posee unos
puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
de regeneración y evasión de ataques.
Requisitos:
1. El usuario debe determinar la vida inicial de cada protagonista.
2. Cada personaje puede impartir un daño aleatorio:
    - Deadpool: Entre 10 y 100.
    - Wolverine: Entre 10 y 120.
3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
4. Cada personaje puede evitar el ataque contrario:
    - Deadpool: 25 % de posibilidades.
    - Wolverine: 20 % de posibilidades.
5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
Acciones: 
1. Simula una batalla.
2. Muestra el número del turno (pausa de 1 segundo entre turnos).
3. Muestra que pasa en cada turno.
4. Muestra la vida en cada turno.
5. Muestra el resultado final.
'''
import random
import time

class Deadpool:

    def __init__(self, life):
        # self.life = input("Introduce la vida inicial de Deadpool (entre 100 y 10000)")
        self.life = life
        self.is_regenerating = False

    def atack(self):
        return random.randint(10, 100)
    
    def defend(self, damage: int) -> int:
        if random.random() <= 0.25:
            return True
        
        self.life -= damage
        return False
    
    def show_life(self):
        return self.life

class Wolverine:
    def __init__(self, life):
        # self.life = input("Introduce la vida inicial de Wolverine (entre 100 y 10000)")
        self.life = life
        self.is_regenerating = False

    def atack(self):
        return random.randint(10, 120)
    
    def defend(self, damage: int) -> int:
        if random.random() <= 0.2:
            return True
        self.life -= damage
        return False

    def show_life(self):
        return self.life

class MainBattle:
    finished = False

    def __init__(self):
        
        #life_deadpool = int(input("Introduce la vida inicial de Deadpool (ej: 500): "))
        #life_wolverine = int(input("Introduce la vida inicial de Wolverine (ej: 500): "))
        life_deadpool = 150 # Inicializo para pruebas
        life_wolverine = 150 # Inicializo para pruebas

        self.deadpool = Deadpool(life_deadpool)
        self.wolverine = Wolverine(life_wolverine)
        self.current_turn = 1

    def execute_turn(self, attacker, defender, attacker_name, defender_name, max_damage):
        if attacker.is_regenerating:
            print(f"{attacker_name} está aturdido del golpe anterior y no puede atacar.")
            attacker.is_regenerating = False
            return False

        damage = attacker.atack()
        print(f"{attacker_name} golpea con {damage} de daño.")

        avoiding = defender.defend(damage)
        if avoiding:
            print(f"{defender_name} ha esquivado el ataque.")
        else:
            if damage == max_damage:
                print(f"Golpe máximo. {defender_name} queda aturdido.")
                defender.is_regenerating = True
            life = max(0, defender.life)
            print(f"{defender_name} recibe un golpe. Vida restante {life}")
        if defender.life <= 0:
            print(f"{defender_name} ha muerto.")
            print(f"{attacker_name} ha GANADO.")
            return True
        return False

    def fight(self):
        print("\n\n  - Bienvenido a la batalla final -")

        while self.deadpool.life > 0  and self.wolverine.life > 0:

            print(f"\n🔔 * [ TURNO {self.current_turn} ] *")
            print(f"Vida actual -> Deadpool: {self.deadpool.life} HP | Wolverine: {self.wolverine.life} HP")
            print("-" * 40)

            if random.choice([True, False]):
                battle_over = self.execute_turn(self.deadpool, self.wolverine, "Deadpool", "Wolverine", 100)
                if not battle_over:
                    battle_over = self.execute_turn(self.wolverine, self.deadpool, "Wolverine", "Deadpool", 120)
            else:
                battle_over = self.execute_turn(self.wolverine, self.deadpool, "Wolverine", "Deadpool", 120)
                if not battle_over:
                    battle_over = self.execute_turn(self.deadpool, self.wolverine, "Deadpool", "Wolverine", 100)

            if battle_over:
                break

            self.current_turn += 1
            time.sleep(1)



"""             print (f"")
            components = ["Wolverine", "Deadpool"]
            random.shuffle(components)
            if components[0] == "Wolverine":
                # print("Wolverine")
                this_atack = self.wolverine.atack() # Vamos a ver con cuanto ataca
                current_life = self.deadpool.defend(this_atack) # Vamos a ver la vida que le queda a deadpool después del ataque
                if current_life <= 0:
                    print(f"\n  *  Turno {self.current_turn}  * \n - Ataca Wolverine:\nAtaque: {this_atack}\nVida restante de Deadpool: 0\n\n     ** Ganador: Wolverine!! \n**")
                    self.finished = True
                else:
                    print(f'''
*  Turno {self.current_turn}  * 
- Ataca Wolverine:
Ataque: {this_atack}
- Vida restante: 
Deadpool: {current_life}
Wolverine: {self.wolverine.show_life()}
                          ''')
            else:
                # print("Deadpool")
                this_atack = self.deadpool.atack() # Vamos a ver con cuanto ataca
                current_life = self.wolverine.defend(this_atack) # Vamos a ver la vida que le queda a wolverine después del ataque
                if current_life <= 0:
                    print(f"\n  *  Turno {self.current_turn}  * \n - Ataca Deadpool:\nAtaque: {this_atack}\nVida restante de Wolverine: 0\n\n     ** Ganador: Deadpool!! **\n")
                    self.finished = True
                else:
                    print(f'''
*  Turno {self.current_turn}  * 
- Ataca Deadpool:
Ataque: {this_atack}
- Vida restante: 
Wolverine: {current_life}
Deadpool: {self.deadpool.show_life()}
                          ''')
            self.current_turn += 1
            time.sleep(1) """
    

MainBattle().fight()

