import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_site_raw_html = response.text

soup = BeautifulSoup(movie_site_raw_html, "html.parser")

all_movies = soup.find_all(name='h3', class_='title')
all_movies.reverse()
print(all_movies)

with open('movies.txt', 'w', encoding='utf-8') as f:
    for i in all_movies:
        f.write(f'{i.getText()}\n')


