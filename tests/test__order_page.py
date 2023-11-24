from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.firefox

import pytest
import allure
import time

from pages.base_page import BasePage
from pages.order_page import OrderPage
from data import URLS as urls
from data import OrderPageData as opdat

from locators import MainPageLocators as mploc
from locators import OrderPageLocators as oploc
from locators import BasePageLocators as bploc


class TestOrderPage:

    @allure.title('Проверка позитивного сценария оформления заказа с 2мя наборами данных')
    @pytest.mark.parametrize('user_info, order_info', [[opdat.USER_1, opdat.ORDER_1], [opdat.USER_2, opdat.ORDER_2]])
    def test_order_page(self, setup_driver, user_info, order_info):
        """ Проверяем кнопку Самокат в хедере страницы заказа """
        # открываем страницу заказа по URL
        driver = setup_driver
        order_page = OrderPage(driver)
        order_page.open_order_page()


    #@allure.title('Проверка позитивного сценария оформления заказа с двумя наборами данных')
    #@pytest.mark.parametrize('user_info, order_info',
    #                         [[data.DATA.USER_INFO_1, data.DATA.ORDER_INF0_1],
    #                          [data.DATA.USER_INFO_2, data.DATA.ORDER_INF0_2]])
    def test_order_page_order_placement(self, setup_driver, user_info, order_info):
        # Получаем данные пользователя из user_info
        user_first_name = user_info[0]
        user_last_name = user_info[1]
        user_address = user_info[2]
        user_station_name = user_info[3]
        user_telephone = user_info[4]
        user_station_index = user_info[5]

        # открываем страницу заказа по URL
        self.order_page.open_order_page()

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        # 1-я страница заказа - данные пользователя
        # получаем список полей ввода: 6 (индексы 0-5)
        #   0 - статус заказа (не используется в тесте)
        #   1 - имя пользователя
        #   2 - фамилия пользователя
        #   3 - адрес доставки
        #   4 - станция метро (селектор - выбор из выпадающего списка)
        #   5 - телефон
        input_fields = self.order_page.get_input_fields()

        # Проверяем, что на странице 6 полей ввода (1-е поле - статус заказа)
        assert len(input_fields) == 6

        # заполняем текстовые поля ввода input, кроме станции метро (индексы 1, 2, 3, 5)
        # информацией из набора данных пользователя
        #for i in {0, 1, 2, 4}:
        self.order_page.set_field_value(input_fields[1], user_first_name)
        self.order_page.set_field_value(input_fields[2], user_last_name)
        self.order_page.set_field_value(input_fields[3], user_address)
        self.order_page.set_field_value(input_fields[5], user_telephone)

        # выбираем станцию метро из списка по индексу
        self.order_page.select_station(user_station_index)

        # проверяем введенные данные в полях
        selected_station = self.order_page.check_station()

        # Проверяем, что в полях введены данные пользователя
        assert self.order_page.check_field_value(input_fields[1]) == user_first_name
        assert self.order_page.check_field_value(input_fields[2]) == user_last_name
        assert self.order_page.check_field_value(input_fields[3]) == user_address
        assert self.order_page.check_field_value(input_fields[5]) == user_telephone

        # проверяем чтобы выбранная станция появилась в поле
        assert selected_station == user_station_name

        # кликаем кнопку Дальше
        self.order_page.click_next_button()

        # ждем перехода на 2-ю страницу - загрузку кнопки "Назад"
        self.order_page.wait_for_load_back_button()

        # получаем список полей ввода input: 5 (индексы 0-4)
        #   0 - статус заказа (не используется в тесте)
        #   1 - дата доставки
        #   2, 3 - цвет самоката
        #   4 - комментарий для курьера
        input_fields = self.order_page.get_input_fields()

        # Проверяем, что на странице 5 полей ввода (1-е поле - статус заказа)
        assert len(input_fields) == 5

        # Получаем данные заказа из order_info
        order_delivery_date = order_info[0]
        order_rent_time = order_info[1]
        order_select_black_color = order_info[2]
        order_select_grey_color = order_info[3]
        order_comment = order_info[4]
        order_rent_time_text = order_info[5]

        # Выбираем дату в поле 'Когда привезти самокат'
        self.order_page.select_delivery_date(order_delivery_date)

        # выбираем срок аренды по индексу (от 0 до 6 - 1-7 суток)
        self.order_page.select_rent_time(order_rent_time)

        # Выбираем цвет самоката (поля ввода с индексами 2 и 3)
        if order_select_black_color:   # выбираем цвет 'Черный жемчуг'
            self.order_page.click_element(locators.ORDER_PAGE_COLOR_BLACK_FIELD)
        if order_select_grey_color:   # выбираем цвет 'Серая безысходность'
            self.order_page.click_element(locators.ORDER_PAGE_COLOR_GREY_FIELD)

        # Вводим комментарий для курьера (поле ввода с индексом 4)
        if order_comment:
            self.order_page.set_value(locators.ORDER_PAGE_COMMENT_FIELD, order_comment)

        # Получаем введенные данные в полях и проверяем, что они соответствуют данным заказа
        selected_delivery_date = self.order_page.get_value(locators.ORDER_PAGE_DATE_DELIVERY_FIELD)
        selected_rent_time = self.order_page.get_text(locators.ORDER_PAGE_RENT_TIME_VALUE)
        selected_comment = self.order_page.get_value(locators.ORDER_PAGE_COMMENT_FIELD)

        # Проверяем, что дата выбрана и совпадает с указанной в данных заказа
        assert selected_delivery_date
        if order_delivery_date:
            assert selected_delivery_date == order_delivery_date

        # Проверяем, что выбранный срок аренды совпадает с указанным в данных заказа
        assert selected_rent_time == order_rent_time_text
        # Проверяем, что введенный комментарий совпадает с указанным в данных заказа
        assert selected_comment == order_comment

        # Кликаем кнопку "Заказать" внизу страницы
        self.order_page.click_element(locators.ORDER_PAGE_ORDER_BUTTON)

        # ждем появления окна "Хотите оформить заказ?" с кнопкой "Да"
        self.order_page.wait_visible_element(locators.ORDER_PAGE_YES_BUTTON)

        # кликаем кнопку Да
        self.order_page.click_element(locators.ORDER_PAGE_YES_BUTTON)

        # ждем всплывающее окно с кнопкой "Посмотреть статус"
        self.order_page.wait_visible_element(locators.ORDER_PAGE_ORDER_ACCEPTED_BUTTON)
        # проверяем заголовок всплывающего окна "Заказ оформлен"

        assert self.order_page.get_element(locators.ORDER_PAGE_ORDER_ACCEPTED_TITLE)

