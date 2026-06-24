from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_valid_login(driver):
    logger.info("Starting valid login test")
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_visible(inventory_page.PAGE_TITLE)
    logger.info("Valid login test passed")


def test_invalid_login_wrong_password(driver):
    logger.info("Starting invalid login test - wrong password")
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "wrong_password")

    error_text = login_page.get_error_text()
    assert "do not match" in error_text.lower()
    logger.info("Invalid login test passed")


def test_locked_out_user(driver):
    logger.info("Starting locked out user test")
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_text()
    assert "locked out" in error_text.lower()
    logger.info("Locked out user test passed")