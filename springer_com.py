import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import *

start = time()
path = Service(r'F:\driver\chromedriver.exe')
driver = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=path, options=driver)
title_list, url_list = [], []
def create_df(title1, title2, list1, list2):
    df = pd.DataFrame({title1: list1, title2: list2})
    print(df)
    df.to_csv('F:/springer_com.csv', index=False)
    print('File Saved....')
flag, pg = True, 1
while flag:
    driver.get(f'https://link.springer.com/search/page/{pg}?facet-discipline=%22Chemistry%22')
    pg += 1
    sleep(1.3)
    titles = driver.find_elements(By.CLASS_NAME, 'title')
    for title in titles:
        if len(title_list) <= 150 and len(url_list) <= 150:
            print(title.text, '--', title.get_attribute('href'))
            # title_list.append(title.text)
            # url_list.append(title.get_attribute('href'))
        else:
            flag = False

end = time()
print('Total Time taken: ', end - start)