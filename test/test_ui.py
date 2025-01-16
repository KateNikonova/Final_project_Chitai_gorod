import pytest
from selenium import webdriver
from ..page.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.mark.smoke
def test_check_main_page_title(main_page):
    assert main_page.check_page_title("«Читай-город» – интернет-магазин книг")


@pytest.mark.parametrize("city_name", ["Казань", "Нижний Новгород", "Ростов-на-Дону"])
@pytest.mark.ui_positive
def test_change_city(main_page, city_name):
    main_page.change_city(city_name)
    assert main_page.check_city() == city_name


@pytest.mark.ui_positive
def test_search_book_by_title(main_page):
    main_page.search_items_by_phrase("Пикник на обочине")
    assert "Пикник на обочине" in main_page.find_book_titles()


@pytest.mark.ui_positive
def test_search_book_by_author(main_page):
    main_page.search_items_by_phrase("Лермонтов")
    assert "Михаил Лермонтов" in main_page.find_book_authors()


@pytest.mark.ui_negative
def test_search_empty_results(main_page):
    main_page.search_items_by_phrase("Фандорин")  # Удивительно, но видимо из-за санкций нет этих книг Акунина
    assert main_page.check_empty_result() == "Похоже, у нас такого нет"

