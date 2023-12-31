# qa_python_6
# Тест-сьют для проверки UI приложения "Самокат" с помощью Selenium и Pytest

Файлы:
- tests/ - папка с файлами тестов
- tests/test_main_page_questions.py - тесты блока вопросов и ответов на Главной странице
- tests/test_order_page.py - тесты страницы заказа

- pages/ - папка с файлами страниц Page Object
- pages/main_page_questions.py - файл POM Главной страницы
- pages/order_page.py - файл POM страницы заказа

- locators.py - указатели для поиска элементов DOM
- data.py - другие константы и URL-адреса

- .gitignore - файл для проекта в Git/GinHub
- requirements.txt - файл с внешними зависимостями
- README.md - файл с описанием проекта (этот файл)

Для запуска тестов должны быть установлены пакеты: 
- pytest,
- selenium, 
- allure-pytest и
- allure-python-commons.
- 
Для генерации отчетов необходимо дополнительно установить:
- фреймворк Allure,
- JDK

Запуск всех тестов выполняется командой:

    pytest -v ./tests

Запуск тестов с генерацией отчета Allure выполняется командой:

    pytest -v ./tests  --alluredir=allure_results

Генерация отчета выполняется командой:

    allure serve allure_results
