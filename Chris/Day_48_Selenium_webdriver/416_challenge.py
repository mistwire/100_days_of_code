from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

