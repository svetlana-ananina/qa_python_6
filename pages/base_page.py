from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import allure

from locators import BasePageLocators as base_page_locators
from data import URLS as urls


class BasePage:
    """ Базовый класс для классов страниц - Главной страницы и страницы заказа """

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        """ Открываем страницу по URL {page_url} """
        self.driver.get(page_url)

    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_open_page(self, page_url):
        """ Ждем открытие страницы при переходе по ссылке: {self.page_url} """
        return WebDriverWait(self.driver, 10).until(
                    expected_conditions.url_to_be(page_url))

    def wait_for_load_all_elements(self, locator):
        """ Ждем загрузку всех элементов HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    def wait_for_presence_of_element(self, locator):
        """ Ждем появление в DOM элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))

    def find_element(self, locator):
        """ Ищем элемент HTML по локатору {locator} """
        return self.driver.find_element(*locator)

    def find_all_elements(self, locator):
        """ Ищем все элементы HTML по локатору {locator} """
        return self.driver.find_elements(*locator)

    @allure.step('Кликаем элемент HTML по локатору {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем согласие с куки')
    def click_accept_cookies_button(self):
        self.driver.find_element(*base_page_locators.COOKIE_BUTTON).click()

    @allure.step('Прокручиваем страницу до элемента по локатору {locator}')
    def scroll_to_element(self, locator):
        """ Прокручиваем страницу до элемента по локатору {locator} """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        """ Переключаемся на новую вкладку """
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ждем загрузку в новой вкладке главной страницы Дзен через редирект')
    def wait_for_new_window(self, new_url=urls.DZEN_URL):
        """ Ждем загрузку в новой вкладке главной страницы Дзен через редирект """
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(urls.BLANK_URL))
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(new_url))

    def set_value(self, locator, value):
        """ Вводим текст в поле по локатору: {locator} """
        self.driver.find_element(*locator).send_keys(value)

    def check_value(self, locator):
        """ Получаем значение поля по локатору: {locator} """
        return self.driver.find_element(*locator).get_attribute("value")

    def check_text(self, locator):
        """ Получаем текст в поле по локатору: {locator} """
        return self.driver.find_element(*locator).text


