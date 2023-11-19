from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import locators
import data


# класс главной страницы
class MainPageQuestions:

    def __init__(self, driver):
        self.driver = driver

    # Открыть Главную страницу
    def open_main_page(self):
        self.driver.get(data.URLS.MAIN_PAGE_URL)

    # Ожидание загрузки страницы: ожидаем появление блока вопросов
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_FAQ_LIST))

    # Кликнуть согласие с куками
    def click_accept_cookies_button(self):
        #cookie_button = self.driver.find_element(*locators.MAIN_PAGE_COOKIE_BUTTON)
        cookie_button = self.driver.find_element(*locators.BASE_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    # Методы для работы с блоком "Вопросы о важном"
    # Прокрутка до блока вопросов
    def scroll_to_faq_list(self):
        element = self.driver.find_element(*locators.MAIN_PAGE_FAQ_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_questions_item(self, index):
        return (self.driver.find_elements(*locators.MAIN_PAGE_FAQ_BUTTONS))[index]

    def get_answers_item(self, index):
        return (self.driver.find_elements(*locators.MAIN_PAGE_FAQ_ITEMS))[index]

    def wait_for_load_questions_list(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(locators.MAIN_PAGE_FAQ_LIST))

    def wait_for_load_answer(self, index):
        xpath = locators.MAIN_PAGE_FAQ_ITEM_XPATH.format(index+1)
        if data._debug:
            print(f'XPATH = "{xpath}"')
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    # Методы для работы со страницей заказа
    # методы работы с двумя кнопками Заказать на Главной странице
    def scroll_to_order_button(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_button(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_open_main_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(data.URLS.MAIN_PAGE_URL))

