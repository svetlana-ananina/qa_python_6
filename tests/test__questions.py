from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.firefox

import pytest
import allure
import time

from pages.base_page import BasePage
from pages.main_page import MainPage
from data import MainPageData as mpdat
from data import URLS as urls
from locators import BasePageLocators as bploc
from locators import MainPageLocators as mploc


class TestMainPageQuestions:

    @allure.title('Проверка вопросов и ответов на Главной странице')
    @allure.description('На Главной странице ищем вопрос и проверяем, что по клику открывается соответствующий ответ')
    @pytest.mark.parametrize('index, question, answer', mpdat.QUESTIONS_AND_ANSWERS_LIST)
    def test_faq_questions_and_answers(self, setup_driver, index, question, answer):
        """ Проверяем список вопросов и ответов на Главной странице
            Параметризованный тест для проверки 8-ми вопросов и ответов в блоке 'Вопросы о важном'
        """
        # Открываем окно веб-браузера и инициализируем класс POM для Главной страницы
        driver = setup_driver
        main_page = MainPage(driver)

        # Открываем Главную страницу
        main_page.open_main_page()

        # прокручиваем страницу до списка вопросов
        main_page.scroll_to_element(mploc.FAQ_LIST)

        # ждем появления списка вопросов
        main_page.wait_for_load_all_elements(mploc.FAQ_LIST)

        # кликаем вопрос с номером 'index'
        question_received = main_page.click_on_question(index)
        # получаем соответствующий ответ
        answer_received = main_page.get_answer(index)

        # проверяем, что текст вопроса соответствует ожидаемому
        assert question_received == question

        # проверяем, что текст вопроса соответствует ожидаемому
        assert answer_received == answer

