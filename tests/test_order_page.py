from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.firefox

import pytest
import time

from pages.main_page_questions import MainPageQuestions
from pages.order_page import OrderPage
import data
import locators


class TestOrderPage:

    driver = None
    main_page = None
    order_page = None


    @pytest.fixture()
    def setup_driver(self):
        # создали драйвер для браузера Firefox
        self.driver = webdriver.Firefox()

        # создаем объект класса Главная страница
        self.main_page = MainPageQuestions(self.driver)

        # создаем объект класса страница заказа
        self.order_page = OrderPage(self.driver)

        yield
        # закрываем драйвер
        self.driver.quit()


    def test_main_page_header_order_button(self, setup_driver):
        """ Проверяем верхнюю кнопку Заказать на Главной странице """
        # переходим на страницу тестового приложения
        self.driver.get(data.URLS.MAIN_PAGE_URL)

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # кликаем согласие с куками
        self.main_page.click_accept_cookies_button()

        # прокручиваем страницу до верхней кнопки Заказать
        self.main_page.scroll_to_header_order_button()

        # кликаем верхнюю кнопку Заказать
        self.main_page.click_header_order_button()

        if data._debug: time.sleep(5)

        # ждем перехода на страницу заказа
        self.order_page.wait_for_open_order_page()

        # проверяем, что открылся URL страницы заказа
        assert self.driver.current_url == data.URLS.ORDER_PAGE_URL



    def test_main_page_footer_order_button(self, setup_driver):
        """ Проверяем нижнюю кнопку Заказать на Главной странице """
        # переходим на страницу тестового приложения
        self.driver.get(data.URLS.MAIN_PAGE_URL)

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # кликаем согласие с куками
        self.main_page.click_accept_cookies_button()

        # прокручиваем страницу до нижней кнопки Заказать
        self.main_page.scroll_to_footer_order_button()

        if data._debug: time.sleep(3)

        # кликаем нижнюю кнопку Заказать
        self.main_page.click_footer_order_button()

        if data._debug: time.sleep(3)

        # ждем перехода на страницу заказа
        self.order_page.wait_for_open_order_page()

        # проверяем, что открылся URL страницы заказа
        assert self.driver.current_url == data.URLS.ORDER_PAGE_URL


    def test_order_page_scooter_button(self, setup_driver):
        """ Проверяем кнопку Самокат в хедере страницы заказа """
        # открываем страницу заказа по URL
        self.driver.get(data.URLS.ORDER_PAGE_URL)

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        if data._debug: time.sleep(3)

        # кликаем кнопку Самокат
        self.order_page.click_scooter_button()

        # ждем загрузки главной страницы
        self.main_page.wait_for_open_main_page()

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        if data._debug: time.sleep(3)

        # проверяем, что открылся URL Главной страницы
        assert self.driver.current_url == data.URLS.MAIN_PAGE_URL

    def test_order_page_logo_button(self, setup_driver):
        """ Проверяем кнопку Яндекс в хедере страницы заказа """
        # открываем страницу заказа по URL
        self.driver.get(data.URLS.ORDER_PAGE_URL)

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        if data._debug:
            print(f'len(self.driver.window_handles) = {len(self.driver.window_handles)}')
        if data._debug: time.sleep(3)

        # кликаем кнопку Яндекс
        self.order_page.click_logo_button()

        # Проверяем что открылась новая вкладка
        if data._debug:
            print(f'len(self.driver.window_handles) = {len(self.driver.window_handles)}')

        # Проверяем что открылась новая вкладка
        assert len(self.driver.window_handles) > 1

        # переключаемся на новую вкладку
        self.order_page.switch_to_new_window()

        if data._debug:
            print(f'current_url = "{self.driver.current_url}"')

        # ждем загрузки на новой вкладке страницы Яндекс Дзен редирект
        self.order_page.wait_for_new_window()

        if data._debug:
            print(f'current_url = "{self.driver.current_url}"')

        if data._debug: time.sleep(3)

        assert self.driver.current_url == data.URLS.DZEN_URL
