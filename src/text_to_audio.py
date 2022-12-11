import requests
import time

def get_uuid_from_api(data,voice,pace):
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

    response = requests.post(url, json=payload, headers=headers)
    time.sleep(20)

    print(response.text)

    data=response.json()

   

    uuid=data['uuid']


    url = f'https://api.uberduck.ai/speak-status?uuid={str(uuid)}'

    '' ""
    print(url)

    headers = {"accept": "application/json"}
    time.sleep(10)

    response = requests.get(url, headers=headers)

    print(response.text)

    data=response.json()

    return data['path']

def get_audio_file_from_uuid(number):

    url = f'https://api.uberduck.ai/speak-status?uuid={number}'

    headers = {"accept": "application/json"}
    time.sleep(25)

    response = requests.get(url, headers=headers)

    print(response.text)

    data=response.json()

    

    return data['path']

def download_audio_file_from_url(url):
    bool=False
    response = requests.get(url)
    print('Downloading File from the URL')
    open("audio_files/audio_output.mp3", "wb").write(response.content) 

    print('Downloaded file from the server')
    bool=True

    return bool