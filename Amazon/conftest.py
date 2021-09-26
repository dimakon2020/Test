import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
# для выбора браузера firefox команда:pytest -s -v --browser_name=firefox test___.py
@pytest.fixture(scope="function")
def browser(request):
    #print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    #browser.set_window_size(1440, 800)
    #browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()