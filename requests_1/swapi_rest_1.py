import json
import requests
from pprint import pprint

base_url = "https://swapi.dev/api/"

partial_url = "planets/1/"
new_url = base_url + partial_url
response = requests.get(new_url)
json_response = response.json()

pprint(json_response)