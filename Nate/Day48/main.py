from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# URL= "https://www.amazon.com/708620B-AFS-1000B-Filtration-Electrostatic-Pre-Filter/dp/B00004R9LO/ref=dp_fod_1?pd_rd_i=B00004R9LO&psc=1"
URL = "https://www.python.org/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get(URL)
# whole_price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# part_price = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
# price = f'{whole_price.text}.{part_price.text}'
#
# full_price = driver.find_element(By.CSS_SELECTOR, '')
# print(price)

X_PATH = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]'
driver.get(URL)

dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

for i in range(len(dates)):
    event = {
        i: {
            'time': dates[i].text,
            'name': events[i].text
        }
    }
    event_dict.update(event)

print(event_dict)

driver.quit()
