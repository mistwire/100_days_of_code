from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&keywords=principal%20azure%20architect"
login_user = os.environ['LI_USER']
login_pass = os.environ['LI_PASS']


def driver_setup(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    return driver


linkedin_driver = driver_setup(URL)

sign_in = linkedin_driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
time.sleep(1)

username_input = linkedin_driver.find_element(By.NAME, 'session_key')
password_input = linkedin_driver.find_element(By.NAME, 'session_password')
submit_btn = linkedin_driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
username_input.send_keys(login_user)
password_input.send_keys(login_pass)
submit_btn.click()

easy_apply_btn = linkedin_driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
easy_apply_btn.click()

