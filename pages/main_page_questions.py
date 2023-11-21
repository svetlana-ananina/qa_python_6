from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import allure

import locators
import data


class MainPageQuestions:
    """ Класс Главной страницы """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        self.driver.get(data.URLS.MAIN_PAGE_URL)

    @allure.step('Ждем открытие Главной страницы при переходе по ссылке')
    def wait_for_open_main_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(data.URLS.MAIN_PAGE_URL))

    @allure.step('Ждем загрузку Главной страницы')
    def wait_for_load_main_page(self):
        """ Ожидание загрузки страницы: ожидаем появление блока 'Вопросы о важном' """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_FAQ_LIST))

    @allure.step('Кликаем согласие с куки')
    def click_accept_cookies_button(self):
        cookie_button = self.driver.find_element(*locators.BASE_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    # Методы для поддержки работы с кнопками "Заказать" и страницей заказа
    @allure.step('Прокручиваем страницу до кнопки "Заказать"')
    def scroll_to_order_button(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ждем загрузку кнопки Заказать')
    def wait_for_load_order_button(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликаем кнопку "Заказать"')
    def click_order_button(self, locator):
        self.driver.find_element(*locator).click()

    # Методы для работы с блоком "Вопросы о важном"
    # Прокрутка до блока вопросов
    @allure.step('Прокручиваем страницу до списка вопросов')
    def scroll_to_faq_list(self):
        element = self.driver.find_element(*locators.MAIN_PAGE_FAQ_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ищем на странице элемент для вопроса с номером {index}')
    def get_questions_item(self, index):
        return (self.driver.find_elements(*locators.MAIN_PAGE_FAQ_BUTTONS))[index]

    @allure.step('Ищем на странице элемент для ответа с номером {index}')
    def get_answers_item(self, index):
        return (self.driver.find_elements(*locators.MAIN_PAGE_FAQ_ITEMS))[index]

    @allure.step('Ждем загрузку списка вопросов')
    def wait_for_load_questions_list(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(locators.MAIN_PAGE_FAQ_LIST))

    @allure.step('Ждем загрузку ответа с номером {index}')
    def wait_for_load_answer(self, index):
        xpath = locators.MAIN_PAGE_FAQ_ITEM_XPATH.format(index+1)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

