import requests

url = "https://api.uberduck.ai/reference-audio"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)