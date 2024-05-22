import requests
from bs4 import BeautifulSoup

def links(url):
    enlaces = []
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href.strip():
                enlaces.append(href)
    return enlaces

url = "http://testphp.vulnweb.com/"

enlaces = links(url)

for enlace in enlaces:
    print(enlace)
