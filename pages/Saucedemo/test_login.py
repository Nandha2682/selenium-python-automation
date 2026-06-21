from selenium import webdriver
from login_page import LoginPage
import pytest

@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url