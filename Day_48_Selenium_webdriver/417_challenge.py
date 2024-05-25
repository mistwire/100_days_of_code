from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Bob")
last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Wehadababyitsaboy")
email_address = driver.find_element(by=By.NAME, value="email")
email_address.send_keys("Bob@wehadababy.com")
button = driver.find_element(by=By.CSS_SELECTOR, value="button")
button.click()



