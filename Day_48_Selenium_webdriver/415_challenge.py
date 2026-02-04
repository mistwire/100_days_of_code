from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# AUTOMATION: Launch browser
driver = webdriver.Chrome(service=Service(
    executable_path=ChromeDriverManager().install()
))

# AUTOMATION: Navigate to Python.org
driver.get("https://www.python.org")

# SCRAPING: Find all event dates using CSS selector ".event-widget time"
# CSS selector ".event-widget time" targets <time> elements inside elements with class="event-widget"
# .find_elements (plural) returns list
upcoming_dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
# for time in upcoming_dates:
#     print(time.text)

# SCRAPING: Find all event links using CSS selector ".event-widget li a"
# Targets <a> tags inside <li> inside .event-widget
upcoming_events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
# for event in upcoming_events:
#     print(event.text)

# PATTERN: Build structured data (dictionary) from scraped elements
events = {}

# LOGIC: Parallel iteration - loop through indices, access both dates and events
for n in range(len(upcoming_events)):
    events[n] = {
        "date": upcoming_dates[n].text,  # Get text from nth date element
        "event": upcoming_events[n].text,  # Get text from nth event element
    }

print(events)  # Pretty print dictionary of all events with dates

# AUTOMATION: Close browser (essential cleanup - prevents zombie processes)
driver.quit()
