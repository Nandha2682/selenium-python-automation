from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

print("Step 1: launching driver")

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/iframes.html")
driver.switch_to.frame("iframe1")
driver.find_element(By.ID,"email").send_keys("nandha@yopmail.com")
driver.switch_to.default_content()
print("success")