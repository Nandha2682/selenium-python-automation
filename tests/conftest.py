import pytest
import os
from new_test import get_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drv = get_driver(browser, headless)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")