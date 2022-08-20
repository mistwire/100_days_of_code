from bs4 import BeautifulSoup

with open('website.html', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a) # 1st anchor tag
# print(soup.li) # 1st li
# print(soup.p) # 1st paragraph

# all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags)
# # all_paragraphs = soup.find_all(name='p')
# # print(all_paragraphs)
#
# for tag in all_anchor_tags:
#     #print(tag.getText()) # get text only
#     print(tag.get('href')) # get hrefs

heading = soup.find(name='h1', id='name')
print(heading)

section_heading = soup.find(name='h3', class_='heading')
print(section_heading.text)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select('.heading')
print(headings)
