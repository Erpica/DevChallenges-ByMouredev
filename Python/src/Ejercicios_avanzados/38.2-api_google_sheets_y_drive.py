'''
                             - APIs Sheets y Drive con Python -

- Para acceder a un archivo google sheets tenemos que habilitar las APIs de Sheets y Drive dentro del proyecto (En este caso vamos a usar el proyecto APIs Sheets y Drive con Python):
  https://console.cloud.google.com/apis/dashboard?hl=es-419&project=strategic-team-431015-s0
- Ejecuto el siguiente comando para instalar las dos librerías que se encargarán de gestionar la conexión y entender los tokens de Google: (Esto es porque tengo el gestor uv)
  uv pip install gspread google-auth
-  Autenticación. service_account: Es una cuenta especial de Google pensada para aplicaciones, no para personas:
1. En Google Cloud creas un service account.
2. Descargas el JSON → credenciales.json.
3. En tu script, cargas ese JSON con Credentials.from_service_account_file(...).
4. Compartes la hoja de Google Sheets con el email del service account (como si fuera un usuario más).
5. A partir de ahí, tu script puede acceder a la hoja como ese “usuario bot”.
#. No dependes de que un usuario haga login en un navegador. El script puede correr en un servidor, CRON, etc., sin intervención humana.

  
'''

import os
import sys
import gspread
from google.oauth2.service_account import Credentials

# Forzamos a Python a mirar primero en la carpeta exacta donde vive este script
# print(os.path.abspath(__file__)) # -> Imprime el path absoluto del script incluyendo el nombre del script

directorio_actual = os.path.dirname(os.path.abspath(__file__))
# print(directorio_actual) # -> Directorio actual sin el nombre del archivo
if directorio_actual not in sys.path:
    sys.path.insert(0, directorio_actual)


# 1. Definimos los "alcances" (permisos) que va a usar el script
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',    # Necesario para leer la hoja de Google Sheets
    'https://www.googleapis.com/auth/drive.readonly'            # Necesario para localizad la hoja de Google Sheets en Drive
]

# 2. Apuntamos a tu archivo de llaves que descargamos en el Paso 1
ruta_credenciales = os.path.join(directorio_actual, 'credenciales.json')
creds = Credentials.from_service_account_file(ruta_credenciales, scopes=SCOPES)

# 3. Autenticamos al cliente de gspread
cliente = gspread.authorize(creds)

try:
    print("⏳ Conectando con Google Drive...")
    
    # 4. Abrimos el documento por su nombre exacto
    # doc_citas = cliente.open("control_citas_junio")
    doc_citas = cliente.open_by_key("15HIjrrl-H5Dld5-fQ9Y_mOf8WVcxeaEtYSffUC4GW7c")
    
    # 5. Entramos en la pestaña concreta que nos interesa
    hoja_datos = doc_citas.worksheet("CITAS JUNIO")
    # print(f"Acceso a una celda concreta: {hoja_datos.get("C2")}") # -> Provando el acceso a una celda.
    
    # 6. Nos traemos todas las filas transformadas en una lista de diccionarios
    registros = hoja_datos.get_all_records()
    
    print("✅ ¡Conexión e importación exitosas!\n")
    print(f"📊 Se han leído correctamente {len(registros)} filas de la pestaña 'DATOS'.\n")
    
    # Muestra en la consola las 3 primeras filas para comprobar que todo está en orden
    if registros:
        print("👀 Aquí tienes una muestra de los primeros registros:")
        for i, fila in enumerate(registros[:3]):
            print(f" Registro {i+1}:")
            print(f"  - Comercial: {fila.get('COMERCIAL')}")
            print(f"  - Captador: {fila.get('CAPTADOR')}")
            print(f"  - Estado: {fila.get('ESTADO')}")
            print(f"  - Resultado: {fila.get('RESULTADO')}\n")
    else:
        print("⚠️ La hoja de cálculo parece estar vacía.")

except gspread.exceptions.SpreadsheetNotFound:
    print("❌ Error: No se ha encontrado el archivo 'control_citas_junio'.")
    print("   Revisa que el nombre sea idéntico y que hayas compartido el documento con el email del JSON.")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")