import requests
import aiohttp
import time
import asyncio

async def get_uuid_from_api(data,voice,pace):
    session = aiohttp.ClientSession()
    print('Checking data that has to been send',voice)
    uuid=None
    url = "https://api.uberduck.ai/speak"

    payload = {
        "voice": voice,
        "pace": pace,
        "speech": data
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic cHViX3ZjbGlseWh2bXBqcXpqcnB4dzpwa19mMTU5MWRlNi01ZjE4LTQzNTgtYTUwZi0zZTUzOGI2MzAzMjE="
    }

    async with session.post(url, json=payload, headers=headers) as response:
        data= await response.json()
    
    uuid=data['uuid']


    url = f'https://api.uberduck.ai/speak-status?uuid={str(uuid)}'

    print(url)

    headers = {"accept": "application/json"}

    path = None

    while(path == None):
        async with session.get(url, headers=headers) as response:
        
            data = await response.json()
            path = data['path']

    
    url = path
    

    return url

def get_audio_file_from_uuid(number):

    url = f'https://api.uberduck.ai/speak-status?uuid={number}'

    headers = {"accept": "application/json"}
    time.sleep(25)

    response = requests.get(url, headers=headers)

    print(response.text)

    data=response.json()

    

    return data['path']

async def download_audio_file_from_url(url):
    bool=False
    
    session = aiohttp.ClientSession()
    time.sleep(10)
    print('Downloading File from the URL')
    print(url)
    async with session.get(url) as response:
        with open("audio_files/audio_output.mp3", 'wb') as fd:
            async for chunk in response.content.iter_chunked(10):
                fd.write(chunk)


    #open("audio_files/audio_output.mp3", "wb").write(content) 

    print('Downloaded file from the server')
    bool=True

    return bool