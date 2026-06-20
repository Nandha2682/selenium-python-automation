from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

badge_text = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
print("Cart count:", badge_text)
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print("Current URL:", driver.current_url)
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("nandha")
driver.find_element(By.ID, "last-name").send_keys("kumar")
driver.find_element(By.ID, "postal-code").send_keys("64166")
driver.find_element(By.ID, "continue").click()
print("Current URL after continue:", driver.current_url)

input("Press Enter to close browser...")
driver.quit()