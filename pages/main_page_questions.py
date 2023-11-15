from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest
import locators
import data


# класс главной страницы
class MainPageQuestions:
    # создай локатор для поля «Занятие» в профиле пользователя

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания загрузки страницы
    # ожидаем появление поля «Занятие»
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_FAQ_LIST))

    def scroll_to_faq_list(self):
        element = self.driver.find_element(*locators.MAIN_PAGE_FAQ_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_accept_cookies_buttons(self):
        cookie_button = self.driver.find_element(*locators.MAIN_PAGE_COOKIE_BUTTON)
        if cookie_button:
            cookie_button.click()

    def get_questions_item(self, index):
        return (self.driver.find_elements(*locators.MAIN_PAGE_FAQ_BUTTONS))[index]

    def get_answers_item(self, index):
        return (self.driver.find_elements(*locators.MAIN_PAGE_FAQ_ITEMS))[index]

    def wait_for_load_answer(self, index):
        # $x("(.//div[@class='accordion__panel'])[8]")
        xpath = f"(.//div[@class='accordion__panel'])[{index+1}]"
        if data._debug:
            print(f'XPATH = "{xpath}"')
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

