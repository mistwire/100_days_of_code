from bs4 import BeautifulSoup

# SCRAPING: Read HTML from file (local testing, no internet needed)
with open('website.html', encoding='utf-8') as file:
    contents = file.read()

# PATTERN: Create BeautifulSoup object to parse HTML string into navigable tree structure
soup = BeautifulSoup(contents, 'html.parser')

# KEY CONCEPT: Hierarchical navigation - access first matching tag directly
# print(soup)              # Print raw parsed HTML
# print(soup.prettify())   # Pretty-print with indentation (useful for debugging)
# print(soup.title)        # First <title> tag
# print(soup.title.name)   # Tag name ('title')
# print(soup.title.string) # Text content of tag
# print(soup.a)            # 1st anchor tag (first <a>)
# print(soup.li)           # 1st list item
# print(soup.p)            # 1st paragraph

# SCRAPING: .find_all() returns list of all matching elements
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)   # List of <a> tags
# all_paragraphs = soup.find_all(name='p')
# print(all_paragraphs)    # List of <p> tags
#
# for tag in all_anchor_tags:
#     print(tag.getText())  # Extract visible text from tag
#     print(tag.get('href'))  # Extract attribute value

# PATTERN: .find() with filters - find first element matching criteria
heading = soup.find(name='h1', id='name')  # First <h1> with id="name"
print(heading)

# PATTERN: Filter by class with class_= (underscore because 'class' is Python keyword)
section_heading = soup.find(name='h3', class_='heading')
print(section_heading.text)  # .text is alias for .getText()

# SCRAPING: CSS selectors with .select_one() (returns single element)
# "p a" selector targets <a> tags inside <p> tags
company_url = soup.select_one(selector="p a")
print(company_url)

# PATTERN: ID selector in CSS (#idname)
name = soup.select_one(selector="#name")
print(name)

# SCRAPING: .select() returns list (CSS class selector .classname)
headings = soup.select('.heading')  # All elements with class="heading"
print(headings)
