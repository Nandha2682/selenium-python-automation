from login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest
import csv
import os

def load_login_data():
    data = []
    csv_path = os.path.join(os.path.dirname(__file__), "login_data.csv")
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
           data.append((row["username"].strip(), row["password"].strip()))
    return data

@pytest.mark.parametrize("username,password", load_login_data())
def test_login(driver, username, password):

    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login(username, password)

    if username == "locked_out_user":
         error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
         assert "locked out" in error.lower()
    else:
        assert "inventory" in driver.current_url