import requests

url = "https://api.uberduck.ai/speak"

payload = {
    "speech": "Hello, We are the group participating in AssemblyAI hackathon",
    "voice": "lj",
    "pace": 1
}
headers = {
    "accept": "application/json",
    "uberduck-id": "anonymous",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)