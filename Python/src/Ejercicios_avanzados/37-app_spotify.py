import base64
import requests


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