from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_info_page import CheckoutInfoPage
from overview_page import OverviewPage
from complete_page import CompletePage

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

LoginPage(driver).login("standard_user", "secret_sauce")

inventory = InventoryPage(driver)
inventory.add_to_cart()
print("Cart count:", inventory.get_cart_count())
inventory.go_to_cart()

CartPage(driver).checkout()

checkout_info = CheckoutInfoPage(driver)
checkout_info.fill_info("nandha", "kumar", "64166")
checkout_info.continue_to_overview()

OverviewPage(driver).finish()

confirmation = CompletePage(driver).get_confirmation_text()
print("Confirmation:", confirmation)
assert confirmation == "Thank you for your order!"
print("TEST PASSED ✅")

input("Press Enter to close browser...")
driver.quit()