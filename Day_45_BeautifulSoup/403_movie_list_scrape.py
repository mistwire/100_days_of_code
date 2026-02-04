import requests
from bs4 import BeautifulSoup

# SCRAPING: Target archived page (archive.org allows scraping)
# Using archived version ensures page structure remains stable for this challenge
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# PATTERN: Fetch and parse
response = requests.get(URL)
movie_site_raw_html = response.text  # Store HTML as string

soup = BeautifulSoup(movie_site_raw_html, "html.parser")

# SCRAPING: Find all movie titles (h3 elements with class="title")
all_movies = soup.find_all(name='h3', class_='title')

# LOGIC: Reverse list because page lists movies bottom-to-top (100 to 1)
# After reverse, movies are in 1-100 order
all_movies.reverse()
print(all_movies)

# PATTERN: Write extracted data to file for storage/analysis
with open('movies.txt', 'w', encoding='utf-8') as f:
    for movie in all_movies:
        # KEY CONCEPT: .getText() extracts visible text content from tag
        f.write(f'{movie.getText()}\n')  # Write each movie title on new line


