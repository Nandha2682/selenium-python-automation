from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class OverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.ID, "finish")
    def finish(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()