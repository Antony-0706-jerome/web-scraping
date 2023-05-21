from bs4 import *
from requests import *
import pandas as pd

req = get('https://www.imdb.com/search/title/?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,')
soup = BeautifulSoup(req.text , 'html.parser')
content = soup.find('div' , class_ = "lister-list").find_all("div" , class_ = "lister-item")
movie_list = []
for movies in content:
    year = movies.find("span", class_="lister-item-year").text.replace('(', '').replace(')', '')
    name = movies.find("div" , class_ = "lister-item-content").a.text
    rating = movies.find("div" , class_ = "inline-block").strong.text
    gross = movies.find("span" , attrs={'name':'nv'}).text
    s_no = movies.find("span", class_="lister-item-index").text.replace('.', '')
    movie_list.append((int(s_no) , name , year , float(rating) , gross))
file = pd.DataFrame(movie_list , columns=['S.No' , 'Movie Name' , 'Year' , 'Rating' , 'Gross'])
print(file)