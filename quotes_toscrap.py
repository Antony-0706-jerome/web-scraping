from bs4 import *
from requests import *
import pandas as pd

url = 'https://quotes.toscrape.com/page/'
page = 1
quotes, authors, tags = [], [], []

while True:
    req = get(url+str(page))
    website = BeautifulSoup(req.text, "html.parser")
    content = website.find_all("div", class_="quote")
    for info in content:
        quote = info.find("span", class_="text").text
        author = info.find("small", class_="author").text
        tag = info.find("div", class_="tags").text.strip().split('\n')
        quotes.append(quote)
        authors.append(author)
        tags.append(tag)
    page += 1
    if website.find("ul", class_ = "pager").find('li', class_ = 'next') is None:
        break

update_tags = []

for i in tags:
    if ('Tags:' in i):
        i.remove('Tags:')
        if ('            ' in i):
            i.remove('            ')
        update_tags.append(i)
    elif i == ['']:
        update_tags.append("none")

result = []
for j in update_tags:
    result.append(', '.join(j)+'.')
# print(result)
df = pd.DataFrame({'quote': quotes, 'Author': authors, 'Tags': result})
df.to_csv('F:/quotes_toscrap.csv', index=False, encoding='UTF-8')
print('File Created')

