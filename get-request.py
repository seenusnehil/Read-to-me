# pk_24ab8389-59cf-4255-8b86-11f852c4c72d

import requests

url = "https://api.uberduck.ai/speak"

payload = {
    "voice": "lj",
    "pace": 1,
    "speech": "Hello World"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic cHViX3R6dGVpdnlnb2NuY2dtaGJqdjpwa18yNGFiODM4OS01OWNmLTQyNTUtOGI4Ni0xMWY4NTJjNGM3MmQ="
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)