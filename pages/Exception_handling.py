from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/draggableLists.html")

try:
    driver.find_element(By.ID, "Nonexistent")
except NoSuchElementException:
    print("Element not found — check the locator")

input("Press Enter to close browser...")
driver.quit()