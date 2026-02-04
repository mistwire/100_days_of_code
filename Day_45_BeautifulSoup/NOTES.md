# Day 45: Web Scraping with BeautifulSoup -- Parsing HTML & Extracting Data

## What You Learned
BeautifulSoup is a Python library for parsing HTML and extracting data from websites. You learned how to navigate HTML structure, select elements using different methods, and transform web pages into usable data.

---

## Key Concepts

### 1. HTTP Requests & HTML Parsing
Web scraping starts with fetching HTML:
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
webpage_html = response.text
soup = BeautifulSoup(webpage_html, "html.parser")
```

**Why:** `requests.get()` fetches the page. BeautifulSoup parses the HTML into a navigable tree structure. Without parsing, HTML is just a string.

### 2. Navigating the DOM Tree
Once parsed, you can navigate hierarchically:
```python
soup.title          # First <title> tag
soup.h1             # First <h1> tag
soup.p              # First <p> tag
soup.prettify()     # Pretty-print the HTML tree
```

**Why:** Hierarchical navigation is useful for simple, predictable HTML. The `.` syntax accesses first matching element.

### 3. Finding Elements: .find() vs .find_all()
```python
# Find first matching element
first_link = soup.find(name='a')
first_paragraph = soup.find(name='p')

# Find ALL matching elements (returns list)
all_links = soup.find_all(name='a')
all_paragraphs = soup.find_all(name='p')

for link in all_links:
    print(link.getText())  # Extract text
    print(link.get('href'))  # Extract attributes
```

**Why:** `.find()` returns one element; `.find_all()` returns a list. Choose based on your needs.

### 4. Filtering by Attributes
```python
# Find by class
heading = soup.find(name='h3', class_='heading')

# Find by ID
element = soup.find(name='div', id='main')

# Find by any attribute
link = soup.find(name='a', attrs={'data-id': '123'})
```

**Why:** Classes and IDs narrow searches. This is crucial for targeting specific elements in large pages.

### 5. CSS Selectors
Modern approach using `.select()` and `.select_one()`:
```python
# CSS selector - returns list
all_headings = soup.select('.heading')  # All elements with class "heading"

# Single selector - returns one element
first_link = soup.select_one('p a')  # First <a> inside <p>

# Complex selectors
skill_boxes = soup.select('div.skill-box > span')  # Children with '>'
links_in_nav = soup.select('nav > a')
```

**Why:** CSS selectors are more powerful than `.find()`. They support complex queries like child selectors (>), descendants, etc. Selectors match your HTML/CSS knowledge (Days 41-44).

### 6. Extracting Text & Attributes
```python
element = soup.find('a', class_='link')

# Get text content
text = element.getText()         # "Click here"
text = element.text             # Alternative syntax

# Get attributes
href = element.get('href')       # "/page.html"
href = element['href']           # Alternative syntax
classes = element.get('class')   # Returns list if multiple classes
```

**Why:** `.getText()` gets visible text; `.get()` gets attributes. This is core to data extraction.

### 7. Handling Missing Elements
```python
# This works (returns None if not found)
element = soup.find(name='span', id='score_123')

# Prevent AttributeError when element is None
try:
    score = int(element.getText().split()[0])
except AttributeError:
    score = 0  # Default value if element missing
```

**Why:** Websites change. Defensive coding prevents crashes when selectors break.

### 8. Real-World Project: Scraping News Sites
Your Hacker News scraper combines concepts:
```python
soup = BeautifulSoup(yc_webpage, "html.parser")
article_tags = soup.find_all(name="a", class_="titlelink")  # All articles

# Extract data from each article
for tag in article_tags:
    title = tag.getText()
    url = tag.get('href')
    # Use this data...
```

**Pattern:** 1) Find containers, 2) Loop through them, 3) Extract data from each.

### 9. Parsing HTML Files vs Live Websites
```python
# From HTML file
with open('website.html', encoding='utf-8') as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')

# From live website (needs requests)
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
```

**Why:** Both approaches work. Local files are faster for testing; live sites give current data.

### 10. BeautifulSoup Parser Types
```python
soup = BeautifulSoup(html, 'html.parser')  # Built-in, no install needed
soup = BeautifulSoup(html, 'lxml')         # Faster, requires: pip install lxml
soup = BeautifulSoup(html, 'html5lib')     # Most forgiving
```

**Why:** Different parsers have different speeds/strictness. `lxml` is fastest (used in Day 47).

---

## Common Pitfalls
- **Forgetting to import**: `from bs4 import BeautifulSoup` and `import requests`
- **Confusing `.find()` and `.find_all()`**: `.find()` returns one; `.find_all()` returns list
- **Not handling missing elements**: Site changes = selectors break. Use try/except
- **Extracting from None**: Check if element exists before calling `.getText()` or `.get()`
- **Using `getText()` vs `.get(attr)`**: `.getText()` gets visible text; `.get()` gets attributes
- **Forgetting `encoding='utf-8'`**: Special characters break without proper encoding
- **Not respecting `robots.txt`**: Legal/ethical issue. Check site's terms before scraping
- **Scraping too fast**: Overload servers. Add delays with `time.sleep()`

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Days 41-44** | HTML/CSS structure + selectors: BeautifulSoup requires understanding what you're targeting |
| **Day 46** | Spotify scraper: combines BeautifulSoup (scrape Billboard) + API (Spotify) |
| **Day 47** | Amazon scraper: adds email notifications when prices drop |
| **Day 48** | Selenium automates form submission (more than just scraping) |

---

## Before You Move On

Make sure you can:
- [ ] Fetch HTML with `requests.get()` and parse with BeautifulSoup
- [ ] Navigate DOM with hierarchical syntax (`soup.tag`)
- [ ] Use `.find()` for single elements and `.find_all()` for multiple
- [ ] Filter by `class_=` and `id=` parameters
- [ ] Use CSS selectors with `.select()` and `.select_one()`
- [ ] Extract text with `.getText()` and attributes with `.get()`
- [ ] Handle missing elements gracefully (try/except)
- [ ] Work with lists returned by `.find_all()` (iterate, index, etc.)

---

## Practice Prompt
**Build a web scraper for a real website:**

1. **Choose a target:** News site, product listings, job board, etc.
2. **Scrape and display:** Extract titles, links, and descriptions
3. **Save to file:** Write results to CSV or TXT
4. **Handle errors:** Use try/except for missing elements
5. **Add filtering:** Extract only items matching criteria (e.g., price < $100)

**Example:** Scrape product listings from a site and find items under a price threshold.

**Ethical note:** Check site's `robots.txt` and Terms of Service. Many sites prohibit scraping. For practice, use sites that explicitly allow it (like the provided archive.org example in Day 45).
