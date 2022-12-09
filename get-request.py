# pk_24ab8389-59cf-4255-8b86-11f852c4c72d

import requests

url = "https://api.uberduck.ai/speak"

payload = {
    "voice": "lj",
    "pace": 1,
    "speech": """Nadezhda Alliluyeva (1901–1932), also known as Nadya or Nadia, was the second wife of Soviet leader 
    Joseph Stalin. She was born in Baku to a friend of Stalin, a fellow revolutionary, and was raised in Saint 
    . Alliluyeva was exposed to revolutionary activity throughout her youth. Having known Stalin from a young age, 
    she married him when she was 18, and they had two children. Alliluyeva worked as a secretary for Bolshevik leaders, 
    including Vladimir Lenin and Stalin, and also as an assistant in the Department of Agitation and Propaganda, before 
    enrolling at the Industrial Academy in Moscow to study synthetic fibres and become an engineer. She had health 
    issues, which had an adverse impact on her relationship with Stalin. She also suspected he was unfaithful, 
    which led to frequent arguments with him. On several occasions, Alliluyeva reportedly contemplated leaving Stalin. 
    After an argument she shot herself early in the morning of 9 November 1932. (Full article...)
    
    """
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic cHViX3R6dGVpdnlnb2NuY2dtaGJqdjpwa18yNGFiODM4OS01OWNmLTQyNTUtOGI4Ni0xMWY4NTJjNGM3MmQ="
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)