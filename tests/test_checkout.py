from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_one_page import CheckoutStepOnePage
from pages.checkout_page_two import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_full_checkout_flow(driver):
    logger.info("Starting full checkout flow test")

    # Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Add item to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart_by_name("sauce-labs-backpack")
    inventory_page.go_to_cart()

    # Cart page
    cart_page = CartPage(driver)
    item_names = cart_page.get_item_names()
    assert "Sauce Labs Backpack" in item_names
    cart_page.checkout()

    # Checkout step 1 - info
    step_one = CheckoutStepOnePage(driver)
    step_one.fill_info("John", "Doe", "600001")

    # Checkout step 2 - overview
    step_two = CheckoutStepTwoPage(driver)
    total_text = step_two.get_total_text()
    logger.info(f"Order total: {total_text}")
    step_two.finish()

    # Checkout complete
    complete_page = CheckoutCompletePage(driver)
    success_msg = complete_page.get_success_message()
    assert "Thank you" in success_msg
    logger.info("Full checkout flow test passed")


def test_checkout_missing_postal_code(driver):
    logger.info("Starting checkout missing postal code test")

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart_by_name("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    step_one = CheckoutStepOnePage(driver)
    step_one.fill_info("John", "Doe", "")  # missing postal code

    error_text = step_one.get_error_text()
    assert "postal code is required" in error_text.lower()
    logger.info("Missing postal code test passed")