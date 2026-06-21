from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Disable Chrome popups that interfere with automated tests
options = Options()
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Stage 1: Login
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Stage 2: Add to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

badge_text = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
print("Cart count:", badge_text)

# Stage 3: Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print("Current URL:", driver.current_url)

# Stage 4: Checkout info
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("nandha")
driver.find_element(By.ID, "last-name").send_keys("kumar")
driver.find_element(By.ID, "postal-code").send_keys("64166")
driver.find_element(By.ID, "continue").click()

wait.until(EC.url_contains("checkout-step-two"))
print("Current URL after continue:", driver.current_url)

# Stage 5: Finish and verify confirmation
wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

confirmation_text = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
).text
print("Confirmation message:", confirmation_text)

assert confirmation_text == "Thank you for your order!"
print("TEST PASSED ✅")

input("Press Enter to close browser...")
driver.quit()