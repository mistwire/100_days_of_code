from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)
article_tags = soup.find_all(name="a", class_="titlelink")
article_text_list = []
article_url_list = []
for tag in article_tags:
    article_text_list.append(tag.getText())
    article_url_list.append(tag.get('href'))
article_ids = [each_id.get('id') for each_id in soup.find_all(name='tr', class_='athing')]
article_score_list = []
for each_id in article_ids:
    try:
        article_score_list.append(int(soup.find(name='span', id=f'score_{each_id}').getText().split()[0]))
    except AttributeError:
        article_score_list.append(0)
highest_score_index = article_score_list.index(max(article_score_list))
print(f"{article_text_list[highest_score_index]}\n"
      f"URL: {article_url_list[highest_score_index]}\n"
      f"Score: {article_score_list[highest_score_index]}")


