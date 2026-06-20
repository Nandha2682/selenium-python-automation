from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/upload.html")
driver.find_element(By.ID, "upload").send_keys(r"D:\Test file\Test.txt")

input("Press Enter to close browser...")
driver.quit()
print("success")