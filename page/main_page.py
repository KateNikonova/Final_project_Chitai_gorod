import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)
        self.driver.maximize_window()
        self._close_city_selection()

    def _wait_for_elements(self, by, value, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, value)))
        else:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def _wait_for_text_in_element(self, by, value, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )

    @allure.step("Закрываем окно выбора города")
    def _close_city_selection(self):
        self._wait_for_elements(By.CSS_SELECTOR, ".button.change-city__button.blue").click()

    @allure.step("Проверяем заголовок страницы")
    def check_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.title != "")
        return self.driver.title == expected_title

    @allure.step("Изменяем город на {city_name}")
    def change_city(self, city_name: str):
        self._wait_for_elements(By.CSS_SELECTOR, ".header-city.header-top-bar__city").click()
        self._wait_for_elements(By.CSS_SELECTOR, ".button.change-city__button.light-blue").click()
        self._wait_for_elements(By.XPATH, f"//li[normalize-space(text())='{city_name}']").click()
        self._wait_for_text_in_element(By.CSS_SELECTOR, ".header-city__title", city_name)

    @allure.step("Проверяем текущий город")
    def check_city(self):
        city_title = self._wait_for_elements(By.CSS_SELECTOR, ".header-city__title").text
        return city_title.split(',')[1].strip() if ',' in city_title else city_title.strip()

    @allure.step("Ищем товары по фразе: {phrase}")
    def search_items_by_phrase(self, phrase):
        search_input = self._wait_for_elements(By.CSS_SELECTOR, ".header-search__input")
        search_input.send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.step("Получаем текст элементов по селектору: {css_selector}")
    def _get_element_texts(self, css_selector):
        elements = self._wait_for_elements(By.CSS_SELECTOR, css_selector, multiple=True)
        return [element.text for element in elements]

    @allure.step("Получаем названия книг")
    def find_book_titles(self):
        return self._get_element_texts(".product-title__head")

    @allure.step("Получаем авторов книг")
    def find_book_authors(self):
        return self._get_element_texts(".product-title__author")

    @allure.step("Проверяем сообщение об отсутствии результатов")
    def check_empty_result(self):
        element = self._wait_for_elements(By.CSS_SELECTOR, ".catalog-empty-result__header")
        return element.text.replace('&nbsp;', ' ')
