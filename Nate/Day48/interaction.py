from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://en.wikipedia.org/wiki/Main_Page'
x_path = '//*[@id="articlecount"]/a[1]'


def get_driver(site_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    return driver


driver = get_driver(URL)
# articles = driver.find_element(By.XPATH, x_path)
articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(articles.text)
articles.click()






time.sleep(5)
driver.quit()



