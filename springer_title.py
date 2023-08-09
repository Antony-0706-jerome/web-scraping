import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import *

path = Service(r'F:\driver\chromedriver.exe')
driver = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=path, options=driver)

file = pd.read_csv('F:/springer_com.csv')
file_name = 1
for url in file['URL']:
    req = driver.get(url)
    sleep(0.5)
    html_content = driver.page_source
    with open(f'F:/html_files/T{file_name}.html', 'w', encoding='utf-8') as html_file:
        html_file.write(str(html_content))
    print(f'F:/html_files/T{file_name}.html'+' File Created....')
    file_name += 1