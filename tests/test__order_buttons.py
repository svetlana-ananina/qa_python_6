from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.firefox

import pytest
import allure
import time

from pages.base_page import BasePage
from data import URLS as urls
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
        # Открываем Главную страницу
        driver = setup_driver
        base_page = BasePage(driver)
        base_page.open_page(urls.MAIN_PAGE_URL)

        # ждем загрузку на Главной странице кнопки "Заказать"
        base_page.wait_for_load_element(locator)

        # кликаем согласие с куки
        base_page.click_accept_cookies_button()

        # прокручиваем страницу до кнопки "Заказать"
        base_page.scroll_to_element(locator)

        # ждем загрузку кнопки Заказать
        base_page.wait_for_load_element(locator)

        # кликаем кнопку Заказать
        base_page.click_element(locator)

        # проверяем, что открылся URL страницы заказа
        assert driver.current_url == urls.ORDER_PAGE_URL

    @allure.title('Проверка клика по логотипу Самокат на странице заказа')
    @allure.description('На странице заказа ищем кнопку "Самокат" и проверяем, что по клику открывается Главная страница')
    def test_order_page_scooter_button(self, setup_driver):
        """ Проверяем кнопку Самокат в хедере страницы заказа """
        # открываем страницу заказа по URL
        driver = setup_driver
        base_page = BasePage(driver)
        base_page.open_page(urls.ORDER_PAGE_URL)

        # ждем загрузки страницы заказа
        base_page.wait_for_load_element(oploc.NEXT_BUTTON)

        # кликаем согласие с куки
        base_page.click_accept_cookies_button()

        # кликаем кнопку Самокат
        base_page.click_element(bploc.SCOOTER_BUTTON)

        # проверяем, что открылся URL Главной страницы
        assert driver.current_url == urls.MAIN_PAGE_URL

    @allure.title('Проверка клика по логотипу Яндекса на странице заказа')
    @allure.description('На странице заказа ищем кнопку "Яндекс" и проверяем, '
                        'что по клику в новом окне через редирект открывается главная страница Дзен')
    def test_order_page_logo_button(self, setup_driver):
        """ Проверяем кнопку Яндекс в хедере страницы заказа """
        # открываем страницу заказа по URL
        driver = setup_driver
        base_page = BasePage(driver)
        base_page.open_page(urls.ORDER_PAGE_URL)

        # ждем загрузки страницы заказа
        base_page.wait_for_load_element(oploc.NEXT_BUTTON)

        # кликаем согласие с куки
        base_page.click_accept_cookies_button()

        # кликаем кнопку Яндекс
        base_page.click_element(bploc.LOGO_BUTTON)

        # Проверяем что открылась новая вкладка
        assert len(driver.window_handles) > 1

        # переключаемся на новую вкладку
        base_page.switch_to_new_window()

        # ждем загрузку в новой вкладке главной страницы Дзен через редирект
        base_page.wait_for_new_window(urls.DZEN_URL)

        # проверяем что открылась главная страница Дзен через редирект
        assert driver.current_url == urls.DZEN_URL

