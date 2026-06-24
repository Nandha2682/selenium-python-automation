from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_info(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)

    def get_error_text(self):
        return self.get_text(self.ERROR_MSG)