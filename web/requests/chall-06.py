import requests

URL = "https://pythonidae.herokuapp.com/web/login"


res = requests.post(url = URL, json={'user': 'xathrya', 'pass': 'Pythonidae'})
token = res.json()['jwt_token']
res = requests.post(url = 'https://pythonidae.herokuapp.com/web/jwt_header',
                    header={'Authorization': 'Bearer ' + token})
print(res.text)