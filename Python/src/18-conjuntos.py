data = [1, 2, 3, 4, 5]

print(f"\nDatos originales: {data}")

data.append(6)
print(f"Añado elemento al final: {data}")

data.insert(0, 0)
print(f"Añado un elemento (el 0) en la posición 0: {data}")

data.extend([7, 8, 9])
print(f"Añado varios elementos al final: {data}")

data[3:3] = [-1, -2, -3]
print(f"Añado varios elementos (tres en total) en la posición 3: {data}")

print(f"elimino el elemento en la posición 3: {data}")
del(data[3])

print(f"Actualizo el elemento en la posición 4: {data}")
data[4] = -1

print(f"Comprobar si un elemento existe: {-1 in data}")

# del (data) # eliminaríamos el objeto. Ya print(data) daría error
data.clear()
print(f"Elimino el contenido: {data}")

'''
Muestra ejemplos de las siguientes operacines con conjuntos:
- Unión
- Intersección
- Diferencia
- Diferencia simétrica
'''

# Conjuntos: set {}
# No permiten duplicados (si metes el mismo elemento diez veces, solo se guarda una).
# No tienen orden (no puedes acceder a ellos mediante un índice como mi_conjunto[0]).

programacion = {"Ana", "Luis", "Carlos", "Sofía"}
diseno = {"Carlos", "Sofía", "María", "Pedro"}

print (f"\nProgramación: {programacion} // Diseño: {diseno}")

# Unión (|):
# La unión junta todos los elementos de ambos conjuntos, pero como los conjuntos no duplican, los estudiantes que están en ambos cursos solo aparecerán una vez.
# Con método: programacion.union(diseno) // Con operador: programacion | diseno
union = programacion.union(diseno)
union = programacion | diseno
print("\nResultado de unión: ", union)

# Intersección (&)
# La intersección te devuelve únicamente los ELEMENTOS EN COMÚN (los que están en ambos conjuntos a la vez). 
# En nuestro caso, los alumnos que estudian tanto programación como diseño.
# Con método: programacion.intersection(diseno) // # Con operador: programacion & diseno
interseccion = programacion.intersection(diseno)
interseccion = programacion & diseno
print("\nresultado de intersección (ELEMENTOS EN COMÚN):", interseccion)

# Diferencia (-)
# La diferencia te da los elementos que ESTÁN EN EL PRIMER CONJUNTO PERO NO EN EL SEGUNDO. Ojo aquí: el orden importa. 
# No es lo mismo $A - B$ que $B - A$.
# Con método: programacion.diference(diseno) // Con operador: -
diferencia = programacion.difference(diseno)
diferencia = programacion - diseno
diferencia_al_reves = diseno - programacion
print("\nResultado de la diferencia (ESTÁN EN EL PRIMER CONJUNTO PERO NO EN EL SEGUNDO): ", diferencia)
print("Resultado de la diferencia (ahora diseño menos programación): ", diferencia_al_reves)

# Diferencia simétrica (^)
# Es lo opuesto a la intersección. Te devuelve todos los elementos que están EN UN CONJUNTO O EN EL OTRO, pero excluye por completo a los que están en ambos. 
# Serían los alumnos que solo están matriculados en una sola materia.
# Con método: programacion.symmetric_difference(diseno) // Con operador: programacion ^ diseno
dif_simetrica = programacion.symmetric_difference(diseno)
dif_simetrica = programacion ^ diseno
print (f"\nResultado de la diferencia simétrica (no tengo en cuenta lo que tienen en común): ", dif_simetrica)



# Una ventaja extra: Combinarlo con List Comprehensions 💡
'''
¿Te acuerdas de las list comprehensions que vimos antes? También existen las Set Comprehensions. 
Funcionan exactamente igual, pero usan llaves {} en lugar de corchetes [] para asegurar que el resultado final no tenga duplicados.
'''