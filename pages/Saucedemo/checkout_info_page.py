from selenium.webdriver.common.by import By

class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_info(self, first, last, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first)
        self.driver.find_element(*self.last_name_input).send_keys(last)
        self.driver.find_element(*self.postal_code_input).send_keys(zip_code)

    def continue_to_overview(self):
        self.driver.find_element(*self.continue_button).click()