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

input("Press Enter to close browser...")
driver.quit()