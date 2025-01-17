import allure
import pytest
from ..page.api_page import ApiPage
from ..config import API_URL, API_TOKEN

api = ApiPage(API_URL, API_TOKEN)

# поиск по названию книги
@allure.feature("Поиск")
@allure.story("API")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Мастер и Маргарита"),
    ("Нос"),
    ("1984"),
    ("Рисунок для начинающих")
])
def test_search_positive(search_phrase):
    allure.dynamic.title(f"Поиск книги по названию на кириллице: {search_phrase}")
    resp_search = api.search_book(search_phrase)
    assert resp_search.status_code == 200
    assert search_phrase in resp_search.text


# поиск книг по автору
@allure.feature("Поиск")
@allure.story("API")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Гоголь"),
    ("Пушкин"),
    ("Лермонтов"),
    ("Тютчев"),
    ("Мамин-Сибиряк")
])
def test_search_positive(search_phrase):
    allure.dynamic.title(f"Поиск книги по автору на кириллице: {search_phrase}")
    resp_search = api.search_book(search_phrase)
    assert resp_search.status_code == 200
    assert search_phrase in resp_search.text

# поиск с пустым запросом
def test_search_by_empty_string():
    resp_search = api.search_book("")
    assert resp_search.status_code == 400
    assert "Phrase обязательное поле" in resp_search.text


# поиск по автору на латинице
def test_search_by_author_in_english():
    resp_search = api.search_book("kant")
    assert resp_search.status_code == 200
    assert "kant" in resp_search.text


# получение информации о книге по нажатию на нее
def test_search_by_title_in_english():
    resp_search = api.search_book("Python")
    assert resp_search.status_code == 200
    assert "Python" in resp_search.text
