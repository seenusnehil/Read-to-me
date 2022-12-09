import requests

url = "https://api.uberduck.ai/speak-status?uuid=97d5c292-60c8-4de1-9847-6bf659ff08f5"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)