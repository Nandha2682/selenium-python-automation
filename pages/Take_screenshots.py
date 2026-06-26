from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(filename="day12.log", level=logging.INFO,
                     format="%(asctime)s - %(levelname)s - %(message)s")

driver = webdriver.Chrome()
driver.get("file:///D:/Test file/Table.html")
logging.info("Page opened successfully")

try:
    driver.find_element(By.ID, "nonexistent").click()
except Exception as e:
    logging.error("There is no expected source")
    driver.save_screenshot("failure_screenshot.png")
    print("Test failed, screenshot saved:", e)

input("Press Enter to close browser...")
driver.quit()