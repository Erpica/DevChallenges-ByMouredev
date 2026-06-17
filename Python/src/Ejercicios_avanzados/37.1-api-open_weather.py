'''
1. Obtenemos la API key
2. Importamos dotenv y os para hacer un os.getenv a la API KEY que estará en un archivo incluido en el .gitignore.
   En este caso las claves privadas se están guardando en .env
3. Hemos tenido problemas para cargar la constante API_KEY_OPEN_WEATHER porque no se han creado correctamente las rutas al iniciar el proyecto.
   La solución ha sido decirle donde está la variable al scritp de Python usando:
   * os.path(__file__) -> Me da la ruta completa del archivo que estoy usando (incluido el nombre del script.py).
   * os.path.dirname(__file__) -> Me da la ruta completa del directorio en el que estoy trabajando (dónde está el script.py).
   * env_file = os.path.join(path, ".env") -> Le digo donde está el archivo .env(que es donde he metido las variables de entorno).
4. Buscamos el primer endpoint, en este caso decidimos que sea el del "tiempo actual"
   Aquí la página me ofrece uno con suscripción (el 4.0) pero decidimos ir al del gratuito y que se consulta por ciudad (no por latitud y longitud).
5. Como vemos que en el endpoint va la api key quiere decir que no hace falta enviarla en un header por separado, como por ejemplo en Spotify.
6. Teniendo ya los datos en un diccionario json, se decide importar el módulo json para hacerle un dumps 
   y ver los datos mejor antes de ver con los que me voy a quedar
7. Aprendemos un par de parámetros para tener la descripción en castellano y los grados en celsius. Por cierto el ° se escribe 
   pulsando alt + 0176 o directamente con su código unicode \u00b0


'''

from dotenv import load_dotenv
import os
import requests
import json


path = os.path.dirname(__file__)
env_file = os.path.join(path, ".env")
print(env_file)
load_dotenv(dotenv_path=env_file)

city_name = "Cádiz"
API_KEY_OPEN_WEATHER = os.getenv("API_KEY_OPEN_WEATHER")


def access_data(api_key: str, city_name: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=es&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo {response.json()}.")

    data = response.json()
    # print(type(data))
    return data

def wind_direction(degrees: int) -> str:
    try:
        int(degrees)
    except Exception as e:
        print (f"Error de tipo {type(e).__name__}Para calcular la dirección del viento necesito un entero entre 0 y 180.")
    match degrees:
        case 0:
            return "Norte"
        case 90:
            return "Este"
        case 180:
            return "Sur"
        case 270:
            return "Oeste"
        case _:
            if degrees > 0 and degrees < 90:
                return "Noroeste"
            elif degrees > 90 and degrees < 180:
                return "Sureste"
            elif degrees > 180 and degrees < 270:
                return "Suroeste"
            else:
                return "Noroeste"



my_data = access_data(API_KEY_OPEN_WEATHER, city_name)
#for element in my_data.items(): # Podía valer para pocos datos pero aquí ya no se ve bien.
#    print(element)

#print(json.dumps(my_data, indent=4))

print(f"   -   Datos sobre la ciudad de {my_data["name"]}:   -\n")
print (f"La longitud de {my_data["name"]} es {my_data["coord"]["lon"]} y su latitud es {my_data["coord"]["lat"]}")
print(f"la situación meteorológica en este momento es {my_data["weather"][0]["description"]}")
print(f"La temperatura es de {my_data["main"]["temp"]} \u00b0C")
print(f"Hace un viento de {my_data["wind"]["speed"]} km/h que viene de {wind_direction(my_data["wind"]["deg"])}")


