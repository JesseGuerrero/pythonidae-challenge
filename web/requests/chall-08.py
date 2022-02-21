import requests

URL = "https://pythonidae.herokuapp.com/web/echo"

req = requests.get(url=URL, json={'user':'Jesse'}, headers={'User-Agent': 'pythonidae'})
token = req.json()['token']
challenge = req.json()['challenge'][::-1]
req = requests.post(url=URL, json={'user':'Jesse', 'token': token, 'answer': challenge}, headers={'User-Agent': 'pythonidae'})
print(req.json())
