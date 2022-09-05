import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

# Now if you want to click on that anchor tag:
# article_count.click()

# find an element by link text:
help_introduction = driver.find_element(by=By.LINK_TEXT, value="anyone can edit")
help_introduction.click()


# How to enter text into a field
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

time.sleep(5)
