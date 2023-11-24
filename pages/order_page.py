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
from base_page import BasePage

from locators import MainPageLocators as mploc
from locators import OrderPageLocators as oploc
from locators import BasePageLocators as bploc

from data import URLS as urls
from data import OrderPageData as opdat


class OrderPage(BasePage):
    """ Класс страницы заказа """
    #
    # Методы для работы с 1-й страницей заказа
    def open_order_page(self):
        # открываем страницу заказа по URL
        self.open_page(urls.ORDER_PAGE_URL)

        # ждем загрузки страницы заказа
        self.wait_for_load_element(oploc.NEXT_BUTTON)

        # кликаем согласие с куки
        self.click_accept_cookies_button()


    def create_user(self, user_info):
        # получаем список полей ввода: 6 (индексы 1-6)
        #   1 - статус заказа (не используется в тесте)
        #   2 - имя пользователя
        #   3 - фамилия пользователя
        #   4 - адрес доставки
        #   5 - станция метро (селектор - выбор из выпадающего списка)
        #   6 - телефон
        #input_fields = self.get_input_fields()

        # заполняем текстовые поля ввода input, кроме станции метро (индексы 2, 3, 4, 5)
        #   информацией из набора данных пользователя
        self.set_input_field_value(2, user_info['first_name'])
        self.set_input_field_value(3, user_info['last_name'])
        self.set_input_field_value(4, user_info['address'])
        self.set_input_field_value(6, user_info['tel_number'])

        # выбираем станцию метро из списка по индексу
        self.select_station(user_info['station_index'])


    @allure.step('Получаем элемент поля ввода input с номером {index}')
    def find_input_field(self, index):
        method, locator = oploc.INPUT_FIELDS
        locator = locator.format(index)
        return self.find_element(method, locator)

    @allure.step('Вводим значение в поле ввода input с номером {index}')
    def set_input_field_value(self, index, text_value):
        method, locator = oploc.INPUT_FIELDS
        locator = locator.format(index)
        self.find_element(method, locator).send_keys(text_value)

    @allure.step('Получаем значение в поле ввода input с номером {index}')
    def get_input_field_value(self, index):
        method, locator = oploc.INPUT_FIELDS
        locator = locator.format(index)
        return self.find_element(method, locator).get_attribute("value")

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

    @allure.step('Проверяем название выбранной станции')
    def check_station(self):
        station_name = self.driver.find_element(*locators.ORDER_PAGE_STATION_VALUE).get_attribute("value")
        return self.check_value(order_page_locators.SELECTED_STATION_VALUE)


    #########################
    @allure.step('Получаем список элементов полей ввода input на странице')
    def get_input_fields(self):
        #return self.driver.find_elements(*locators.ORDER_PAGE_INPUT_FIELDS)
        return super().find_all_elements(oploc.INPUT_FIELDS)

    @allure.step('Кликаем кнопку "Дальше"')
    def click_next_button(self):
        #self.driver.find_element(*locators.ORDER_PAGE_NEXT_BUTTON).click()
        super().click_element(oploc.NEXT_BUTTON)


    allure.step('Проверяем название выбранной станции')
    def check_station(self):
        station_name = self.driver.find_element(*locators.ORDER_PAGE_STATION_VALUE).get_attribute("value")
        return self.check_value(order_page_locators.SELECTED_STATION_VALUE)

    #
    # функции для работы со 2-й страницей оформления заказа
    @allure.step('Ждем загрузку 2-й страницы заказа - появления кнопки "Назад"')
    def wait_for_load_back_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_BACK_BUTTON))
        return super().wait_for_load_element(order_page_locators.BACK_BUTTON)

    @allure.step('Выбираем дату доставки {delivery_date} в поле "Когда привезти самокат?"')
    def select_delivery_date(self, delivery_date=''):
        if delivery_date:
            # если дата указана, вводим ее в поле
            self.set_value(order_page_locators.DATE_DELIVERY_FIELD, delivery_date)

        # кликаем на поле даты, чтобы открылся календарь с введенной датой (или текущей датой, если дата не указана)
        #self.driver.find_element(*locators.ORDER_PAGE_DATE_DELIVERY_FIELD).click()
        self.click_element(order_page_locators.DATE_DELIVERY_FIELD)

        # ждем появления элементов календаря - неделя и день
        #self.wait_element(locators.ORDER_PAGE_WEEK_ELEMENT)
        #self.wait_element(locators.ORDER_PAGE_DAY_ELEMENT)
        self.wait_for_presence_of_element(order_page_locators.WEEK_ELEMENT)
        self.wait_for_presence_of_element(order_page_locators.DAY_ELEMENT)

        # ищем выбранный день в календаре и кликаем по нему
        #element = self.driver.find_element(*locators.ORDER_PAGE_DAY_ELEMENT)
        #element.click()
        self.click_element(order_page_locators.DAY_ELEMENT)

    @allure.step('Выбираем срок аренды (index 0-6: {index})')
    def select_rent_time(self, index=0):
        #if index not in (0, 1, 2, 3, 4, 5, 6):
        #    index = 0

        # кликаем поле выбора срока аренды
        #element = self.driver.find_element(*locators.ORDER_PAGE_RENT_TIME_FIELD)
        #element.click()
        self.click_element(order_page_locators.RENT_TIME_FIELD)

        # ждем загрузку выпадающего списка сроков аренды - от 1 до 7 суток
        #self.wait_element(locators.ORDER_PAGE_RENT_TIME_LIST)
        self.wait_for_presence_of_element(order_page_locators.RENT_TIME_LIST)

        # получаем список кликабельных элементов DOM, соответствующих элементам списка сроков аренды
        #elements = self.driver.find_elements(*locators.ORDER_PAGE_RENT_TIME_ITEM)
        elements = self.find_all_elements(order_page_locators.RENT_TIME_ITEM)

        # кликаем на нужный срок аренды по его индексу в списке (от 0 до 6)
        #elements[index].click()
        self.click_page_element(elements[index])


