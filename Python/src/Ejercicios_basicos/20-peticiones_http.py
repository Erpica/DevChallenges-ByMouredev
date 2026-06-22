import requests
import json


'''
# Al intentar usar requests me aparece el error: "Import "requests" could not be resolved from source"
- intento pip install requests -> me da error porque tengo instalada uv (siguiendo una normativa moderna de Python llamada PEP 668) para que no instales librerías globales que puedan romper tu sistema.
- intento uv pip install requests -> error porque no tengo un entorno virtual creado
- creo un entorno virtual con P:...>uv venv
- ahora sí, instalo el paquete con P:...>uv pip install requests
- ahora no funciona el botón play porque hay que decirle a VSCode que no ejecute el entorno global sino el entorno virtual. (no obstante si lo obligo a ejecutarse si funciona: uv run Python/src/20-peticiones_http.py)
- Pulso ctrl+shift+p y escribo "Python: Select Interpreter". Le digo "enter interpreter patth" y le meto el P:/.../ .venv/Scripts/python.exe.
- El problema es que el botón play sigue sin funcionar, así que lo que hago es editar el archivo settings.json (que me lo había crearo la extensión Code Runner) y le añado las siguientes líneas (excepto la 1º que ya estaba):
{
    "python.terminal.executeInFileDir": true,
    "code-runner.runInTerminal": true,
    "code-runner.clearPreviousOutput": true,
    "code-runner.executorMap": {
        "python": "uv run $fullFileName"
    }
}

# requests:
La propia librería requests tiene un método mágico incorporado llamado .json() que transforma el texto directamente en un diccionario de Python.

# Códigos HTTP:
200 OK: La petición se realizó correctamente y el servidor devolvió la información esperada.
301 Moved Permanently: Redirección permanente. La página cambió de dirección URL de forma definitiva.
302 Found: Redirección temporal. La página se encuentra temporalmente en otra ubicación.
400 Bad Request: El servidor no pudo entender la solicitud debido a un error de sintaxis por parte del cliente.
401 Unauthorized: Faltan las credenciales o la autenticación es inválida.
403 Forbidden: El servidor entendió la petición, pero se niega a autorizarla (acceso denegado).
404 Not Found: La página o recurso solicitado no existe. Es el error más común.500 Internal Server Error: Error interno del servidor. El servidor falló al procesar la solicitud.
503 Service Unavailable: El servidor no está disponible temporalmente (suele deberse a sobrecarga o mantenimiento).
'''


response = requests.get("http://moure.dev")

if response.status_code == 200:
    #print(response.text)
    pass
else:
    #print(f"Error con código {response.status_code} al realizar la petición.")
    pass

'''
# Extra
Utilizando la PokéAPI (https://pokeapi.co), crea un programa por 
terminal al que le puedas solicitar información de un Pokemon concreto
utilizando su nombre o número.
- Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
- Muestra el nombre de su cadena de evoluciones
- Muestra los juegos en los que aparece
- Controla posibles errores

'''

# pokemon = input("Introduce el nombre del Pokemon a buscar: ").lower().strip()
pokemon = "bulbasaur" 

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    json_data = response.json()
    
    """ print(f"\nNombre: {json_data["name"]}.")
    print(f"Peso: {json_data["weight"]} kg.")
    print(f"Altura: {json_data["height"]} metros.")
    print(f"Nombre: {json_data["types"][0]["type"]["name"]}")
     """
    # Vamos a mostrar el nombre de su cadena de evoluciones:
    #for clave in json_data:
    #    print (clave)
    # Vemos las claves que hay para ver dónde puedo encontrar la evolución. Se detecta que viene por "species"
    # Vamos a ver que tipo de datos hay en species:
    # print(type(json_data["species"])) # -> Es un diccionario
    # print(json_data["species"]) # -> Así veo que consta de una URL. Vamos a capturar la url para investigarla
    url_species = json_data["species"]["url"]
    # print (url_species)
    response_species = requests.get(url_species)
    if response_species.status_code == 200:
        species_data = response_species.json()
        # Volvemos a ver las claves que tiene nuestra nueva url (y vemos que tiene evolution_chain):
        # for clave in species_data:
        #     print (clave)
        # print(type(species_data["evolution_chain"])) # -> Es un diccionario
        # print(f"evolution chain: {species_data["evolution_chain"]["url"]}")   # ya tenemos de nuevo la url
        species_data_url = species_data["evolution_chain"]["url"]
        print(species_data_url)
        response_evolution_chain = requests.get(species_data_url)
        # A partir de aquí IMPORTAMOS EL MÓDULO JSON lo que vacilita el visionado de datos
        if response_evolution_chain.status_code == 200:
            data_evolution_chain = response_evolution_chain.json()
            # print(data_evolution_chain)
            # for value in data_evolution_chain:
            #    print(value)
            # print(json.dumps(data_evolution_chain, indent=4))  # para el json.dumps hace falta importar el módulo json
            # chain, evolves_to, evolves_to, species, name
            print(data_evolution_chain["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"])
            """for value in data_evolution_chain["chain"]:
               print(value)
                print (data_evolution_chain["chain"]["evolves_to"]) 
            """
        else:
            print ("Fallo al obtener la cadena de evoluciones")

    else: 
        print("Fallo al obtener datos de especies")

else:
    print("KO")





# Extra by Brais
print ("\n\n\n### Extra by Brais ###\n")

# pokemon = input("Introduce el nombre del Pokemon a buscar: ").lower().strip()
pokemon = "bulbasaur"  # Para ir probando

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    print(f"\n- Nombre: {data["name"]}.")
    print(f"- Peso: {data["weight"]} kg.")
    print(f"- Altura: {data["height"]} metros.")
    print("- Tipo(s):")
    for type in data["types"]:
        print(type["type"]["name"])
    print("- Juegos")
    for game in data["game_indices"]:
        print(game["version"]["name"])
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Cadena de evolución:")
            # print(data["chain"]["species"]["name"]) # Encontramos la primera y decidimos hacer una función recursiva para sacarlas todas:
            def get_evolves(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        get_evolves(evolve)
            
            get_evolves(data["chain"])

        else:
            print(f"Error {response.status_code}: Fallo al buscar la evolución")
    else:
        print (f"Error {response.status_code}: Fallo al buscar la evolución")
else:
    print (f"Error {response.status_code}: Pokemon no encontrado")