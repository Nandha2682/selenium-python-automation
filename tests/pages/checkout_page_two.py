from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    FINISH_BTN = (By.ID, "finish")
    CANCEL_BTN = (By.ID, "cancel")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_total_text(self):
        return self.get_text(self.TOTAL)

    def get_item_names(self):
        names = self.find_all(self.ITEM_NAMES)
        return [n.text for n in names]

    def finish(self):
        self.click(self.FINISH_BTN)