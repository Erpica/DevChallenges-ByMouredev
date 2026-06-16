import base64
import requests
from env import CLIENT_ID, CLIENT_SECRET

'''
Hemos tenido problemas al importar el archivo env.py. Paso a explicar porqué se crea el archivo, problemas y soluciones:
Para no poner aquí la clave secreta (ni la pública) de Spotify, hemos creado un archivo con dichas claves y lo hemos añadido a gitignore.
Se crea en la raíz
'''

client_secret = CLIENT_SECRET
print(client_secret)
'''
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

'''

""" def get_token() -> str:
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Autorization": "Basic" + base64.b64decode()
        "Content-Type": "application/x-www-form-urlencoded"
    } """