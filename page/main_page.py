from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..config import UI_BASE_URL


class MainPage:

    # Настройка браузера, переход на сайт, закрытие окна с выбором города
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(UI_BASE_URL)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".button.change-city__button.blue").click()  # Закрываем окно с выбором города

    # Проверка заголовка страницы
    def check_page_title(self, expected_title):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: driver.title != "")
        current_title = self.driver.title
        if current_title == expected_title:
            return True
        else:
            return False

    # Изменение города
    def change_city(self, city_name: str) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-city.header-top-bar__city"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.change-city__button.light-blue"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[normalize-space(text())='{city_name}']"))).click()

        # Ожидание обновления заголовка города
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".header-city__title"),
            city_name
        ))

    def check_city(self):
        wait = WebDriverWait(self.driver, 10)
        string_to_trim = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-city__title"))).text
        return string_to_trim.split(',')[1].strip()


    # Поиск товаров по фразе
    def search_items_by_phrase(self, phrase):
        self.driver.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # Получение результатов поиска (список названий книг)
    def find_book_titles(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-title__head")))
        elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-title__head")))
        titles = [element.text for element in elements]
        return titles

    # Получение результатов поиска (список авторов книг)
    def find_book_authors(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-title__author")))
        elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-title__author")))
        authors = [element.text for element in elements]
        return authors

    # Проверка сообщения об отсутствии результатов
    def check_empty_result(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".catalog-empty-result__header")))
        text = element.text.replace('&nbsp;', ' ')
        return text
