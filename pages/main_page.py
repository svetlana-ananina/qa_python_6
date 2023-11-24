from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import allure
import time

from pages.base_page import BasePage
from locators import BasePageLocators as base_page_locators
from locators import MainPageLocators as main_page_locators
from data import URLS as urls
from data import MainPageData as mpdat


class MainPage(BasePage):
    """ Класс Главной страницы """

    # Методы для работы с блоком "Вопросы о важном"
    @allure.step('Кликаем вопрос с номером {index} и получаем текст вопроса')
    def click_on_question(self, index):
        method, locator = main_page_locators.FAQ_QUESTION
        locator = locator.format(index)
        # Ждем загрузку вопроса
        self.wait_for_load_element((method, locator))
        # Кликаем вопрос
        question = self.find_element((method, locator))
        question.click()
        return question.text

    @allure.step('Получаем ответ с номером {index}')
    def get_answer(self, index):
        method, locator = main_page_locators.FAQ_ANSWER
        locator = locator.format(index)
        # Ждем загрузку ответа
        self.wait_for_load_element((method, locator))
        return self.find_element((method, locator)).text

