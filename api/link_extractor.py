import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        extract_links = [link.get('href') for link in links]
        return extract_links
    except Exception as e:
        print("Error:",e)
        return []
website_url = "https://es.scribd.com/"
links = extract_links(website_url)
for link in links:
    print(link)