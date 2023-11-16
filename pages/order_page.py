from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import locators
import data


# класс главной страницы
class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    # Открыть Главную страницу
    def open_order_page(self):
        self.driver.get(data.URLS.ORDER_PAGE_URL)

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_ORDER_BUTTON))

    def wait_for_open_order_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(data.URLS.ORDER_PAGE_URL))

    # Кликнуть согласие с куками
    def click_accept_cookies_button(self):
        cookie_button = self.driver.find_element(*locators.BASE_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    def wait_for_scooter_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_SCOOTER_BUTTON))

    def click_scooter_button(self):
        self.driver.find_element(*locators.ORDER_PAGE_SCOOTER_BUTTON).click()

    def wait_for_logo_button(self):
        WebDriverWait(self.driver, 10).until(
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
