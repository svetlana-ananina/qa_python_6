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
from pages.order_page import OrderPage
from data import URLS as urls
from data import OrderPageData as opdat
from data import MainPageData as mpdat
from locators import MainPageLocators as mploc
from locators import OrderPageLocators as oploc
from locators import BasePageLocators as bploc


class TestOrderButtons:

    @allure.title('Проверка клика по двум кнопкам "Заказать на Главной странице')
    @allure.description('Проверяем, что при клике по кнопке Заказать на Главной странице'
                        'открывается страница заказа')
    @pytest.mark.parametrize('locator', [mploc.HEADER_ORDER_BUTTON, mploc.FOOTER_ORDER_BUTTON])
    def test_order_button(self, setup_driver, locator):
        """ Проверка клика по кнопке Заказать на Главной странице.
            Параметризованный тест для двух кнопок Заказать: в хедере и внизу Главной страницы.
        """
        # Открываем окно веб-браузера и инициализируем класс POM для Главной страницы
        driver = setup_driver
        main_page = MainPage(driver)

        # Открываем Главную страницу
        main_page.open_main_page()

        # прокручиваем страницу до кнопки "Заказать"
        main_page.scroll_to_element(locator)

        # ждем загрузку кнопки Заказать
        main_page.wait_for_load_element(locator)

        # кликаем кнопку Заказать
        main_page.click_element(locator)

        # ждем что открылось страница оформления заказа с формой "Для кого самокат"
        main_page.wait_for_load_element(oploc.FORM1_TITLE)

        # проверяем заголовок формы: "Для кого самокат"
        assert opdat.FORM1_TITLE_TEXT in main_page.check_text(oploc.FORM1_TITLE)

        # проверяем, что открылся URL страницы заказа
        assert driver.current_url == urls.ORDER_PAGE_URL

    @allure.title('Проверка клика по логотипу Самокат на странице заказа')
    @allure.description('На странице заказа ищем кнопку "Самокат" и проверяем, что по клику открывается Главная страница')
    def test_order_page_scooter_button(self, setup_driver):
        """ Проверяем кнопку Самокат в хедере страницы заказа """
        # Открываем окно веб-браузера и инициализируем класс POM для страницы заказа
        driver = setup_driver
        order_page = OrderPage(driver)

        # Открываем страницу заказа
        order_page.open_order_page()

        # кликаем кнопку Самокат
        order_page.click_element(bploc.SCOOTER_BUTTON)

        # ждем что открылось Главная страница
        order_page.wait_for_load_element(mploc.FAQ_LIST)

        # проверяем заголовок Главной страницы
        assert mpdat.TITLE_TEXT in order_page.check_text(mploc.PAGE_TITLE)

        # проверяем, что открылся URL Главной страницы
        assert driver.current_url == urls.MAIN_PAGE_URL


    @allure.title('Проверка клика по логотипу Яндекса на странице заказа')
    @allure.description('На странице заказа ищем кнопку "Яндекс" и проверяем, '
                        'что по клику в новом окне через редирект открывается главная страница Дзен')
    def test_order_page_logo_button(self, setup_driver):
        """ Проверяем кнопку Яндекс в хедере страницы заказа """
        # Открываем окно веб-браузера и инициализируем класс POM для страницы заказа
        driver = setup_driver
        order_page = OrderPage(driver)

        # Открываем страницу заказа
        order_page.open_order_page()

        # кликаем кнопку Яндекс
        order_page.click_element(bploc.LOGO_BUTTON)

        # Проверяем что открылась новая вкладка
        assert order_page.check_new_window()

        # переключаемся на новую вкладку
        order_page.switch_to_new_window()

        # ждем загрузку в новой вкладке главной страницы Дзен через редирект
        order_page.wait_for_new_window(urls.DZEN_URL)

        # проверяем что открылась главная страница Дзен через редирект
        assert driver.current_url == urls.DZEN_URL

