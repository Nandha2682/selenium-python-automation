from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()