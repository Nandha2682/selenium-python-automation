from login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
])
def test_login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login(username, password)

    if username == "locked_out_user":
         error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
         assert "locked out" in error.lower()
    else:
        assert "inventory" in driver.current_url