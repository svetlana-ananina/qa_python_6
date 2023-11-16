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
        # создали драйвер для браузера Chrome
        self.driver = webdriver.Firefox()

        # создаем объект класса Главная страница
        self.main_page = MainPageQuestions(self.driver)

        # создаем объект класса страница заказа
        self.order_page = OrderPage(self.driver)

        yield
        # закрываем драйвер
        self.driver.quit()

    def test_main_page_header_order_button(self, setup_driver):
        # переходим на страницу тестового приложения
        self.driver.get(data.URLS.MAIN_PAGE_URL)

        # создаем объект класса Главная страница
        # self.main_page = MainPageQuestions(self.driver)

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # кликаем согласие с куки
        self.main_page.click_accept_cookies_button()

        # прокручиваем страницу до
        self.main_page.scroll_to_header_order_button()

        # кликаем
        self.main_page.click_header_order_button()

        if data._debug: time.sleep(5)

        self.main_page.wait_for_open_order_page()

        assert self.driver.current_url == data.URLS.ORDER_PAGE_URL



    def test_main_page_footer_order_button(self, setup_driver):
        # переходим на страницу тестового приложения
        self.driver.get(data.URLS.MAIN_PAGE_URL)

        # создаем объект класса Главная страница
        self.main_page = MainPageQuestions(self.driver)

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # кликаем согласие с куки
        self.main_page.click_accept_cookies_button()

        # прокручиваем страницу до
        self.main_page.scroll_to_footer_order_button()

        if data._debug: time.sleep(3)

        # кликаем
        self.main_page.click_footer_order_button()

        if data._debug: time.sleep(3)

        self.main_page.wait_for_open_order_page()

        assert self.driver.current_url == data.URLS.ORDER_PAGE_URL



