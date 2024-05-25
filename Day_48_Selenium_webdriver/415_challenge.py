from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
driver.get("https://www.python.org")

upcoming_dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
# for time in upcoming_dates:
#     print(time.text)

upcoming_events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
# for event in upcoming_events:
#     print(event.text)

events = {}

for n in range(len(upcoming_events)):
    events[n] = {
        "date": upcoming_dates[n].text,
        "event": upcoming_events[n].text,
    }

print(events)

driver.quit()
