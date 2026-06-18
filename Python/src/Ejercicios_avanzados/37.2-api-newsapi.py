'''
1. Accedemos a la documentación en https://newsapi.org/ y me dice que tiene tres formas de auth: 
   - Via the apiKey querystring parameter. (en la url) -> descartado
   - Via the X-Api-Key HTTP header. (X-Api-Key) -> Probaremos primero
   - Via the Authorization HTTP header. Including Bearer is optional, and be sure not to base 64 encode it like you may have seen in other authentication tutorials. 
     (HTTP Header) -> La implementaremos después.
2. Elegimos un endpoint. Tenemos Everithing y top headlines. Empezamos por este segundo.
3. Ya hemos visto que la X-Api-Key va en el Header y ya tenemos un enpoint.
4. Lo de siempre:
    headers = {"Authorization": "X-Api-Key"}
    url = f"https://newsapi.org/v2/everything?q=keyword&apiKey={API_KEY}"
    response = requests.get(url, headers=headers)
    data = response.json()


--
 - Authentication
Via querystring
GET https://newsapi.org/v2/everything?q=keyword&apiKey={API_KEY_NEWSAPI}
Via X-Api-Key HTTP header
X-Api-Key: 0c8fdd89723e410094d7346a1e8f4c84
Via Authorization HTTP header
Authorization: 0c8fdd89723e410094d7346a1e8f4c84

""" 
# Para ver las variables de entorno que empiezan por API
for clave, valor in os.environ.items():
    if clave.startswith("API"):
        print(f"{clave}: {valor}")

print("Directorio actual:", os.getcwd())
print("Archivos en este directorio:", os.listdir())
 """
'''

from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY_NEWSAPI")


def access_data(API_KEY):

    # API_KEY = os.getenv("API_KEY_NEWSAPI")
    headers = {"Authorization": "X-Api-Key"}
    #url = f"https://newsapi.org/v2/everything?q=keyword&apiKey={API_KEY}"
    url = f"https://newsapi.org/v2/top-headlines/sources?category=technology&apiKey={API_KEY}"

    response = requests.get(url, headers=headers)

    data = response.json()
    # print (type(data))
    return data

def get_data_sources(my_data):

    print(f"\nEstado de la respuesta: {my_data["status"]}")
    print(f"Número de artículos: {len(my_data["sources"])}")
    #print(f"Primer artículo: {my_data["sources"][0]["name"]}")
    for element in my_data["sources"]:
        print (f"* Título: {element["name"]}. Fuente: '{element["url"]}'")


#print(type(access_data()))
my_data = access_data(API_KEY)
#print(json.dumps(my_data, indent=4))
get_data_sources(my_data)

