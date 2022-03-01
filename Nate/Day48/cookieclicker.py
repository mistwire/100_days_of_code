from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import threading
import re

URL = "https://orteil.dashnet.org/cookieclicker/"


def driver_setup(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    return driver


def checks():
    threading.Timer(5.0, checks).start()
    product_prices = cookie_driver.find_elements(By.CSS_SELECTOR, 'div.product.unlocked.enabled span.price')
    products = cookie_driver.find_elements(By.CSS_SELECTOR, 'div.product.unlocked.enabled')
    prices = []
    for product in product_prices:
        price = re.findall(r'[0-9]+', product.text)
        price = int("".join(price))
        prices.append(price)

    if len(prices) > 0:
        max_price = max(prices)
        price_index = prices.index(max_price)
        products[price_index].click()


cookie_driver = driver_setup(URL)

big_cookie = cookie_driver.find_element(By.CSS_SELECTOR, '#bigCookie')
cookie_count = cookie_driver.find_element(By.CSS_SELECTOR, '#cookies')
cookie_bakery_name = cookie_driver.find_element(By.CSS_SELECTOR, '#bakeryName')

checks()

while True:
    big_cookie.click()


