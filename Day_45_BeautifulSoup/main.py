from bs4 import BeautifulSoup
import requests

# SCRAPING: Fetch live website (requires internet connection)
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text  # Get HTML as string

# PATTERN: Parse HTML into BeautifulSoup object for navigation
soup = BeautifulSoup(yc_webpage, "html.parser")

# SCRAPING: Find all article title links (class="titlelink")
article_tags = soup.find_all(name="a", class_="titlelink")

# PATTERN: Parallel lists to store related data (titles, URLs, scores)
article_text_list = []
article_url_list = []

# KEY CONCEPT: Loop through tags and extract text/attributes
for tag in article_tags:
    article_text_list.append(tag.getText())  # Get visible text (title)
    article_url_list.append(tag.get('href'))  # Get href attribute (URL)

# SCRAPING: Complex query - extract IDs from tr tags with class="athing"
# Uses list comprehension: extract 'id' attribute from each tr element
article_ids = [each_id.get('id') for each_id in soup.find_all(name='tr', class_='athing')]

article_score_list = []

# PATTERN: Loop through IDs and find corresponding score spans
for each_id in article_ids:
    try:
        # SCRAPING: Find score span with id like "score_12345678"
        score_element = soup.find(name='span', id=f'score_{each_id}')
        # Extract number before word "points" (e.g., "123 points" → 123)
        score_text = score_element.getText().split()[0]
        article_score_list.append(int(score_text))
    except AttributeError:
        # PATTERN: Handle missing elements gracefully (site structure might change)
        # If score not found, default to 0
        article_score_list.append(0)

# LOGIC: Find article with highest score
highest_score_index = article_score_list.index(max(article_score_list))

# OUTPUT: Display top article (title, URL, score)
print(f"{article_text_list[highest_score_index]}\n"
      f"URL: {article_url_list[highest_score_index]}\n"
      f"Score: {article_score_list[highest_score_index]}")


