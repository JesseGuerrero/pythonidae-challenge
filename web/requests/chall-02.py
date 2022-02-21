import requests

URL = "https://pythonidae.herokuapp.com/web/cookies"

session = requests.Session()
session.get(url=URL, headers={'User-Agent': 'pythonidae'})

print(session.cookies.get_dict())