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
        self.driver.get(data.URLS.ORDER_PAGE_URL)

    def wait_for_open_order_page(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(data.URLS.ORDER_PAGE_URL))

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_NEXT_BUTTON))

    # Кликнуть согласие с куками
    def click_accept_cookies_button(self):
        cookie_button = self.driver.find_element(*locators.BASE_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    def wait_for_scooter_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_SCOOTER_BUTTON))

    def click_scooter_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_SCOOTER_BUTTON).click()

    def wait_for_logo_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_LOGO_BUTTON))

    def click_logo_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_LOGO_BUTTON).click()

    def switch_to_new_window(self):
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_new_window(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(data.URLS.BLANK_URL))
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(data.URLS.DZEN_URL))

    ################################
    def select_station(self, index):
        """ Выбор станции из выпадающего списка по индексу, название станции для проверки """
        if data._debug: print(f'index = {index}')

        # кликаем поле выбора станции
        self.driver.find_element(*locators.ORDER_PAGE_STATION_FIELD).click()
        #self.driver.find_element(By.XPATH, ".//div[@class='select-search']").click()


        if data._debug: time.sleep(3)
        # ждем появления выпадающего списка станций
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                locators.ORDER_PAGE_SELECT_STATION_LIST))
                #(By.XPATH, ".//div[@class='select-search__select']")))

        # кликаем станцию в списке
        #self.driver.find_element(By.XPATH, ".//ul/li/button[@value='4']").click()
        station_xpath = locators.ORDER_PAGE_SELECT_STATION_XPATH.format(index)
        if data._debug: print(f'station_xpath = "{station_xpath}"')
        #station_locator = [By.XPATH, station_xpath]
        self.driver.find_element(By.XPATH, station_xpath).click()


        if data._debug: time.sleep(3)
        # ждем чтобы выбранная станция появилась в поле
        #WebDriverWait(self.driver, 3).until(
        #    expected_conditions.text_to_be_present_in_element_attribute(
        #        locators.ORDER_PAGE_STATION_VALUE, "value", "Сокольники"))
        if data._debug:
            value = self.driver.find_element(*locators.ORDER_PAGE_STATION_VALUE).get_attribute("value")
            print(f'field.value = "{value}"')
            time.sleep(5)

    # получить список из элементов по локатору (поля ввода с тегом input)
    def get_input_fields(self):
        return self.driver.find_elements(*locators.ORDER_PAGE_INPUT_FIELDS)

    # ввести значение в поле по элементу DOM
    def set_field_value(self, input_field, value):
        input_field.send_keys(value)

    def click_next_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_NEXT_BUTTON).click()

    # функции для работы со 2-й страницей оформления заказа
    def wait_for_load_back_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_BACK_BUTTON))

    # Ввести значение в поле по локатору
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)


    # получить значение поля по локатору
    def get_field_value(self, locator):
        value = self.driver.find_element(*locator).get_attribute("value")
        #if data._debug:
        #    print(f'field.value = "{value}"')
        return value


    def select_rent_time(self, index):
        # кликаем поле выбора срока аренды, индекс 1-7
        self.driver.find_element(*locators.ORDER_PAGE_RENT_TIME).click()

        # ждем появления выпадающего списка
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(
                locators.ORDER_PAGE_RENT_TIME_LIST))

        # кликаем элемент списка по индексу
        #ORDER_PAGE_RENT_TIME_ITEM = [By.XPATH, "(.//div[@class='Dropdown-option'])[1]"]
        rent_time_xpath = locators.ORDER_PAGE_RENT_TIME_ITEM.format(index)
        if data._debug: print(f'station_xpath = "{rent_time_xpath}"')
        self.driver.find_element(By.XPATH,rent_time_xpath).click()


