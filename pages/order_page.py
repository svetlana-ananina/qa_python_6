from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import time

import locators
import data


# класс главной страницы
class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    # Открыть Главную страницу
    def open_order_page(self):
        """ открыть страницу заказа по URL """
        self.driver.get(data.URLS.ORDER_PAGE_URL)

    def wait_for_open_order_page(self):
        """ ожидание открытия URL страницы заказа """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(data.URLS.ORDER_PAGE_URL))

    def wait_for_load_order_page(self):
        """ ожидание загрузки страницы заказа (ждем кнопку Далее внизу страницы) """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_NEXT_BUTTON))

    #
    # Методы для работы с общими элементами страницы
    def click_accept_cookies_button(self):
        """ Кликнуть согласие с куками """
        cookie_button = self.driver.find_element(*locators.BASE_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    def wait_for_scooter_button(self):
        """ ожидание кнопки Самокат в хедере """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_SCOOTER_BUTTON))

    def click_scooter_button(self):
        """ кликнуть кнопку Самокат в хедере """
        self.driver.find_element(*locators.ORDER_PAGE_SCOOTER_BUTTON).click()

    def wait_for_logo_button(self):
        """ ожидание кнопки Яндекс в хедере """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_LOGO_BUTTON))

    def click_logo_button(self):
        """ кликнуть кнопку Яндекс в хедере """
        self.driver.find_element(*locators.ORDER_PAGE_LOGO_BUTTON).click()

    def switch_to_new_window(self):
        """ переключиться на новую вкладку """
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_new_window(self):
        """ ждем загрузку страницы в новой вкладке после перехода по клику на логотип Яндекса в хедере """
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(data.URLS.BLANK_URL))
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(data.URLS.DZEN_URL))

    #
    # Методы для работы со 2-й страницей заказа
    def select_station(self, index):
        """ Выбор станции из выпадающего списка по индексу, название станции для проверки """
        if data._debug: print(f'index = {index}')

        # кликаем поле выбора станции
        self.driver.find_element(*locators.ORDER_PAGE_STATION_FIELD).click()

        # ждем появления выпадающего списка станций
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                locators.ORDER_PAGE_SELECT_STATION_LIST))

        # кликаем станцию в списке
        station_xpath = locators.ORDER_PAGE_SELECT_STATION_XPATH.format(index)
        if data._debug: print(f'station_xpath = "{station_xpath}"')
        self.driver.find_element(By.XPATH, station_xpath).click()

        # ждем чтобы выбранная станция появилась в поле
        if data._debug:
            value = self.driver.find_element(*locators.ORDER_PAGE_STATION_VALUE).get_attribute("value")
            print(f'field.value = "{value}"')

    def get_input_fields(self):
        """ получить список полей ввода на странице """
        return self.driver.find_elements(*locators.ORDER_PAGE_INPUT_FIELDS)

    def set_field_value(self, input_field, value):
        """ ввести значение в поле ввода """
        input_field.send_keys(value)

    def click_next_button(self):
        """ кликнуть кнопку Далее """
        self.driver.find_element(*locators.ORDER_PAGE_NEXT_BUTTON).click()

    #
    # функции для работы со 2-й страницей оформления заказа
    def wait_for_load_back_button(self):
        """ Ждем загрузки кнопки Назад """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_BACK_BUTTON))

    def set_value(self, locator, value):
        """ Ввести значение в поле по локатору """
        self.driver.find_element(*locator).send_keys(value)

    def get_value(self, locator):
        """ получить значение поля по локатору """
        value = self.driver.find_element(*locator).get_attribute("value")
        return value

    def wait_element(self, locator):
        """ ожидание появления элемента в DOM по его локатору """
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(locator))

    def wait_visible_element(self, locator):
        """ ожидание появления элемента в DOM по его локатору """
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    def get_element(self, locator):
        """ получить список полей ввода на странице """
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        """ найти элемент в DOM по его локатору и кликнуть """
        self.driver.find_element(*locator).click()

    def click_page_element(self, element):
        """ кликнуть элемент DOM """
        element.click()

    def select_delivery_date(self, delivery_date=None):
        """ Выбор даты доставки """
        if delivery_date:
            # если дата указана, вводим ее в поле
            self.set_value(locators.ORDER_PAGE_DATE_DELIVERY_FIELD, delivery_date)

        # если дата не указана, то кликаем на поле даты, чтобы открылся календарь с текущей датой
        self.driver.find_element(*locators.ORDER_PAGE_DATE_DELIVERY_FIELD).click()

        self.wait_element(locators.ORDER_PAGE_WEEK_ELEMENT)
        self.wait_element(locators.ORDER_PAGE_DAY_ELEMENT)

        element = self.driver.find_element(*locators.ORDER_PAGE_DAY_ELEMENT)
        if data._debug:
            print(f'element = {element}')
        element.click()

        if data._debug:
            value = self.get_value(locators.ORDER_PAGE_DATE_DELIVERY_FIELD)
            print(f'field.value = "{value}"')

    def select_rent_time(self, index=0):
        """ Выбор срока аренды от 1 до 7 дней (индекс от 0 до 6) """
        if index not in (0, 1, 2, 3, 4, 5, 6):
            if data._debug:
                print(f'select_rent_time: получен неправильный индекс, надо 0-6, получено "{index}"')
            index = 0
        # кликаем поле выбора срока аренды
        element = self.driver.find_element(*locators.ORDER_PAGE_RENT_TIME_FIELD)
        if data._debug:
            print(f'element = {element}')
        element.click()
        # ждем загрузку выпадающего списка сроков аренды - от 1 до 7 суток
        self.wait_element(locators.ORDER_PAGE_RENT_TIME_LIST)
        # получаем список кликабельных элементов DOM, соответствующих элементам списка сроков аренды
        elements = self.driver.find_elements(*locators.ORDER_PAGE_RENT_TIME_ITEM)
        if data._debug:
            print(f'elements = {len(elements)}')
        # кликаем на нужный срок аренды по его индексу в списке (от 0 до 6)
        elements[index].click()


