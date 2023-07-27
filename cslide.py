from requests import *
from bs4 import *

url = 'https://cslide.ctimeetingtech.com/icopa22/attendee/confcal/presentation?p='
page = 1
title = []
while True:
    req = get(url+str(page))
    content = BeautifulSoup(req.text, 'html.parser')
    for tit in content.find_all('div', class_='card-block'):
        h4 = tit.find('h4', class_='card-title')
        small = tit.find('small').extract()
        title.append(h4.text)
    page += 1
    if content.find('a', class_='next-page-anchor') is None:
       break

print(len(title))
