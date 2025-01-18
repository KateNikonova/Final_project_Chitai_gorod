## Дипломный проект автоматизации тестирования на python

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

###  Структура проекта
- **page**: 
   - `api_page.py`: код для взаимодействия с API сайта
   - `main_page.py`: код для взаимодействия с  основной страницей сайта
- **test**:
   - `test_ui.py`: тесты пользовательского интерфейса
   - `test_api.py`: тесты API
- **.gitignore**: файл, который игнорируется при  Git-контроле
- **config.py**: конфигурационный файл 
- **pytest.ini**: конфигурационный файл для фреймворка тестирования pytest
- **requirements.txt**: файл, который содержит список зависимостей проекта
- **README.md**: файл с описанием проекта 


### Ссылка на проект и краткое описание 
https://kate-alex.yonote.ru/doc/kursovaya-rabota-3-UlKN4by0ZZ
....

### Шаги по работе с проектом
1. Склонировать проект `git clone https://github.com/KatrinAlex15/Final_project_Chitai_gorod.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. Получить токен и прописать его в файле `config.py`
3. Запустить тесты:
```python
pytest --alluredir=allure-files # запуск сразу всех тестов;
pytest test/test_api.py --alluredir=allure-files # запуск Api тестов;
pytest test/test_ui.py --alluredir=allure-files # запуск Ui тестов.
```
4. Сгенерировать отчет  `allure generate allure-files --clean -o allure-report`
5. Открыть отчет `allure open allure-report`