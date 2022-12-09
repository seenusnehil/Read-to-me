import requests

url = "https://api.uberduck.ai/speak-status?uuid=444e3331-9a59-4440-8d0a-fca3d3291bf8"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)