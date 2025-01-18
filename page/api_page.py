import urllib.parse
import allure
import requests
from config import UI_BASE_URL


class ApiPage:
    def __init__(self, url: str):
        self.url = url
        self.token = self.set_cookie()  # Устанавливаем куки и получаем токен
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def set_cookie(self):
        response = requests.get(UI_BASE_URL)
        set_cookie = response.headers.get('Set-Cookie')

        if set_cookie:
            # Проверяем наличие set_cookie и извлекаем токен
            if 'access-token' in set_cookie:
                token = set_cookie.split('Bearer%20')[1].split(';')[0]  # Извлекаем токен до точки с запятой
                return urllib.parse.unquote(token)  # Декодируем токен
            else:
                raise Exception("Bearer токен не найден в заголовке Set-Cookie.")
        else:
            raise Exception("Заголовок Set-Cookie не найден в ответе.")

    @allure.step("Поиск книги по фразе: {search_phrase}")
    def search_book(self, search_phrase):
        my_params = {
            "phrase": search_phrase
        }
        resp = requests.get(self.url + 'api/v2/search/product', headers=self.headers, params=my_params)
        return resp
