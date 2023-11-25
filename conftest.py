from selenium import webdriver
import allure
import pytest


@allure.step('Открываем браузер Firefox')
@pytest.fixture()
def setup_driver():
    # создали драйвер для браузера Firefox
    driver = webdriver.Firefox()

    yield driver
    # закрываем драйвер после использования
    driver.quit()

