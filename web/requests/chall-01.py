import requests

URL = "https://pythonidae.herokuapp.com/web/identity"

req = requests.get(url=URL, headers={'User-Agent': 'pythonidae'})

print(req.json())