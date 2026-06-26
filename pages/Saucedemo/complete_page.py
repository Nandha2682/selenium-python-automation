from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.confirmation_header = (By.CLASS_NAME, "complete-header")

    def get_confirmation_text(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(self.confirmation_header)).text