'''
¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
¿Qué pasaría si tuvieras que encargarte de repartir los anillos
entre las razas de la Tierra Media?
Desarrolla un programa que se encargue de distribuirlos.
Requisitos:
1. Los Elfos recibirán un número impar.
2. Los Enanos un número primo.
3. Los Hombres un número par.
4. Sauron siempre uno.
Acciones:
1. Crea un programa que reciba el número total de anillos
y busque una posible combinación para repartirlos.
2. Muestra el reparto final o el error al realizarlo.

--

El usuario introduce un número
- resto uno que es para Sauron
- divido entre 3 para ver más o menos cuantos le voy a dar equitativamente a los otros
- guardo tres listas con las posibilidades:
    los pares, los impares y los primos entre cero y el número dado


20 - 1 = 19
19 / 3 = 7 redondeando hacia arriba

- 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
- 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
- 2, 3, 5, 7, 11, 13, 17, 19 

posibles soluciones:
7 + 7 + 6 -> Error, me quedo sin el de Sauron
5 + 5 + 6 -> 16 + 1 = 17 (sobran 3)

finalmente olvido el reparto equitativo, busco todas las soluciones y devuelvo la de en medio

'''


def recursive_primes(number: int) -> list:
    primes = []
    for num in range(2, number + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # py CORRECTO: Ahora comprueba y añade CADA número antes de pasar al siguiente
        if is_prime:
            primes.append(num)
            
    return primes

def check_solution(number: int) -> list:
    '''
    Recibe: Medallas a repartir


    Devuelve: una lista con el reparto o la lista vacía si no hay solución posible

    '''
    ''' Busca todas las combinaciones posibles de reparto '''
    list_of_solutions = []

    prime_numbers = recursive_primes(number)
    even_list = [n for n in range(2, number + 1) if n % 2 == 0]
    odd_list = [n for n in range(1, number + 1) if n % 2 != 0]

    # x = Elfos (Impar), y = Enanos (Primo), z = Hombres (Par)
    for x in odd_list:
        for y in prime_numbers:
            for z in even_list:
                if x + y + z == number - 1:
                    list_of_solutions.append([x, y, z])
    return list_of_solutions


#number = 20
# --- PROCESO PRINCIPAL ---
try:
    number = int(input("Introduce el número de anillos a repartir: "))
    
    todas_las_soluciones = check_solution(number)
    
    if todas_las_soluciones:
        # py Seleccionamos la solución central usando la división entera //
        indice_medio = len(todas_las_soluciones) // 2
        choosed_list = todas_las_soluciones[indice_medio]
        
        race_list = ["Elfos", "Enanos", "Hombres"]
        
        print(f"\n✨ Se han encontrado {len(todas_las_soluciones)} combinaciones.")
        print(f"Reparto intermedio seleccionado (Opción {indice_medio + 1}):\n")
        
        # py Mostramos el reparto definitivo emparejando los datos con las razas
        for i, j in zip(choosed_list, race_list):
            print(f"   - {j} - {i}")
        print("   - Sauron - 1")
        
        #print("\nLista de valores aplicada [Elfos, Enanos, Hombres]:")
        #print(choosed_list)
            
    else:
        print("❌ No existe una solución posible.")

except ValueError:
    print("Por favor introduce un número entero de anillos.")

