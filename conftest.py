from selenium import webdriver
import pytest
import time

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    time.sleep(3)
    browser.close()