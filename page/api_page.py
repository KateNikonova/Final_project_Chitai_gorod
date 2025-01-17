import allure
import requests


class ApiPage:
    def __init__(self, url: str, token: str):
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    @allure.step("Поиск книги с фразой: {search_phrase}")
    def search_book(self, search_phrase):
        my_params = {
            "phrase": search_phrase
        }
        resp = requests.get(self.url + 'api/v2/search/product', headers=self.headers, params=my_params)
        return resp
