from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://secure-retreat-92358.herokuapp.com/'


def get_driver(site_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    return driver


driver = get_driver(URL)

fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
submit = driver.find_element(By.CLASS_NAME, 'btn')

fname.send_keys('Nathan')
lname.send_keys('Farrar')
email.send_keys('farroar@farroar.com')
submit.click()
time.sleep(5)




