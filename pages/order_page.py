from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import allure
import pytest
import time

#import locators
#import data
from pages.base_page import BasePage

from locators import MainPageLocators as mploc
from locators import OrderPageLocators as oploc
from locators import BasePageLocators as bploc

from data import URLS as urls
from data import OrderPageData as opdat


class OrderPage(BasePage):
    """ Класс страницы заказа """
    @allure.step('Открываем страницу заказа по URL')
    def open_order_page(self):
        # открываем страницу заказа по URL
        self.open_page(urls.ORDER_PAGE_URL)

        # ждем загрузку страницы заказа
        self.wait_for_load_element(oploc.NEXT_BUTTON)

        # кликаем согласие с куки
        self.click_accept_cookies_button()


    # Методы для работы с формой данных пользователя
    @allure.step('Вводим данные пользователя в форму 1ой на странице заказа {user_info}')
    def create_user(self, user_info):
        # поля ввода input в форме данных о пользователе на странице заказа: 6 (индексы 1-6)
        #   1 - статус заказа (не используется в тесте)
        #   2 - имя пользователя
        #   3 - фамилия пользователя
        #   4 - адрес доставки
        #   5 - станция метро (селектор - выбор из выпадающего списка)
        #   6 - телефон

        # заполняем текстовые поля ввода input, кроме станции метро (индексы 2, 3, 4, 5)
        #   информацией из набора данных пользователя
        self.set_input_value(2, user_info['first_name'])
        self.set_input_value(3, user_info['last_name'])
        self.set_input_value(4, user_info['address'])
        self.set_input_value(6, user_info['tel_number'])

        # выбираем станцию метро из списка по индексу
        self.select_station(user_info['station_index'])

    @allure.step('Вводим текст в поле ввода input с номером {index}')
    def set_input_value(self, index, value):
        """ Вспомогательная функция: ввести текст в поле input по его индексу """
        method, locator = oploc.INPUT_FIELDS
        locator = locator.format(index)
        self.find_element((method, locator)).send_keys(value)

    @allure.step('Получаем значение поля ввода input с номером {index}')
    def check_input_value(self, index):
        """ Вспомогательная функция: получить значение пол input по его индексу """
        method, locator = oploc.INPUT_FIELDS
        locator = locator.format(index)
        return self.find_element((method, locator)).get_attribute("value")

    @allure.step('Выбираем станцию из списка по индексу {index}')
    def select_station(self, index):
        # кликаем поле выбора станции
        self.click_element(oploc.STATION_FIELD)

        # ждем появления выпадающего списка станций
        self.wait_for_presence_of_element(oploc.SELECT_STATION_LIST)

        # кликаем станцию в списке
        method, locator = oploc.SELECT_STATION_BUTTON
        locator = locator.format(index)
        self.click_element((method, locator))

    @allure.step('Получаем название выбранной станции')
    def check_station(self):
        return self.find_element(oploc.STATION_VALUE).get_attribute("value")


    # Методы для работы с формой данных о заказе
    @allure.step('Вводим данные о заказе в форму 2ой на странице заказа {order_info}')
    def create_order(self, order_info):
        # Выбираем дату в поле 'Когда привезти самокат'
        self.select_delivery_date(order_info['delivery_date'])
        # выбираем срок аренды по индексу: 1-7 суток
        self.select_rent_time(order_info['rent_days'])
        # Выбираем цвет самоката (True/False)
        if order_info['black']:   # выбираем цвет 'Черный жемчуг'
            self.click_element(oploc.BLACK_COLOR_FIELD)
        if order_info['grey']:   # выбираем цвет 'Серая безысходность'
            self.click_element(oploc.GREY_COLOR_FIELD)
        # Вводим комментарий для курьера (поле ввода с индексом 4)
        if order_info['comment']:
            self.set_value(oploc.COMMENT_FIELD, order_info['comment'])

    @allure.step('Выбираем дату доставки {delivery_date} в поле "Когда привезти самокат?"')
    def select_delivery_date(self, delivery_date):
        self.set_value(oploc.DATE_DELIVERY_FIELD, delivery_date)

        # кликаем на поле даты, чтобы открылся календарь с введенной датой
        #   (или текущей датой, если дата не указана)
        self.click_element(oploc.DATE_DELIVERY_FIELD)

        # ждем появления элементов календаря - неделя и день
        self.wait_for_presence_of_element(oploc.WEEK_ELEMENT)
        self.wait_for_presence_of_element(oploc.DAY_ELEMENT)

        # ищем выбранный день в календаре и кликаем по нему
        self.click_element(oploc.DAY_ELEMENT)

    @allure.step('Выбираем срок аренды (1-7 дней: {index})')
    def select_rent_time(self, index):
        # кликаем поле выбора срока аренды
        self.click_element(oploc.RENT_TIME_FIELD)

        # ждем загрузку выпадающего списка сроков аренды - от 1 до 7 суток
        self.wait_for_presence_of_element(oploc.RENT_TIME_LIST)

        # кликаем элемент списка с индексом {index}
        method, locator = oploc.RENT_TIME_ITEM
        locator = locator.format(index)
        self.click_element((method, locator))

