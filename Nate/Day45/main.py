from bs4 import BeautifulSoup
import requests
#
# with open("website.html", encoding='utf8') as f:
#     content = f.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# all_a_tags = soup.find_all(name='a')
#
# for t in all_a_tags:
#     print(t.get('href'))
#
# heading = soup.find(name='h3', class_='heading')
# print(heading.string)



url = "https://news.ycombinator.com/news"

response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

articles = soup.find_all(name='a', class_='titlelink')

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get('href')
    article_texts.append(text)
    article_links.append(link)

# article_upvotes = soup.find_all(class_='score').getText()
article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(class_='score')]

max_upvotes = max(article_upvotes)
index = article_upvotes.index(max_upvotes)


print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])
