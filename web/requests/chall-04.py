import requests

URL = "https://pythonidae.herokuapp.com/web/login"


res = requests.post(url = URL, json={'user': 'xathrya', 'pass': 'Pythonidae'})

print(res.text)