from requests import *
from bs4 import *
import pandas as pd

headers = {
    'authority': 'www.bikewale.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'BWC=1BOER6SRQB7pU5xSzw6yjZJ7P; _bwtest=90; _bwutmz=utmcsr%3Dgoogle%7Cutmgclid%3D%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic; BHC=1BOER6SRQB7pU5xSzw6yjZJ7P; _gid=GA1.2.1991467488.1690366682; newUserSession=0; AMP_TOKEN=%24NOT_FOUND; DesktopDetected=1; _ga=GA1.2.1000642431.1690366681; _cwv=1BOER6SRQB7pU5xSzw6yjZJ7P.4ZxshiRgfQ.1690392374.1690392422.1690392423.2; _ga_KQ9B4GY2C7=GS1.1.1690372576.2.1.1690373647.0.0.0',
    'Referer': 'https://www.bikewale.com/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

req = get('https://www.bikewale.com/', headers=headers)
website = BeautifulSoup(req.content, 'html.parser')
content = website.find('body')
bikes_content = content.find('ul', class_="o-XylGE o-bCRRBE o-cpnuEd")
name = bikes_content.find_all('div', class_="o-cpNAVm o-byFsZJ o-eemiLE o-fzpihx")
bike_name = []
for bikes in name:
    bike_name.append(bikes.text)

url_details = bikes_content.find_all('a', class_='o-cKuOoN o-frwuxB')
urls = []
for url in url_details:
    urls.append('https://www.bikewale.com'+url.attrs['href'])

bikes_url = dict()
for i, j in zip(bike_name, urls):
    bikes_url.update({i: j})

df1 = pd.DataFrame({'BikeName': bike_name, 'URL': urls})
df1.to_csv('F:/Bikes.csv', index=False)

royalEnfield = {
    "authority": "www.bikewale.com",
    "method": "GET",
    "path": "/royalenfield-bikes/",
    "scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "BWC=1BOER6SRQB7pU5xSzw6yjZJ7P; _bwtest=90; _bwutmz=utmcsr%3Dgoogle%7Cutmgclid%3D%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic; BHC=1BOER6SRQB7pU5xSzw6yjZJ7P; _gid=GA1.2.1991467488.1690366682; DesktopDetected=1; _CustCityMaster=Select%20City; _CustAreaId=-1; _CustCityIdMaster=-1; _CustAreaName=Select%20Area; _CustZoneIdMaster=; _CustZoneMaster=Select%20Zone; _CustLatitude=-100; _CustLongitude=-200; newUserSession=0; _fbp=fb.1.1690429081554.1145260784; AMP_TOKEN=%24NOT_FOUND; _cwv=1BOER6SRQB7pU5xSzw6yjZJ7P.oWevjPzIP2.1690448877.1690449966.1690449971.4; _ga=GA1.2.1000642431.1690366681; _ga_KQ9B4GY2C7=GS1.1.1690429087.4.1.1690431041.0.0.0",
    "Referer": "https://www.bikewale.com/",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

royal_enfield = get(bikes_url.get('Royal Enfield'), headers=royalEnfield)
website = BeautifulSoup(royal_enfield.content, 'html.parser')
content = website.find('body').find('section', id = 'bikeMakeList')
enfield_bikes = content.find_all('div', class_='bikeDescWrapper')
model_name, model_url, price, cc, kmpl, bhp, kg = [], [], [], [], [], [], []

for det in enfield_bikes:
    name = det.find('a', class_='modelurl').attrs
    model_name.append(name['title'])
    model_url.append('https://www.bikewale.com/' + name['href'])
    price.append(det.find('div', class_='text-bold').find('span', class_='font18').text.replace('₹', '').strip())
    features = det.find('div', class_='text-xt-light-grey font14 margin-bottom15').text.strip().split(',')
    cc.append(features[0])
    kmpl.append(features[1])
    bhp.append(features[2])
    kg.append('NA') if len(features) < 4 else kg.append(features[3])

df2 = pd.DataFrame({'ModelName': model_name, 'ModelUrl': model_url, 'Price': price, 'CC': cc, 'KMPL': kmpl, 'bhp': bhp, 'KG': kg})
df2.to_csv('F:/RoyalEnfield.csv', index=False)
print('CSV created....')