from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

login_page = LoginPage(driver)
login_page.login("standard_user", "secret_sauce")

inventory_page = InventoryPage(driver)
inventory_page.add_to_cart()
print("Cart count:", inventory_page.get_cart_count())
inventory_page.go_to_cart()
print("Current URL:", driver.current_url)

input("Press Enter to close browser...")
driver.quit()