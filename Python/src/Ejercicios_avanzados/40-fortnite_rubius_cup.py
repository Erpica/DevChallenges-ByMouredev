'''
EJERCICIO:
¡Rubius tiene su nueva skin en Fortnite!
Y va a organizar una competición para celebrarlo.
Esta es la historia de participantes:
https://x.com/Rubiu5/status/1840161450154692876

Desarrolla un programa que obtenga el número de seguidores en 
Twitch de cada participante, la fecha de creación de la cuenta
y ordene los resultados en dos listados.
- Usa la API de Twitch: https://dev.twitch.tv/docs/api/reference
  (NO subas las credenciales de autenticación)
- Crea un ranking por número de seguidores y por antigüedad.
- Si algún participante no tiene usuario en Twitch, debe reflejarlo.

        ## PROCESO: ##
1. Obtener un Token, se elige un token de aplicación que se llama "Client credentials grant flow" (por lo que necesito de datos y seguridad)
   * Estas se denominan server-to-server y quiere decir que ningún usuario meterá credenciales ni dará a aceptar.
   Es decir un pc (mi script) conectará directamente al servidor de Twitch
   * Nombre: Con Brais y Python
   URL de redireccionamiento de OAuth: http://localhost
   Confidential -> Porque la app estará en mi pc. Nadie puede ver las credencias (.env y .gitignore)
   * Vamos a necesitar importar dotenv para meter en una variable de entorno el contenido de .env. Se hace con load_dotenv()
   Una vez cargadas en memoria, necesitamos la librería os para meterlas ya en una variable usable por el script.
   (Para todo esto hemos tenido que aplicar el doble factor de autenticación y, para ello instalado en el móvil Authy)
2. Tras solicitar acceso tengo ahora un ID de cliente y un Secreto de Cliente (como la de Spotify)
   Se meten los dos en .env
3. Con estos datos vamos a perdir un token de acceso. NO HACEMOS GET, HACEMOS POST ya que estamos creando algo: la sesión.
   En la documentación encontramos:
    curl -X POST 'https://id.twitch.tv/oauth2/token' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials'
4. En response.get() además de headers o data también se pueden pasar params, por ejemplo para filtros de búsqueda.
   En Twich concretamente son obligatorios para este tipo de búsquedas.

# Notas:

- curl -
* El comando curl tiene similitudes con request:
  curl -X GET        => request.get()
* 'https://...'      => el primer argumento: url
* -H 'Nombre: Valor' => El parámetro headers=

- json -
Para ir viendo lo que trae el archivo, es decir, para ver mejor el json:
   * importamos json
   * print(json.dumps(data, indent=4))


'''

import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

CLIENT_ID = os.getenv("TWICH_CLIENT_ID")
SECRET_ID = os.getenv("TWICH_CLIENT_SECRET")






def get_token() ->str:
    url = "https://id.twitch.tv/oauth2/token"

    data = {
        "client_id": CLIENT_ID,
        "client_secret": SECRET_ID,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo el Token: {response.json()}")
    
    # return response.json() # -> devolvería {'access_token': 'xxx', 'expires_in': 4821832, 'token_type': 'bearer'}
    return response.json()["access_token"]

# print(get_token())
access_token = get_token()

'''
# Get Strems
curl -X GET 'https://api.twitch.tv/helix/streams' \
     -H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
     -H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'

# Get Users Endpoint:
curl -X GET 'https://api.twitch.tv/helix/users?login=twitchdev' \
     -H 'Authorization: Bearer jostpf5q0puzmxmkba9iyug38kjtg' \
     -H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'
'''

def get_streams(access_token: str):
   '''
   Creado para probar, no se usará
   '''
   url = "https://api.twitch.tv/helix/streams"

   headers = {
       f"Authorization": f"Bearer {access_token}",
       "client-Id": f"{CLIENT_ID}"
   }

   response = requests.get(url, headers=headers)
   data = response.json()
   return data
   #return json.dumps(data, indent=4)

# Pruebas
""" 
streams = get_streams(access_token)
# print(len(streams["data"])) # Me da el número de eventos
for element in streams["data"]:
    print (element["game_name"]) 
"""


user_name = "mouredev"
# https://x.com/Rubiu5/status/1840161450154692876
def get_user_data(access_token: str, user_name: str):
    url = "https://api.twitch.tv/helix/users"

    headers = {
        f"Authorization": f"Bearer {access_token}",
        "client-id": CLIENT_ID
    }

    params = {
        "login": user_name
    }

    response = requests.get(url=url, headers=headers, params=params)
    #print(response.status_code)
    data = response.json()
    #print (json.dumps(data, indent=4))
    return data["data"][0]["id"], data["data"][0]["created_at"]


user_id, created_at = get_user_data(access_token, user_name)

print(f"User ID: {user_id}, Created at: {created_at}.")

# https://x.com/Rubiu5/status/1840161450154692876
def get_video(access_token: str, user_id: str):
    url = "https://api.twitch.tv/helix/videos"

    headers = {
        f"Authorization": f"Bearer {access_token}",
        "client-id": CLIENT_ID
    }

    params = {
        "user_id": user_id
    }

    response = requests.get(url=url, headers=headers, params=params)
    #print(response.status_code)
    data = response.json()
    return data
    
    #print (json.dumps(data, indent=4))

video = get_video(access_token, user_id)
#print(json.dumps(video, indent=4))




#print (json.dumps(data, indent=4))

""" for element in video["data"]:
    print (f"Título: {element["title"]}. \t\tFecha de creación: {element["created_at"]}") """
