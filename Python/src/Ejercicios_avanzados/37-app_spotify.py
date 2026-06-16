import requests

url = "https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V"
headers = {
    "Authorization": "Bearer NgCXRK...MzYjw"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())  # Si la respuesta es JSON