import requests
from bs4 import BeautifulSoup, Tag

URL = "https://www.youtube.com/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

for scriptTag in soup.find_all('script'):
    if scriptTag.get('src'):
        print(scriptTag.get('src'))
