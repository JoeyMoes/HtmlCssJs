print("Begin scraping script")

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://coinmarketcap.com/')
#print(pagina.content)

entire_html = BeautifulSoup(pagina.content, 'html.parser')
tableBodies = entire_html.find('tbody')

#print(tableBodies.prettify())

rows = entire_html.find('tr')

links = entire_html.find_all(class_='cmc-link')
for rij in links:
    print(rij)