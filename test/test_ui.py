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


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(
            "«Читай-город» – интернет-магазин книг")


@allure.feature("Локация")
@allure.story("UI")
@allure.title("Изменение города на {city_name}")
@pytest.mark.ui_positive
@pytest.mark.parametrize("city_name", ["Казань", "Нижний Новгород", "Ростов-на-Дону"])
def test_change_city(main_page, city_name):
    with allure.step(f"Изменении локации на город:"
                     f" {city_name}"):
        main_page.change_city(city_name)
    with allure.step("Город успешно изменен"):
        assert main_page.check_city() == city_name


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск книги по названию")
@pytest.mark.ui_positive
@pytest.mark.parametrize("book_name",
                         ["Пикник на обочине", "1984"])
def test_search_book_by_title(main_page, book_name):
    with allure.step(f"Поиск книг с названием"
                     f" {book_name}"):
        main_page.search_items_by_phrase(book_name)
    with allure.step(f"Книга с названием {book_name} есть в ответе"):
        assert book_name in main_page.find_book_titles()


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск книги по автору")
@pytest.mark.ui_positive
@pytest.mark.parametrize("author_name",
                         ["Михаил Лермонтов", "Agatha Christie"])
def test_search_book_by_author(main_page, author_name):
    with allure.step(f"Поиск книг автора: "
                     f" {author_name}"):
        main_page.search_items_by_phrase(author_name)
    with allure.step(f"Книга с названием {author_name} есть в ответе"):
        assert author_name in main_page.find_book_authors()


@allure.feature("UI")
@allure.story("Поиск")
@allure.title("Поиск с пустыми результатами")
@pytest.mark.ui_negative
@pytest.mark.parametrize("search_phrase",
                         ["Фандорин", "Afyljhby"])
def test_search_empty_results(main_page, search_phrase):
    with allure.step(f"Поиск по {search_phrase}"):
        main_page.search_items_by_phrase(search_phrase)
    with allure.step(f"Сообщение об отсутствии книг выведено"):
        assert main_page.check_empty_result() == "Похоже, у нас такого нет"
