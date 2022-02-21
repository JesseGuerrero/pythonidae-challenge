import requests

URL = "https://pythonidae.herokuapp.com/web/generate"

req = requests.get(url=URL)

print(req.json())