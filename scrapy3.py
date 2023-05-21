from bs4 import *
from requests import *

req = get("http://quotes.toscrape.com/")
website = BeautifulSoup(req.text , "html.parser")
content = website.find_all("div" , class_ = "quote")
details = []
for info in content:
    quote = info.find("span" , class_ = "text").text.replace('"' , '')
    author = info.find("small" , class_ = "author").text
    details.append((quote , author))
print(details)