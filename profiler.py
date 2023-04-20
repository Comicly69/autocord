import requests
import json

url = "https://discord.com/api/v9/users/@me"
about_me = "i am you"

payload = {
    "bio": about_me
}
headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

response = requests.patch(url, headers=headers, data=json.dumps(payload))

print(response.status_code)
