from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.firefox

import pytest
import allure
import time

from pages.base_page import BasePage
from pages.main_page_questions import MainPageQuestions
from data import MainPageData as dat
from data import URLS as urls


class TestMainPageQuestions:

    driver = None
    #main_page = None

    @allure.step('Открываем браузер Firefox')
    @pytest.fixture()
    def setup_driver(self):
        # создали драйвер для браузера Chrome
        self.driver = webdriver.Firefox()

        # создаем объект класса Главная страница с разделом 'Вопросы о важном'
        main_page = MainPageQuestions(self.driver)
        #self.main_page = MainPageQuestions(self.driver, urls.MAIN_PAGE_URL)
        #main_page = MainPageQuestions(self.driver, urls.MAIN_PAGE_URL)

        return main_page
        #yield self.main_page
        #yield main_page
        #yield
        # закрываем драйвер после использования
        #self.driver.quit()

    @allure.title('Проверка вопросов и ответов на Главной странице')
    @allure.description('На Главной странице ищем вопросы и проверяем, что по клику открывается соответствующий ответ')
    @pytest.mark.parametrize('index', [0])      # @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_answers(self, setup_driver, index):
        """ Проверяем список вопросов и ответов на Главной странице
            Параметризованный тест для проверки 8-ми вопросов и ответов в блоке 'Вопросы о важном'
        """
        # Открываем Главную страницу
        #self.main_page.open_main_page()
        main_page = setup_driver
        #self.main_page.open_page()
        main_page.open_page()

        # ждем загрузки главной страницы
        #self.main_page.wait_for_load_main_page()
        main_page.wait_for_load_main_page()

        # кликаем согласие с куки
        #self.main_page.click_accept_cookies_button()
        main_page.click_accept_cookies_button()

        # прокручиваем страницу до
        #self.main_page.scroll_to_faq_list()
        main_page.scroll_to_faq_list()

        # ждем появления списка вопросов
        #self.main_page.wait_for_load_questions_list()
        main_page.wait_for_load_questions_list()

        # получаем элемент списка вопросов с индексом 'index'
        #questions_item = self.main_page.get_questions_item(index)
        questions_item = main_page.get_questions_item(index)

        # кликаем вопрос
        questions_item.click()

        #self.main_page.wait_for_load_answer(index)
        main_page.wait_for_load_answer(index)

        # получаем соответствующий ответ с тем же индексом
        #answers_item = self.main_page.get_answers_item(index)
        answers_item = main_page.get_answers_item(index)

        # проверяем, что текст вопроса соответствует ожидаемому
        question_expected = dat.QUESTIONS_TEXT[index]
        question_received = questions_item.text
        assert question_received == question_expected

        # проверяем, что текст вопроса соответствует ожидаемому
        answer_expected = dat.ANSWERS_TEXT[index]
        answer_received = answers_item.text
        assert answer_received == answer_expected

        # проверяем, что ответ появился на экране
        is_displayed = answers_item.is_displayed()
        assert is_displayed

        #yield
        # закрываем драйвер после использования
        self.driver.quit()

