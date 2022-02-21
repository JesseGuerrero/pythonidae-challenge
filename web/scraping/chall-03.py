import requests
from bs4 import BeautifulSoup

URL = "https://warbycode.com/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

from urllib.request import urlopen
for image in images:
    if 'http' in image.attrs['src']:
        print(image.attrs['src'])
        print(urlopen(image.attrs['src']).read())





