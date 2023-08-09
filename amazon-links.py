from requests import *
from bs4 import *

req = get('https://www.amazon.in/')
website = BeautifulSoup(req.text, 'html.parser')
content = website.find('body')
category_url = content.find('div', attrs={'id': "nav-main"}).find('div', class_="nav-fill")
header_url = category_url.find_all('a', class_='nav-a')

head_url_list = []

for html in header_url:
    head_url_list.append({html.text.strip(): 'https://www.amazon.in/' + html.attrs['href']})

electronics_url = get(head_url_list[8]['Electronics'])
website = BeautifulSoup(req.text, 'html.parser')
content = website.find('body')
electro_nav_bar = content.find('header', id="navbar-main").find('div', id="nav-main")
print(head_url_list)