import allure
import pytest
from page.api_page import ApiPage
from config import API_URL, API_TOKEN

api = ApiPage(API_URL, API_TOKEN)

# поиск по названию книги
@allure.story("API")
@allure.feature("Поиск")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Мастер и Маргарита"),
    ("Нос"),
    ("1984"),
    ("Рисунок для начинающих")
])
@allure.title("Поиск книги по названию на кириллице: {search_phrase}")
def test_search_positive(search_phrase):
    resp_search = api.search_book(search_phrase)
    assert resp_search.status_code == 200
    assert search_phrase in resp_search.text

# поиск по названию на латинице
@allure.story("API")
@allure.feature("Поиск")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("The ABC Murders"),
    ("Nineteen Eighty-Four"),
    ("Python")
])
@allure.title("Поиск книги по названию на кириллице: {search_phrase}")
def test_search_by_title_in_english(search_phrase):
    resp_search = api.search_book(search_phrase)
    assert resp_search.status_code == 200
    assert search_phrase in resp_search.text



# поиск книг по автору на кириллице
@allure.story("API")
@allure.feature("Поиск")
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


# поиск по автору на латинице
@allure.story("API")
@allure.feature("Поиск")
@pytest.mark.api_positive
@pytest.mark.parametrize("search_phrase", [
    ("Kant"),
    ("Orwell G."),
    ("Agatha Christie")
])
@allure.title("Поиск книги по автору на латинице: {search_phrase}")
def test_search_by_author_in_english(search_phrase):
    resp_search = api.search_book(search_phrase)
    assert resp_search.status_code == 200
    assert search_phrase in resp_search.text


# поиск с пустым запросом
@allure.story("API")
@allure.feature("Поиск")
@pytest.mark.api_positive
@allure.title("Поиск с пустым запросом")
@pytest.mark.api_positive
def test_search_by_empty_string():
    resp_search = api.search_book("")
    assert resp_search.status_code == 400
    assert "Phrase обязательное поле" in resp_search.text
