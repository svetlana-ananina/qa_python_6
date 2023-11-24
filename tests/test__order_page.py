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

    @allure.title('Проверка заполнения данных пользователя на странице оформления заказа')
    @allure.description('Заполняем форму данных пользователя на странице оформления заказа'
                        ' и проверяем введенные данные: {user_info}')
    @pytest.mark.parametrize('user_info, order_info', [[opdat.USER_1, opdat.ORDER_1], [opdat.USER_2, opdat.ORDER_2]])
    def test_order_page_form_1(self, setup_driver, user_info, order_info):
    #def test_order_page_form_1(self, setup_driver, user_info=opdat.USER_1):
        """ Позитивный сценарий оформления заказа: заполнение формы данных пользователя.
            Параметризованный тест для двух наборов данных пользователя.
        """
        # Открываем Главную страницу
        # инициализируем драйвер веб-браузера
        driver = setup_driver
        order_page = OrderPage(driver)
        # открываем страницу заказа по URL, ждем ее загрузку и кликаем куки
        order_page.open_order_page()
        # Вводим данные пользователя в форму на странице заказа
        order_page.create_user(user_info)
        # проверяем введенные данные пользователя
        # поля ввода input в форме данных о пользователе на странице заказа: 6 (индексы 1-6)
        #   1 - статус заказа (не используется в тесте)
        #   2 - имя пользователя
        #   3 - фамилия пользователя
        #   4 - адрес доставки
        #   5 - станция метро (селектор - выбор из выпадающего списка)
        #   6 - телефон
        assert order_page.check_input_value(2) == user_info['first_name']
        assert order_page.check_input_value(3) == user_info['last_name']
        assert order_page.check_input_value(4) == user_info['address']
        assert order_page.check_input_value(6) == user_info['tel_number']


    @allure.title('Проверка заполнения данных о заказе на странице оформления заказа')
    @allure.description('Заполняем форму данных о заказе на странице оформления заказа'
                        ' и проверяем введенные данные: {order_info}')
    @pytest.mark.parametrize('user_info, order_info', [[opdat.USER_1, opdat.ORDER_1], [opdat.USER_2, opdat.ORDER_2]])
    def test_order_page_form_2(self, setup_driver, user_info, order_info):
    #def test_order_page_form_2(setup_driver, user_info, order_info):
        """ Позитивный сценарий оформления заказа: заполнения формы данных о заказе.
            Параметризованный тест для двух наборов данных пользователя и заказа.
        """
        # инициализируем драйвер веб-браузера
        driver = setup_driver
        order_page = OrderPage(driver)
        # открываем страницу заказа по URL, ждем ее загрузку и кликаем куки
        order_page.open_order_page()
        # Вводим данные пользователя в форму 1 на странице заказа
        order_page.create_user(user_info)

        # кликаем кнопку "Дальше"
        order_page.click_element(oploc.NEXT_BUTTON)
        # ждем перехода на 2-ю страницу - загрузку кнопки "Назад"
        order_page.wait_for_load_element(oploc.BACK_BUTTON)
        # вводим данные заказа в форму 2 на странице заказа
        order_page.create_order(order_info)

        # Получаем введенные данные в полях и проверяем, что они соответствуют данным заказа
        assert order_page.check_value(oploc.DATE_DELIVERY_FIELD) == order_info['delivery_date']
        assert order_page.check_text(oploc.RENT_TIME_VALUE) == order_info['rent_text']
        assert order_page.check_value(oploc.COMMENT_FIELD) == order_info['comment']


    @allure.title('Проверка позитивного сценария оформления заказа с двумя наборами данных')
    @allure.description('Заполняем форму заказа и проверяем, что появилось всплывающее окно'
                        ' с сообщением об успешном оформлении заказа')
    @pytest.mark.parametrize('user_info, order_info', [[opdat.USER_1, opdat.ORDER_1], [opdat.USER_2, opdat.ORDER_2]])
    def test_order_page_make_order(self, setup_driver, user_info, order_info):
        # инициализируем драйвер веб-браузера
        driver = setup_driver
        order_page = OrderPage(driver)
        # открываем страницу заказа по URL, ждем ее загрузку и кликаем куки
        order_page.open_order_page()
        # заполняем 1-ю страницу формы заказа - данные пользователя
        order_page.create_user(user_info)

        # кликаем кнопку "Дальше"
        order_page.click_element(oploc.NEXT_BUTTON)
        # ждем перехода на 2-ю страницу - загрузку кнопки "Назад"
        order_page.wait_for_load_element(oploc.BACK_BUTTON)
        # заполняем 2-ю страницу формы заказа - данные о заказе
        order_page.create_order(order_info)

        # Кликаем кнопку "Заказать" внизу страницы
        order_page.click_element(oploc.ORDER_BUTTON)
        # ждем появления окна "Хотите оформить заказ?" с кнопкой "Да"
        order_page.wait_for_load_element(oploc.ORDER_CONFIRM)
        # кликаем кнопку 'Да"
        order_page.click_element(oploc.YES_BUTTON)
        # ждем всплывающее окно об успешном оформлении заказа с кнопкой "Посмотреть статус"
        order_page.wait_for_load_element(oploc.ORDER_COMPLETED)
        # проверяем заголовок всплывающего окна "Заказ оформлен"
        assert opdat.ORDER_CONFIRM_TITLE in order_page.check_text(oploc.ORDER_COMPLETED)

