import allure
import pytest
from page.api_page import ApiPage
from config import API_URL

api = ApiPage(API_URL)


# поиск по названию книги
@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск книги по названию на кириллице: {search_phrase}")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Мастер и Маргарита"),
    ("Нос"),
    ("1984"),
    ("рисунок для начинающих")
])
def test_search_by_title_in_russian(search_phrase):
    with allure.step(f"Отправка запроса на поиск книги с названием:"
                     f" {search_phrase}"):
        resp_search = api.search_book(search_phrase)

    with allure.step("Статус код = 200"):
        assert resp_search.status_code == 200

    with allure.step(f"Название '{search_phrase}'"
                     f" содержится в теле ответе"):
        assert search_phrase in resp_search.text


# поиск по названию на латинице
@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск книги по названию на кириллице: {search_phrase}")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("The ABC Murders"),
    ("Nineteen Eighty-Four"),
    ("Python")
])
def test_search_by_title_in_english(search_phrase):
    with allure.step(f"Отправка запроса на поиск книги с названием: "
                     f"{search_phrase}"):
        resp_search = api.search_book(search_phrase)

    with allure.step("Статус код = 200"):
        assert resp_search.status_code == 200

    with allure.step(f"Название '{search_phrase}'"
                     f" содержится в теле ответе"):
        assert search_phrase in resp_search.text


# поиск книг по автору на кириллице
@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск книги по названию на кириллице: {search_phrase}")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Гоголь"),
    ("Пушкин"),
    ("Лермонтов"),
    ("Тютчев"),
    ("Мамин-Сибиряк")
])
def test_search_by_author_in_russian(search_phrase):
    with allure.step(f"Отправка запроса на поиск книг по автору:"
                     f" {search_phrase}"):
        resp_search = api.search_book(search_phrase)

    with allure.step("Статус код"):
        assert resp_search.status_code == 200

    with allure.step(f"Имя автора '{search_phrase}'"
                     f" содержится в теле ответа"):
        assert search_phrase in resp_search.text


# поиск по автору на латинице
@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск книги по автору на латинице: {search_phrase}")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Kant"),
    ("Orwell G."),
    ("Agatha Christie")
])
def test_search_by_author_in_english(search_phrase):
    with allure.step(f"Отправка запроса на поиск книг по автору:"
                     f" {search_phrase}"):
        resp_search = api.search_book(search_phrase)

    with allure.step("Статус код = 200"):
        assert resp_search.status_code == 200

    with allure.step(f"Имя автора '{search_phrase}'"
                     f" содержится в теле ответе"):
        assert search_phrase in resp_search.text


# поиск с пустым запросом
@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск с пустым запросом")
@pytest.mark.api_positive
@pytest.mark.api_positive
def test_search_by_empty_string():
    with allure.step("Отправка запроса на поиск книг с пустой строкой"):
        resp_search = api.search_book("")

    with allure.step("Статус код = 200"):
        assert resp_search.status_code == 400

    with allure.step("Сообщение об ошибке содержится в теле ответа"):
        assert "Phrase обязательное поле" in resp_search.text
