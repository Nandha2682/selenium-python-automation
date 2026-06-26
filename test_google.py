from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")

print("Title:", driver.title)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("iphone")
search_box.submit()

time.sleep(3)
print("Search done! Title:", driver.title)

driver.quit()
print("Test Passed!")