import requests

URL = "https://pythonidae.herokuapp.com/web/login"


res = requests.post(url = URL, json={'user': 'xathrya', 'pass': 'Pythonidae'})
token = res.json()['jwt_token']
res = requests.post(url = 'https://pythonidae.herokuapp.com/web/jwt_body',
                    json={'jwt_token': token})
print(res.text)