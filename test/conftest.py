import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    
    with allure.step("Закрыть браузер"):
    browser.quit()