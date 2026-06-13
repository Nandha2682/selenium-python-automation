from selenium import webdriver
from pages.login_page import LoginPage
def test_valid_login():
    driver =webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    login_page=LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    assert "inventory" in driver.current_url
    driver.quit()

