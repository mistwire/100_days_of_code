# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.empireonline.com/movies/features/best-movies-2/"
#
# response = requests.get(url)
# site_contents = response.text
# soup = BeautifulSoup(site_contents, 'html.parser')
#
# print("100 Greatest Movies of All Time!")
#
# headings = soup.find_all(class_="jsx-4245974604")
# print(headings[5].getText())
#

from bs4 import BeautifulSoup
import requests as r

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = r.get(URL)
empire_web = response.text

soup = BeautifulSoup(empire_web, "html.parser")
all_tags = soup.find_all(name="img", class_="jsx-952983560")

titles = []
for tag in all_tags:
    title = tag.get("alt")
    titles.append(title)
cut_list_titles = titles[12:]
movies = cut_list_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        number = movies.index(movie) + 1
        file.write(f"{number}) {movie}\n")