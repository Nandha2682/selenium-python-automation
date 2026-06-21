from selenium.webdriver.common.by import By

class InventoryPage:

     def __init__(self, driver):
        self.driver = driver
        self.add_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

     def add_to_cart(self):
        self.driver.find_element(*self.add_cart_button).click()

     def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

     def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()