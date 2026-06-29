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
1. Obtener un Token, se elige un token de aplicación que se llama "Client credentials grant flow"
   Nombre: Con Brais y Python
   URL de redireccionamiento de OAuth: http://localhost
   Confidential -> Porque la app estará en mi pc. Nadie puede ver las credencias (.env y .gitignore)
   (Para todo esto hemos tenido que aplicar el doble factor de autenticación y, para ello instalado en el móvil Authy)
2. Tras solicitar acceso tengo ahora un ID de cliente y un Secreto de Cliente (como la de Spotofy)
   Se meten los dos en .env
3. Con estos datos vamos a perdir un token de acceso. NO HACEMOS GET, HACEMOS POST ya que estamos creando algo: la sesión.
   En la documentación encontramos:
    curl -X POST 'https://id.twitch.tv/oauth2/token' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'client_id=<your client id goes here>&client_secret=<your client secret goes here>&grant_type=client_credentials'


'''

'''
 OAuth 2.0 





curl -X GET 'https://api.twitch.tv/helix/channels/ads?broadcaster_id=141981764' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'
'''

import requests





