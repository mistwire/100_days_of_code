import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

money_available = driver.find_element(by=By.ID, value="money")
print(money_available.text)

buy_cursor = driver.find_element(by=By.ID, value="buyCursor")
buy_grandma = driver.find_element(by=By.ID, value="buyGrandma")
buy_factory = driver.find_element(by=By.ID, value="buyFactory")

i = 0

while i <= 601:
    cookie.click()
    try:
        if int(money_available.text) >= 500:
            buy_factory.click()
        elif int(money_available.text) >= 100:
            buy_grandma.click()
        elif int(money_available.text) >= 50:
            buy_cursor.click()
        else:
            continue
    except:
        None
    # elif int(money_available.text) >= 100:
    #     buy_grandma.click()
    # else:
    #     buy_cursor.click()
    i += 1

print(money_available.text)

input("hit enter to close: ")
