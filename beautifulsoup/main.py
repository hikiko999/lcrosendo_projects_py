import requests

url = "https://www.linkedin.com/in/leifchristianrosendo/"

r = requests.get(url=url)

print(r.content)