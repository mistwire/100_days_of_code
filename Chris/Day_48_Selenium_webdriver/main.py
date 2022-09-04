from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://www.python.org")

# you can use .find_element or .find_elements (and get a list back)
search_bar = driver.find_element(by=By.NAME, value="q")
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

slide_menu = driver.find_elements(by=By.ID, value="dive-into-python")
print(slide_menu)


python_logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(python_logo.size)
# print(python_logo.)

docs_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(docs_link.text)

bug_link = driver.find_element(by=By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)

driver.quit()

