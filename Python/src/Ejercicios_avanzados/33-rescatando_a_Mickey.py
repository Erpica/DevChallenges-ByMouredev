'''
¡Disney ha presentado un montón de novedades en su D23!
Pero... ¿Dónde está Mickey?
Mickey Mouse ha quedado atrapado en un laberinto mágico
creado por Maléfica.
Desarrolla un programa para ayudarlo a escapar.
Requisitos:
1. El laberinto está formado por un cuadrado de 6x6 celdas.
2. Los valores de las celdas serán:
    - ⬜ Vacío
    - ⬛ Obstáculo
    - 🐭 Mickey
    - 🚪 Salida
Acciones:
1. Crea una matriz que represente el laberinto (No hace falta
que se genere de manera automática).
2. Interactúa con el usuario por consola para preguntarle hacia
donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
3. Muestra la actualización del labrerinto tras cada desplazamiento.
4. Valida todos los movimientos, teniendo en cuenta los límites
del laberinto y los obstáculos. Notifica al usuario.
5. Finaliza el programa cuando Mickey llegue a la salida.
'''

import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#clear_screen()



class MickeyLabyrinth:
    def __init__(self):
        self.labyrinth = [
          #0     #1    #2    #3     #4     #5          -> primera coordenada al acceder a la matriz        
        ["⬛", "🐭", "⬛", "⬛", "⬛", "⬛", ], # 0 -> segunda
        ["⬛", "⬜", "⬜", "⬜", "⬜", "⬛", ], # 1
        ["⬛", "⬜", "⬛", "⬜", "⬛", "⬛", ], # 2
        ["⬛", "⬜", "⬛", "⬜", "⬛", "⬛", ], # 3
        ["⬛", "⬛", "⬛", "⬜", "⬜", "⬜", ], # 4
        ["⬛", "⬛", "⬛", "⬛", "⬛", "🚪", ], # 5
        ]
        #print(self.labyrinth[0][1])
        self.coordinate_y = 0
        self.coordinate_x = 0
        self.game_over = False  # Añadido para controlar el fin del juego
        self.locate_mickey()

    def locate_mickey(self):
        for line_number, line in enumerate(self.labyrinth):
            for col_number, character in enumerate(line):
                if character == "🐭":
                    self.coordinate_y = line_number
                    self.coordinate_x = col_number
                    return
        
    def show_labyrinth(self):
        clear_screen()  # Limpiar pantalla antes de mostrar
        for line in self.labyrinth:
            print(" ".join(line))
        print()
                
    def move_mickey_down(self):
        if self.coordinate_y + 1 > 5:
            print("No puedes salir del límite inferior.")
            return False
        celda_destino = self.labyrinth[self.coordinate_y + 1][self.coordinate_x]
        if celda_destino == "⬛":
            print("No puedes mover en esa posición porque hay un obstáculo.")
            input("Pulsa enter para continuar...")
            return False
        if celda_destino == "🚪": 
            print("\nHas conseguido ayudar a escapar a Mickey.\n       -- ¡¡Enhorabuena!!--")
            self.game_over = True
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "⬜"
        self.coordinate_y += 1
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "🐭"

    def move_mickey_up(self):
        #print(f"a ver que pasa x: {x} y: {y}")
        if self.coordinate_y -1 < 0:
            print("No puedes salir del límite superior.")
            return False
        celda_destino = self.labyrinth[self.coordinate_y - 1][self.coordinate_x]
        if celda_destino == "⬛":
            print("No puedes mover en esa posición porque hay un obstáculo.")
            input("Pulsa enter para continuar...")
            return False
        if celda_destino == "🚪": 
            print("\nHas conseguido ayudar a escapar a Mickey.\n       -- ¡¡Enhorabuena!!--")
            self.game_over = True
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "⬜"
        self.coordinate_y -= 1
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "🐭"
        return True

    def move_mickey_left(self):
        #print(f"a ver que pasa x: {x} y: {y}")
        if self.coordinate_x -1 < 0:
            print("No puedes salir del límite izquierdo.")
            return False
        celda_destino = self.labyrinth[self.coordinate_y][self.coordinate_x - 1]
        if celda_destino == "⬛":
            print("No puedes mover en esa posición porque hay un obstáculo.")
            input("Pulsa enter para continuar...")
            return False
        if celda_destino == "🚪": 
            print("\nHas conseguido ayudar a escapar a Mickey.\n       -- ¡¡Enhorabuena!!--")
            self.game_over = True
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "⬜"
        self.coordinate_x -= 1
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "🐭"
        return True

    def move_mickey_right(self):
        #print(f"a ver que pasa x: {x} y: {y}")
        if self.coordinate_x +1 > 5:
            print("No puedes salir del límite derecho.")
            return False
        celda_destino = self.labyrinth[self.coordinate_y][self.coordinate_x + 1]
        if celda_destino == "⬛":
            print("No puedes mover en esa posición porque hay un obstáculo.")
            input("Pulsa enter para continuar...")
            return False
        if celda_destino == "🚪": 
            print("\nHas conseguido ayudar a escapar a Mickey.\n       -- ¡¡Enhorabuena!!--")
            self.game_over = True
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "⬜"
        self.coordinate_x += 1
        self.labyrinth[self.coordinate_y][self.coordinate_x] = "🐭"
        return True


        
            

class PlayMickeyLabyrinth:
    def __init__(self):
        self.labyrinth = MickeyLabyrinth()

    def start(self):
        print("\nBienvenido al laberinto de Mickey")
        print("\n    - Usa para moverte: -\n\n\t      5\n            1 2 3\n")
        input("Pulsa enter para empezar...")
        while True:
            self.labyrinth.show_labyrinth()
            movement = input("Introduce el movimiento: \n   - 0 para salir -\n\t")
            #print("Introduce el movimiento.")               # Esto lo acabará pidiento el usuario
            #movement = "2"
            state = None
            match movement:
                case "2":
                    state = self.labyrinth.move_mickey_down()
                    if self.labyrinth.game_over == True:
                        break
                case "1":
                    state = self.labyrinth.move_mickey_left()
                    if self.labyrinth.game_over == True:
                        break
                case "3":
                    state = self.labyrinth.move_mickey_right()
                    if self.labyrinth.game_over == True:
                        break
                case "5":
                    state = self.labyrinth.move_mickey_up()
                    if self.labyrinth.game_over == True:
                        break
                case "0":
                    print("\n\n     -- Has elegido salir. --\nGracias por utilizar el programa.")
                    break
                case _:
                    print("\nIntroduce una opción correcta:\n\n\t\t5. Ir arriba\n1. Izquierda\t2. Abajo\t3. Derecha\n       -- Introduce 0 para salir. --")
                    continue
            # Mostrar mensaje de continuación si el juego no ha terminado
            #if not self.labyrinth.game_over:
            #    input("\nPulsa Enter para continuar...")
            
            

            



            
        #print("\nHas conseguido ayudar a escapar a Mickey.\n       -- ¡¡Enhorabuena!!--")
        #print("")
        #labyrinth.locate_mickey()


print("\n\n\n")
PlayMickeyLabyrinth().start()



