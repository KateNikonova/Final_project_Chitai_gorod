import pytest
import allure
from selenium import webdriver
from page.main_page import MainPage
from config import UI_BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver, UI_BASE_URL)

@pytest.mark.smoke
@allure.feature("UI")
@allure.story("Smoke")
@allure.title("Проверка заголовка главной страницы")
def test_check_main_page_title(main_page):
    assert main_page.check_page_title("«Читай-город» – интернет-магазин книг")

@pytest.mark.parametrize("city_name", ["Казань", "Нижний Новгород", "Ростов-на-Дону"])
@pytest.mark.ui_positive
@allure.feature("UI")
@allure.story("Локация")
@allure.title("Изменение города на {city_name}")
def test_change_city(main_page, city_name):
    main_page.change_city(city_name)
    assert main_page.check_city() == city_name

@pytest.mark.ui_positive
@allure.feature("UI")
@allure.story("Поиска книги")
@allure.title("Поиск книги по названию")
def test_search_book_by_title(main_page):
    main_page.search_items_by_phrase("Пикник на обочине")
    assert "Пикник на обочине" in main_page.find_book_titles()

@pytest.mark.ui_positive
@allure.feature("UI")
@allure.story("Поиск книги")
@allure.title("Поиск книги по автору")
def test_search_book_by_author(main_page):
    main_page.search_items_by_phrase("Лермонтов")
    assert "Михаил Лермонтов" in main_page.find_book_authors()

@pytest.mark.ui_negative
@allure.feature("UI")
@allure.story("Поиск книги")
@allure.title("Поиск с пустыми результатами")
def test_search_empty_results(main_page):
    main_page.search_items_by_phrase("Фандорин")  # Удивительно, но видимо из-за санкций нет этих книг Акунина
    assert main_page.check_empty_result() == "Похоже, у нас такого нет"
