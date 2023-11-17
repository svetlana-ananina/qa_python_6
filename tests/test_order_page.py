from selenium import webdriver
from selenium.webdriver.support.ui import Select
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


    @pytest.mark.parametrize('locator', [locators.MAIN_PAGE_HEADER_ORDER_BUTTON,
                                         locators.MAIN_PAGE_FOOTER_ORDER_BUTTON])
    def test_main_page_order_button(self, setup_driver, locator):
        """ Проверяем верхнюю и нижнюю кнопку Заказать на Главной странице """
        # открываем Главную страницу
        #self.driver.get(data.URLS.MAIN_PAGE_URL)
        self.main_page.open_main_page()

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # кликаем согласие с куками
        self.main_page.click_accept_cookies_button()

        # прокручиваем страницу до кнопки Заказать
        self.main_page.scroll_to_order_button(locator)

        if data._debug: time.sleep(5)

        # кликаем нижнюю кнопку Заказать
        self.main_page.click_order_button(locator)

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


    @pytest.mark.parametrize('user_info',
                             [data.DATA.INFO_USER_1])
#                              [data.DATA.INFO_USER_1, data.DATA.INFO_USER_2])
    def test_order_page_order_placement(self, setup_driver, user_info):
        """ Проверяем оформление заказа """
        # открываем страницу заказа по URL
        self.driver.get(data.URLS.ORDER_PAGE_URL)

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        # получаем список полей ввода
        input_fields = self.order_page.get_input_fields()

        if data._debug:
            print(f'len = {len(input_fields)}')
        # Проверяем, что на странице 6 полей ввода (1-е поле - статус заказа)
        assert len(input_fields) == 6

        # заполняем текстовые поля, кроме станции метро
        for i in {0, 1, 2, 4}:
            self.order_page.set_field_value(input_fields[i+1], user_info[i])

        # выбираем станцию метро из списка по индексу
        self.order_page.select_station(user_info[5])

        # кликаем кнопку Дальше
        self.order_page.click_next_button()

        # ждем перехода на 2-ю страницу - кнопку Назад
        self.order_page.wait_for_load_back_button()

        # получаем список полей ввода
        input_fields = self.order_page.get_input_fields()

        if data._debug:
            print(f'len = {len(input_fields)}')
        # Проверяем, что на странице 6 полей ввода (1-е поле - статус заказа)
        assert len(input_fields) == 5

        #self.order_page.set_field_value(input_fields[1], '01.12.2023')
        #self.order_page.set_value(locators.ORDER_PAGE_DATE_PICKER, data.DATA.ORDER_INF0_1[0])
        self.order_page.set_value(locators.ORDER_PAGE_DATE_PICKER, '01.12.2023')

        if data._debug:
            #value = self.order_page.get_field_value(([By.XPATH, "(.//input)[2]"]))
            value = self.order_page.get_field_value(locators.ORDER_PAGE_DATE_PICKER)
            print(f'field.value = "{value}"')

        # выбираем срок аренды по индексу (от 1 до 7 - 1-7 суток)
        #self.order_page.select_rent_time(data.DATA.ORDER_INF0_1[1])
        self.order_page.select_rent_time(1)

        if data._debug:
            time.sleep(5)
