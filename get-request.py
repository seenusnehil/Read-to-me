# pk_24ab8389-59cf-4255-8b86-11f852c4c72d

import requests

url = "https://api.uberduck.ai/speak"

payload = {
    "voice": "lj",
    "pace": 1,
    "speech": """
    You and I experience life differently
Is the idea of immortality and rebirth real or conceptual?
What is real? Can the conceptual be real? Our
understanding of reality is a function of the capabilities
of our body or deha, home of the atma. What is real for a
plant is not real for an animal, what is real for one human
is not real for another. Nature is all about diversity. This
understanding of the body, the instrument through
which we experience and express reality, is not explicitly
a part of The Gita, but certainly a part of Vedic knowledge
elaborated in the Upanishads, that Krishna assumes
Arjuna to be familiar with.
    """
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic cHViX3R6dGVpdnlnb2NuY2dtaGJqdjpwa18yNGFiODM4OS01OWNmLTQyNTUtOGI4Ni0xMWY4NTJjNGM3MmQ="
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
