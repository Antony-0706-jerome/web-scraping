from bs4 import *
from requests import *
import pandas as pd

req = get(url='https://www.bls.gov/web/empsit/cesbmart.htm', headers =
{'Authority': 'www.bls.gov', 'Method': 'GET', 'Path': '/web/empsit/cesbmart.htm', 'Scheme': 'https',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0',
'Cookie': '_gid=GA1.2.1090119362.1689824116; nmstat=95ac81ae-017f-cd53-10ab-cb74bdbb960e; _ga_WFFDEGRMJE=GS1.1.1689824115.1.1.1689825251.0.0.0; _ga=GA1.2.223454453.1689824115; _gat_GSA_ENOR0=1',
'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"', 'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site',
'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

website = BeautifulSoup(req.text, "html.parser")
content = website.find("div", class_="main-content").find("table", id='Table5')
header = content.find('thead').find_all('th')
col_name = []
for heading in header:
    col_name.append(heading.text)
col1 = content.find('tbody').find_all('tr')
col_val = []
for i in col1:
    col_val.append(i.text.strip().split('\n'))

df = pd.DataFrame(data=col_val, columns=col_name)

# for col in (col_val):
#     print(col)
print(df)
# print(df)
