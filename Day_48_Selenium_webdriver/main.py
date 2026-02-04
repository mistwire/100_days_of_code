from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# AUTOMATION: Initialize WebDriver with auto-managed ChromeDriver
driver = webdriver.Chrome(service=Service(
    executable_path=ChromeDriverManager().install()
))

# AUTOMATION: Navigate to Python.org
driver.get("https://www.python.org")

# SELECTOR: By.NAME - find element by name attribute
# .find_element (singular) returns one element
search_bar = driver.find_element(by=By.NAME, value="q")  # Finds <input name="q">
print(search_bar)

# ELEMENT PROPERTIES: Get information about element
print(search_bar.tag_name)  # Tag name ("input")
print(search_bar.get_attribute("placeholder"))  # Get attribute value ("Search")

# KEY CONCEPT: .find_elements (plural) returns list (even if only one element exists)
# By.ID selector targets element with specific id="dive-into-python"
slide_menu = driver.find_elements(by=By.ID, value="dive-into-python")
print(slide_menu)

# SELECTOR: By.CLASS_NAME - find element by class attribute
# Gets <img class="python-logo">
python_logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(python_logo.size)  # Get element dimensions {"width": X, "height": Y}
# print(python_logo.)

# SELECTOR: By.CSS_SELECTOR - most flexible (same syntax as CSS Days 43-44)
# ".documentation-widget a" targets <a> inside .documentation-widget
docs_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(docs_link.text)  # Get visible text content

# SELECTOR: By.XPATH - XML path (precise but brittle)
# XPath like navigating directory structure (/html/body/div/footer...)
# CAUTION: XPath breaks easily if HTML structure changes; avoid when possible
bug_link = driver.find_element(by=By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)

# AUTOMATION: Close browser (critical for cleanup)
driver.quit()

