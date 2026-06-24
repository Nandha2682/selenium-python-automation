from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def add_to_cart_by_name(self, product_slug):
        """product_slug example: 'sauce-labs-backpack'"""
        locator = (By.ID, f"add-to-cart-{product_slug}")
        self.click(locator)

    def remove_from_cart_by_name(self, product_slug):
        locator = (By.ID, f"remove-{product_slug}")
        self.click(locator)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE) if self.is_visible(self.CART_BADGE) else "0"

    def sort_products(self, value):
        from selenium.webdriver.support.select import Select
        dropdown = self.find(self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(value)  # e.g. "lohi", "hilo", "az", "za"

    def get_product_names(self):
        names = self.find_all((By.CLASS_NAME, "inventory_item_name"))
        return [n.text for n in names]