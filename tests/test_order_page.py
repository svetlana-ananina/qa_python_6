from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.firefox

import pytest
import allure
import time

from pages.main_page_questions import MainPageQuestions
from pages.order_page import OrderPage
import data
import locators


class TestOrderPage:

    driver = None
    main_page = None
    order_page = None


    @allure.step('Открываем браузер Firefox')
    @pytest.fixture()
    def setup_driver(self):
        # создали драйвер для браузера Firefox
        self.driver = webdriver.Firefox()

        # создаем объект класса Главная страница
        self.main_page = MainPageQuestions(self.driver)

        # создаем объект класса страница заказа
        self.order_page = OrderPage(self.driver)

        yield

        # закрываем драйвер
        self.driver.quit()


    @allure.title('Проверка двух кнопок "Заказать" на Главной странице')
    @allure.description('На Главной странице ищем кнопку "Заказать" и проверяем, что по клику открывается страница заказа')
    @pytest.mark.parametrize('locator', [locators.MAIN_PAGE_HEADER_ORDER_BUTTON,
                                         locators.MAIN_PAGE_FOOTER_ORDER_BUTTON])
    def test_main_page_order_button(self, setup_driver, locator):
        """ Проверяем кнопки 'Заказать' на Главной странице
            Параметризованный тест для проверки двух кнопок 'Заказать':
            - в хедере Главной страницы
            - внизу Главной страницы
        """
        # открываем Главную страницу
        self.main_page.open_main_page()

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # кликаем согласие с куками
        self.main_page.click_accept_cookies_button()

        # прокручиваем страницу до кнопки Заказать
        self.main_page.scroll_to_order_button(locator)

        # загрузку кнопки Заказать
        self.main_page.wait_for_load_order_button(locator)

        # кликаем кнопку Заказать
        self.main_page.click_order_button(locator)

        # ждем перехода на страницу заказа
        self.order_page.wait_for_open_order_page()

        # проверяем, что открылся URL страницы заказа
        assert self.driver.current_url == data.URLS.ORDER_PAGE_URL


    @allure.title('Проверка клика по логотипу Самокат на странице заказа')
    @allure.description('На странице заказа ищем кнопку "Самокат" и проверяем, что по клику открывается Главная страница')
    def test_order_page_scooter_button(self, setup_driver):
        """ Проверяем кнопку Самокат в хедере страницы заказа """
        # открываем страницу заказа по URL
        self.order_page.open_order_page()

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        # кликаем кнопку Самокат
        self.order_page.click_scooter_button()

        # ждем загрузки главной страницы
        self.main_page.wait_for_open_main_page()

        # ждем загрузки главной страницы
        self.main_page.wait_for_load_main_page()

        # проверяем, что открылся URL Главной страницы
        assert self.driver.current_url == data.URLS.MAIN_PAGE_URL


    @allure.title('Проверка клика по логотипу Яндекса на странице заказа')
    @allure.description('На странице заказа ищем кнопку "Яндекс" и проверяем, '
                        'что по клику в новом окне через редирект открывается главная страница Дзена')
    def test_order_page_logo_button(self, setup_driver):
        """ Проверяем кнопку Яндекс в хедере страницы заказа """
        # открываем страницу заказа по URL
        self.order_page.open_order_page()

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        # кликаем кнопку Яндекс
        self.order_page.click_logo_button()

        # Проверяем что открылась новая вкладка
        assert len(self.driver.window_handles) > 1

        # переключаемся на новую вкладку
        self.order_page.switch_to_new_window()

        # ждем загрузки на новой вкладке страницы Яндекс Дзен редирект
        self.order_page.wait_for_new_window()

        assert self.driver.current_url == data.URLS.DZEN_URL


    @allure.title('Проверка позитивного сценария оформления заказа с 2мя наборами данных')
    @allure.description('Нажать кнопку заказать на Главной странице, заполнить форму заказа и проверить, '
                        'что появилось всплывающее окно с сообщением об успешном оформлении заказа')
    @pytest.mark.parametrize('user_info, order_info',
                             [[data.DATA.USER_INFO_1, data.DATA.ORDER_INF0_1],
                              [data.DATA.USER_INFO_2, data.DATA.ORDER_INF0_2]])
    def test_order_page_order_placement(self, setup_driver, user_info, order_info):
        """ Проверяем позитивный сценарий всего процесса оформление заказа.
            Параметризованный тест для проверки двух наборов данных. Пример данных клиента и заказа:
            USER_INFO_1 = [
                    'Иван',
                    'Иванов',
                    'Москва, Русаковская улица, 22',
                    'Сокольники',
                    '+79999999999',
                    4                       # индекс станции Сокольники в списке
            ]

            ORDER_INF0_1 = [
                    '01.12.2023',           # Когда привезти самокат
                    0,                      # Срок аренды - 1 сутки (индекс от 0 до 6)
                    True,                   # Выбрать 1-й цвет
                    True,                   # Выбрать 2-й цвет
                    "Позвоните за полчаса", # Комментарий для курьера
                    "сутки"                 # Текст в поле срок аренды после выбора
            ]
        """
        # Получаем данные пользователя из user_info
        user_first_name = user_info[0]
        user_last_name = user_info[1]
        user_address = user_info[2]
        user_station_name = user_info[3]
        user_telephone = user_info[4]
        user_station_index = user_info[5]

        # открываем страницу заказа по URL
        self.order_page.open_order_page()

        # ждем загрузки страницы заказа
        self.order_page.wait_for_load_order_page()

        # кликаем согласие с куки
        self.order_page.click_accept_cookies_button()

        # получаем список полей ввода: 6 (индексы 0-5)
        #   0 - статус заказа (не используется в тесте)
        #   1 - имя пользователя
        #   2 - фамилия пользователя
        #   3 - адрес доставки
        #   4 - станция метро (селектор - выбор из выпадающего списка)
        #   5 - телефон
        input_fields = self.order_page.get_input_fields()

        # Проверяем, что на странице 6 полей ввода (1-е поле - статус заказа)
        assert len(input_fields) == 6

        # заполняем текстовые поля ввода input, кроме станции метро (индексы 1, 2, 3, 5)
        # информацией из набора данных пользователя
        #for i in {0, 1, 2, 4}:
        self.order_page.set_field_value(input_fields[1], user_first_name)
        self.order_page.set_field_value(input_fields[2], user_last_name)
        self.order_page.set_field_value(input_fields[3], user_address)
        self.order_page.set_field_value(input_fields[5], user_telephone)

        # выбираем станцию метро из списка по индексу
        self.order_page.select_station(user_station_index)

        # проверяем введенные данные в полях
        selected_station = self.order_page.check_station()

        # Проверяем, что в полях введены данные пользователя
        assert self.order_page.check_field_value(input_fields[1]) == user_first_name
        assert self.order_page.check_field_value(input_fields[2]) == user_last_name
        assert self.order_page.check_field_value(input_fields[3]) == user_address
        assert self.order_page.check_field_value(input_fields[5]) == user_telephone

        # проверяем чтобы выбранная станция появилась в поле
        assert selected_station == user_station_name

        # кликаем кнопку Дальше
        self.order_page.click_next_button()

        # ждем перехода на 2-ю страницу - загрузку кнопки "Назад"
        self.order_page.wait_for_load_back_button()

        # получаем список полей ввода input: 5 (индексы 0-4)
        #   0 - статус заказа (не используется в тесте)
        #   1 - дата доставки
        #   2, 3 - цвет самоката
        #   4 - комментарий для курьера
        input_fields = self.order_page.get_input_fields()

        # Проверяем, что на странице 5 полей ввода (1-е поле - статус заказа)
        assert len(input_fields) == 5

        # Получаем данные заказа из order_info
        order_delivery_date = order_info[0]
        order_rent_time = order_info[1]
        order_select_black_color = order_info[2]
        order_select_grey_color = order_info[3]
        order_comment = order_info[4]
        order_rent_time_text = order_info[5]

        # Выбираем дату в поле 'Когда привезти самокат'
        self.order_page.select_delivery_date(order_delivery_date)

        # выбираем срок аренды по индексу (от 0 до 6 - 1-7 суток)
        self.order_page.select_rent_time(order_rent_time)

        # Выбираем цвет самоката (поля ввода с индексами 2 и 3)
        if order_select_black_color:   # выбираем цвет 'Черный жемчуг'
            self.order_page.click_element(locators.ORDER_PAGE_COLOR_BLACK_FIELD)
        if order_select_grey_color:   # выбираем цвет 'Серая безысходность'
            self.order_page.click_element(locators.ORDER_PAGE_COLOR_GREY_FIELD)

        # Вводим комментарий для курьера (поле ввода с индексом 4)
        if order_comment:
            self.order_page.set_value(locators.ORDER_PAGE_COMMENT_FIELD, order_comment)

        # Получаем введенные данные в полях и проверяем, что они соответствуют данным заказа
        selected_delivery_date = self.order_page.get_value(locators.ORDER_PAGE_DATE_DELIVERY_FIELD)
        selected_rent_time = self.order_page.get_text(locators.ORDER_PAGE_RENT_TIME_VALUE)
        selected_comment = self.order_page.get_value(locators.ORDER_PAGE_COMMENT_FIELD)

        # Проверяем, что дата выбрана и совпадает с указанной в данных заказа
        assert selected_delivery_date
        if order_delivery_date:
            assert selected_delivery_date == order_delivery_date

        # Проверяем, что выбранный срок аренды совпадает с указанным в данных заказа
        assert selected_rent_time == order_rent_time_text
        # Проверяем, что введенный комментарий совпадает с указанным в данных заказа
        assert selected_comment == order_comment

        # Кликаем кнопку "Заказать" внизу страницы
        self.order_page.click_element(locators.ORDER_PAGE_ORDER_BUTTON)

        # ждем появления окна "Хотите оформить заказ?" с кнопкой "Да"
        self.order_page.wait_visible_element(locators.ORDER_PAGE_YES_BUTTON)

        # кликаем кнопку Да
        self.order_page.click_element(locators.ORDER_PAGE_YES_BUTTON)

        # ждем всплывающее окно с кнопкой "Посмотреть статус"
        self.order_page.wait_visible_element(locators.ORDER_PAGE_ORDER_ACCEPTED_BUTTON)
        # проверяем заголовок всплывающего окна "Заказ оформлен"

        assert self.order_page.get_element(locators.ORDER_PAGE_ORDER_ACCEPTED_TITLE)

