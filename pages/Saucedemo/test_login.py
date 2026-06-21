from login_page import LoginPage
def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url