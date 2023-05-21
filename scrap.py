from bs4 import *
from requests import *
import pandas as pd

req = get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(req.text , 'html.parser')
movies = soup.find('tbody' , class_ = "lister-list").find_all("tr")
movie_list = []
for movie in movies:
    rank = movie.find('td' , class_ = 'titleColumn').get_text(strip=True).split('.')[0]
    name = movie.find('td' , class_ = 'titleColumn').a.text
    yr = movie.find('td' , class_ = 'titleColumn').span.text.replace('(' , '').replace(')' , '')
    rate = movie.find('td', class_='ratingColumn').text
    movie_list.append((int(rank) , name , int(yr) , float(rate)))
file = pd.DataFrame(movie_list , columns=["Rank" , "Movie Name" , "Year" , "Rating"])
print(file)