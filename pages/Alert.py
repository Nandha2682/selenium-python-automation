from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

print("Step 1: launching driver")

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
driver.find_element(By.ID, "alert").click()


alert = driver.switch_to.alert
print(alert.text)
alert.accept()

input("Press Enter to close browser...")
driver.quit()