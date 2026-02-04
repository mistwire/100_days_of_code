# Day 48: Browser Automation with Selenium -- WebDriver & Interaction

## What You Learned
Selenium automates web browsers, allowing you to click buttons, fill forms, and interact with JavaScript-heavy websites. Unlike BeautifulSoup (static HTML), Selenium controls a real browser that executes JavaScript.

---

## Key Concepts

### 1. Selenium vs. BeautifulSoup
| Aspect | BeautifulSoup | Selenium |
|--------|---------------|----------|
| **What it does** | Parses static HTML | Controls real browser |
| **JavaScript** | ✗ Can't execute | ✓ Executes dynamically |
| **Speed** | Fast | Slower (launches browser) |
| **Use cases** | Scraping static sites | Interacting, logging in, forms |

**Why:** Choose based on needs. Static sites = BeautifulSoup (faster). Dynamic sites/interaction = Selenium.

### 2. Setting Up WebDriver
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Install ChromeDriver automatically
driver = webdriver.Chrome(service=Service(
    executable_path=ChromeDriverManager().install()
))
```

**Why:** `webdriver_manager` automatically downloads correct ChromeDriver version. No manual setup needed.

### 3. Opening & Navigating Pages
```python
driver.get("https://www.python.org")  # Navigate to URL
title = driver.title                    # Get page title
driver.quit()                           # Close browser
```

**Why:** `.get()` waits for page to load. `.quit()` is essential cleanup (prevents zombie processes).

### 4. Finding Elements by Different Selectors
```python
from selenium.webdriver.common.by import By

# Find by name attribute
search_bar = driver.find_element(by=By.NAME, value="q")

# Find by class
logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")

# Find by ID
element = driver.find_element(by=By.ID, value="main")

# Find by CSS selector (most flexible)
docs_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")

# Find by XPath (XML path language - like navigation)
bug_link = driver.find_element(by=By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
```

**Why:** Different selectors suit different scenarios. CSS selectors are most intuitive (same as CSS Days 43-44).

### 5. Finding Multiple Elements
```python
# Returns list of all matching elements
all_dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
all_events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

for event in all_events:
    print(event.text)
```

**Why:** `.find_element()` (singular) returns one; `.find_elements()` (plural) returns list.

### 6. Element Interaction
```python
# Get element properties
element = driver.find_element(by=By.NAME, value="my-text")
print(element.tag_name)  # "input"
print(element.get_attribute("placeholder"))  # Get attribute value
print(element.size)  # {"width": 100, "height": 20}

# Interact with element
text_box.send_keys("Hello")  # Type text
submit_button.click()         # Click button
```

**Why:** Element objects provide full control. `send_keys()` simulates typing; `click()` simulates clicking.

### 7. Waiting for Elements (Implicit & Explicit)
```python
# Implicit wait - default wait for all finds
driver.implicitly_wait(0.5)  # Wait up to 0.5 seconds for element to appear

# Elements might not be immediately available (JavaScript loading)
driver.find_element(by=By.NAME, value="my-text")  # Waits before throwing error
```

**Why:** JavaScript loads elements after page loads. Implicit waits prevent "element not found" errors.

### 8. Testing with Assertions
```python
title = driver.title
assert title == "Web form"  # Verify page loaded correctly

message = driver.find_element(by=By.ID, value="message")
value = message.text
assert value == "Received!"  # Verify action succeeded
```

**Why:** Assertions verify automation worked. Essential for testing workflows.

### 9. Scraping Dynamic Content
```python
events = {}

# Loop through elements and build data structure
for n in range(len(upcoming_events)):
    events[n] = {
        "date": upcoming_dates[n].text,
        "event": upcoming_events[n].text,
    }

print(events)  # Dictionary of structured data
```

**Pattern:** Find all elements → Loop → Extract data → Store in structure

**Why:** Structured data (dict, list) is more useful than raw text.

### 10. Browser Automation Workflow
General pattern:
1. Launch browser
2. Navigate to page
3. Find elements
4. Interact (click, type)
5. Wait for results
6. Extract/verify data
7. Repeat for next action
8. Close browser

---

## Common Pitfalls
- **Not calling `.quit()`:** Leaves zombie browser processes running. Always cleanup!
- **Not waiting for elements:** JavaScript loads content after page load. Use implicit waits.
- **Using `.find_element()` vs `.find_elements()`:** Singular returns one; plural returns list. Different return types.
- **Assuming XPath is stable:** XPath breaks easily if structure changes. Use CSS selectors instead.
- **Not importing `By`:** Must import from `selenium.webdriver.common.by`
- **Clicking elements that aren't clickable:** Some elements don't respond to `.click()`. Check if button/link.
- **Not checking element existence:** NoSuchElementException if element not found. Use try/except.
- **Hard-coding paths:** Use `ChromeDriverManager()` instead of hardcoding driver path.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Days 45-47** | Scraping alternatives: Selenium handles JS; BeautifulSoup handles static HTML |
| **Day 46** | Spotify: APIs vs. Selenium (different automation approaches) |
| **Days 14-23** | turtle graphics automated drawing; Selenium automates web interaction |
| **Day 27** | Tkinter GUIs: both create interactive automation |
| **Days 33-40** | Web APIs: Selenium's cousin (both automated data extraction) |

---

## Before You Move On

Make sure you can:
- [ ] Launch Chrome WebDriver with webdriver_manager
- [ ] Navigate to URLs and check page titles
- [ ] Find elements using CSS selectors, ID, class, XPath
- [ ] Distinguish between `.find_element()` and `.find_elements()`
- [ ] Type text with `.send_keys()` and click with `.click()`
- [ ] Use implicit waits for dynamic content loading
- [ ] Extract text and attributes from elements
- [ ] Handle errors when elements don't exist
- [ ] Build data structures from scraped elements
- [ ] Properly close browsers with `.quit()`

---

## Practice Prompt
**Build an automated login & data extraction bot:**

1. **Login:** Automate login to a test site (or your own project from Days 41-44)
2. **Navigate:** Click through menus/pages
3. **Fill forms:** Type in input fields, select dropdowns
4. **Extract data:** Scrape dynamic content generated by JavaScript
5. **Save results:** Store extracted data in CSV or JSON
6. **Error handling:** Handle missing elements gracefully
7. **Assertions:** Verify each step succeeded

**Example:** Login to a job board → Search for specific role → Scrape job listings → Save to CSV

**Challenge:**
- Create bot that logs in multiple accounts and compares data
- Schedule with task scheduler to run daily
- Take screenshots on errors for debugging
- Handle rate limiting (delays between actions)
