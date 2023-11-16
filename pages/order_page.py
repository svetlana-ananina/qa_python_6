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

    #def wait_for_open_order_page(self):
    #    WebDriverWait(self.driver, 10).until(
    #        expected_conditions.url_to_be(data.URLS.ORDER_PAGE_URL))

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.ORDER_PAGE_ORDER_BUTTON))

