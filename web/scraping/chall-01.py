import requests
from bs4 import BeautifulSoup, Tag

URL = "https://pythonidae.herokuapp.com/web/flag"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

tags = soup.find_all()
for tag in tags:
    if tag.get('id') != None and'flag' in tag.get('id'):
        print(tag)