from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import allure
import pytest
import time

import locators
import data


class OrderPage:
    """ Класс страницы заказа """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу заказа по URL')
    def open_order_page(self):
        self.driver.get(data.URLS.ORDER_PAGE_URL)

    def wait_for_open_order_page(self):
        """ ожидание открытия URL страницы заказа """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(data.URLS.ORDER_PAGE_URL))

    @allure.step('Ждем загрузку страницы заказа')
    def wait_for_load_order_page(self):
        """ ожидание загрузки страницы заказа (ждем кнопку Далее внизу страницы) """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_NEXT_BUTTON))

    #
    # Методы для работы с общими элементами страницы
    @allure.step('Кликаем согласие с куки')
    def click_accept_cookies_button(self):
        cookie_button = self.driver.find_element(*locators.BASE_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    @allure.step('Ждем загрузку кнопки "Самокат"')
    def wait_for_scooter_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_SCOOTER_BUTTON))

    @allure.step('Кликаем кнопку "Самокат"')
    def click_scooter_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_SCOOTER_BUTTON).click()

    @allure.step('Ждем загрузку логотипа Яндекса')
    def wait_for_logo_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_LOGO_BUTTON))

    @allure.step('Кликаем логотип Яндекса')
    def click_logo_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_LOGO_BUTTON).click()

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ждем загрузку на новой вкладке главной страницы Дзен через редирект')
    def wait_for_new_window(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(data.URLS.BLANK_URL))
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(data.URLS.DZEN_URL))

    #
    # Методы для работы с 1-й страницей заказа
    @allure.step('Получаем список элементов полей ввода input на странице')
    def get_input_fields(self):
        return self.driver.find_elements(*locators.ORDER_PAGE_INPUT_FIELDS)

    @allure.step('Вводим данные пользователя в поле ввода input по элементу DOM')
    def set_field_value(self, input_field, value):
        input_field.send_keys(value)

    @allure.step('Получаем значение из поля input по элементу DOM')
    def check_field_value(self, input_field):
        value = input_field.get_attribute("value")
        return value

    @allure.step('Кликаем кнопку "Дальше"')
    def click_next_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_NEXT_BUTTON).click()

    @allure.step('Выбираем станцию из списка по индексу {index}')
    def select_station(self, index):
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

    @allure.step('Проверяем название выбранной станции')
    def check_station(self):
        #station_name = self.driver.find_element(*locators.ORDER_PAGE_STATION_VALUE).get_attribute("value")
        station_name = self.get_value(locators.ORDER_PAGE_STATION_VALUE)
        return station_name

    #
    # функции для работы со 2-й страницей оформления заказа
    @allure.step('Ждем загрузку 2-й страницы заказа - появления кнопки "Назад"')
    def wait_for_load_back_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_BACK_BUTTON))

    @allure.step('Вводим значение в поле по его локатору: {locator}')
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Получаем значение поля по локатору: {locator}')
    def get_value(self, locator):
        value = self.driver.find_element(*locator).get_attribute("value")
        return value

    @allure.step('Получаем текст в поле по локатору: {locator}')
    def get_text(self, locator):
        value = self.driver.find_element(*locator).text
        return value

    @allure.step('Ждем появление элемента в DOM по локатору: {locator}')
    def wait_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(locator))

    @allure.step('Ждем появления видимого элемента по локатору {locator}')
    def wait_visible_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Находим и проверяем элемент страницы по локатору {locator}')
    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Находим и кликаем элемент в DOM по локатору {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем элемент DOM')
    def click_page_element(self, element):
        element.click()

    @allure.step('Выбираем дату доставки в поле "Когда привезти самокат?"')
    def select_delivery_date(self, delivery_date=None):
        if delivery_date:
            # если дата указана, вводим ее в поле
            self.set_value(locators.ORDER_PAGE_DATE_DELIVERY_FIELD, delivery_date)

        # если дата не указана, то кликаем на поле даты, чтобы открылся календарь с текущей датой
        self.driver.find_element(*locators.ORDER_PAGE_DATE_DELIVERY_FIELD).click()

        # ждем загрузки элементов календаря - неделя и день
        self.wait_element(locators.ORDER_PAGE_WEEK_ELEMENT)
        self.wait_element(locators.ORDER_PAGE_DAY_ELEMENT)

        # ищем выбранный день в календаре и кликаем по нему
        element = self.driver.find_element(*locators.ORDER_PAGE_DAY_ELEMENT)
        if data._debug:
            print(f'element = {element}')
        element.click()

    @allure.step('Выбираем срок аренды (index 0-6: {index})')
    def select_rent_time(self, index=0):
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


