from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_eight_components():
    # AUTOMATION: Launch Chrome browser (webdriver_manager auto-downloads ChromeDriver)
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=ChromeDriverManager().install()
    ))

    # AUTOMATION: Navigate to test page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # TESTING: Verify page loaded correctly
    title = driver.title
    assert title == "Web form"

    # KEY CONCEPT: Implicit wait for elements (JS might load after initial page load)
    driver.implicitly_wait(0.5)

    # AUTOMATION: Find elements using different selectors
    # By.NAME selector targets element with name="my-text" (input field)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    # By.CSS_SELECTOR targets first <button> on page
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # INTERACTION: Send keystrokes (type text) and click button
    text_box.send_keys("Selenium")  # Simulates user typing
    submit_button.click()             # Simulates user clicking button

    # AUTOMATION: Find result element and verify form submission succeeded
    message = driver.find_element(by=By.ID, value="message")
    value = message.text  # Get visible text from element
    assert value == "Received!"  # Verify expected response

    # NOTE: driver.quit() commented out here for debugging; always call in production


test_eight_components()  # Run test function

