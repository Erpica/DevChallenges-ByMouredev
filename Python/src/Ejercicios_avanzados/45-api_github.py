'''
/*
 * EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 * 
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *   
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la información que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */
'''

import json

from dotenv import load_dotenv
import requests
import os

load_dotenv()

MY_TOKEN = os.getenv("GITHUB_TOKEN")

#user_name = input ("Introduce el nombre del usuario a estudiar: ")
user_name = "mouredev"

def get_info_repos(user_name):
    url = f"https://api.github.com/users/{user_name}/repos"
    


    headers = {"Authorization": f"Bearer {MY_TOKEN}",
               "header": "X-GitHub-Api-Version: 2026-03-10"
               }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def show_data_languages(data):
    #print(json.dumps(data, indent=4))
    
        
    for i in range(1,len(data)):
        if data[i]["language"] == None:
            pass
        else:
            print(data[i]["language"])
        
    
    """    
        for one_item in data[0].items():
            print(one_item) """    
    
def show_following(data):
    url = f"https://api.github.com/users/{user_name}"
    data = requests.get(url).json()
    return data


data = get_info_repos(user_name)
show_data_languages(data)
print (show_following(data))
