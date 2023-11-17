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

    #def set_metro_field_value(self, value):
        #field = self.driver.find_element(*locators.ORDER_PAGE_INPUT_METRO_FIELD)
        #select = Select(self.driver.find_element(By.CLASS_NAME, "select-search"))
        #if data._debug:
        #    old_value = field.get_attribute("value")
        #    print(f'field.value = "{old_value}"')
        #field.send_keys("Сокольники")
        #select.select_by_visible_text("Сокольники")
        #select.select_by_value('1')
        #if data._debug:
        #    new_value = field.get_attribute("value")
        #    print(f'field.value = "{new_value}"')
        #field.click()
        #if data._debug:
        #    new_value = field.get_attribute("value")
        #    print(f'field.value = "{new_value}"')
        #    time.sleep(5)

    def select_station(self, index):
        # кликаем поле выбора станции
        #self.driver.find_element(*locators.ORDER_PAGE_STATION_FIELD).click()
        self.driver.find_element(By.XPATH, ".//div[@class='select-search']").click()


        if data._debug: time.sleep(3)
        # ждем отображения нужной станции в выпадающем списке
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//div[@class='select-search__select']")))

        if data._debug: time.sleep(3)
        # кликаем станцию
        self.driver.find_element(*locators.ORDER_PAGE_STATION_BUTTON).click()

        if data._debug: time.sleep(3)
        #
        WebDriverWait(self.driver, 3).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                locators.ORDER_PAGE_STATION_VALUE, "value", "Сокольники"))
        if data._debug:
            value = self.driver.find_element(*locators.ORDER_PAGE_STATION_VALUE).get_attribute("value")
            print(f'field.value = "{value}"')
            time.sleep(5)

    def get_input_fields(self):
        return self.driver.find_elements(*locators.ORDER_PAGE_INPUT_FIELDS)

    def set_field_value(self, input_field, value):
        input_field.send_keys(value)

    #def wait_for_next_button(self):
    #    WebDriverWait(self.driver, 5).until(
    #        expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_NEXT_BUTTON))

    def click_next_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_NEXT_BUTTON).click()
