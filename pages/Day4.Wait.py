from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

print("Step 1: launching driver")
driver = webdriver.Chrome()

print("Step 2: opening page")
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
dropdown_element = driver.find_element(By.NAME, "my-select")
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)
print("Dropdown set to:", dropdown.first_selected_option.text)

checkbox = driver.find_element(By.ID, "my-check-1")
if not checkbox.is_selected():
    checkbox.click()
print("Checkbox 1 selected state:", checkbox.is_selected())
input("Press Enter to close browser...")
driver.quit()