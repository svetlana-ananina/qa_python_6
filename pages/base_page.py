from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import allure

#import locators
#import data
from locators import BasePageLocators as base_page_locators
from data import URLS as urls


class BasePage:
    """ Базовый класс для классов страниц - Главной страницы и страницы заказа """

    def __init__(self, new_driver, new_page_url):
        self.driver = new_driver
        self.page_url = new_page_url

    @allure.step('Открываем страницу по URL {self.page_url}')
    def open_page(self):
        self.driver.get(self.page_url)

    @allure.step('Ждем открытие страницы при переходе по ссылке: {self.page_url}')
    def wait_for_open_page(self):
        return WebDriverWait(self.driver, 10).until(
                    expected_conditions.url_to_be(self.page_url))

    @allure.step('Кликаем согласие с куки')
    def click_accept_cookies_button(self):
        self.driver.find_element(*base_page_locators.COOKIE_BUTTON).click()

    #def wait_visible_element(self, locator):
    @allure.step('Ждем загрузку элемента по локатору {locator}')
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ждем загрузку всех элементов по локатору {locator}')
    def wait_for_load_all_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    #def wait_element(self, locator):
    @allure.step('Ждем появление в DOM элемента по локатору {locator}')
    def wait_for_presence_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))

    #def get_element(self, locator):
    @allure.step('Ищем элемент по локатору {locator}')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ищем все элементы по локатору {locator}')
    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Кликаем элемент по локатору {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    # ???
    @allure.step('Кликаем элемент DOM')
    def click_page_element(self, element):
        element.click()

    @allure.step('Прокручиваем страницу до элемента по локатору {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        #if len(self.driver.window_handles) > 1:
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ждем загрузку в новой вкладке Дзен через редирект')
    def wait_for_new_window(self, new_url=urls.DZEN_URL):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(urls.BLANK_URL))
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(new_url))

    @allure.step('Вводим данные в поле по элементу DOM')
    def set_field_value(self, element, value):
        element.send_keys(value)

    @allure.step('Получаем значение из поля по элементу DOM')
    def check_field_value(self, element):
        return element.get_attribute("value")

    # get_value()
    @allure.step('Получаем значение поля по локатору: {locator}')
    def check_value(self, locator):
        return self.driver.find_element(*locator).get_attribute("value")

    @allure.step('Вводим значение в поле по его локатору: {locator}')
    def set_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    # get_text()
    @allure.step('Получаем текст в поле по локатору: {locator}')
    def check_text(self, locator):
        return self.driver.find_element(*locator).text


