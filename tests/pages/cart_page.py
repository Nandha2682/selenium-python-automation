from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def get_item_names(self):
        names = self.find_all((By.CLASS_NAME, "inventory_item_name"))
        return [n.text for n in names]

    def checkout(self):
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)