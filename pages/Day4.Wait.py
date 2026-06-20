from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Step 1: launching driver")
driver = webdriver.Chrome()

print("Step 2: opening page")
driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

print("Step 3: waiting for reveal button")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "reveal")))
element.click()
print("Step 4: clicked reveal")

revealed = wait.until(EC.visibility_of_element_located((By.ID, "revealed")))
print("Step 5: got revealed element")
revealed.send_keys("Hello QA")
print(revealed.get_attribute("value"))

input("Press Enter to close browser...")
driver.quit()