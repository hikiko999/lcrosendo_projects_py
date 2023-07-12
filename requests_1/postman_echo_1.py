import json
import requests
import yaml
from pprint import pprint
# Authorization: Basic cG9zdG1hbjpwYXNzd29yZA==

headers = {
    "Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="
}
url = "https://postman-echo.com/basic-auth"
response = requests.get(url=url,headers=headers)
json_response = response.json()

pprint(json_response)

headers = {
    # "Content-Type" : "application/json"
}

payload = {
    "event": "message",
    "request": "POST"
}

url = "https://postman-echo.com/server-events/2"
response = requests.post(url=url,data=json.dumps(payload),headers=headers)
# json_response = response.text()

print(response.text)