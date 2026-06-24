from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    SUCCESS_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def get_success_message(self):
        return self.get_text(self.SUCCESS_HEADER)

    def back_to_products(self):
        self.click(self.BACK_HOME_BTN)