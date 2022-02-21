import requests
from bs4 import BeautifulSoup

URL = "https://www.youtube.com/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

FQDN = []
for aTag in soup.find_all('a'):
    if 'http' in aTag.get('href'):
        print(aTag.get('href'))