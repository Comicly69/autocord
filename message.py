import requests
import json
import time
from colorama import Fore, Style

# define the API endpoint
url = "https://discord.com/api/v9/channels/1098398208591401133/messages"

while True:
    message = input("What is the message? ")

    # generate a new nonce value based on the current timestamp
    nonce = str(time.time())

    # define the data to be sent in the request
    data = {
        "content": message,
        "nonce": nonce,
        "tts": False,
        "flags": 0
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }

    # send the POST request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # format the response based on the status code
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if response.status_code == 200:
        print(f"{Fore.LIGHTBLACK_EX}{current_time} {Fore.GREEN}Success {Style.RESET_ALL}Response status code: {response.status_code}")
    else:
        print(f"{Fore.LIGHTBLACK_EX}{current_time} {Fore.RED}Error {Style.RESET_ALL}Response status code: {response.status_code}")
        print("Response text:", response.text)
