from selenium.webdriver.common.by import By


class BasePageLocators:
    # Хедер
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    LOGO_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
    # Куки
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]


class MainPageLocators:

    PAGE_TITLE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
    # Локаторы для работы с блоком вопросов и ответов на Главной странице
    FAQ_LIST = [By.CLASS_NAME, "accordion"]
    FAQ_QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    FAQ_ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]
    # Локаторы для работы со страницей заказа
    HEADER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[1]"]
    FOOTER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]


# Страница заказа
class OrderPageLocators:

    # 1-я страница
    FORM1_TITLE = [By.XPATH, "//div[contains(@class, 'Order_Header')]"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    INPUT_FIELDS = [By.XPATH, "(.//input)[{}]"]
    STATION_FIELD = [By.XPATH, ".//div[@class='select-search']"]
    SELECT_STATION_LIST = [By.XPATH, ".//div[@class='select-search__select']"]
    SELECT_STATION_BUTTON = [By.XPATH, ".//ul/li/button[@value='{}']"]
    # Поле с выбранной станции для проверки:                                    # Атрибут value
    STATION_VALUE = [By.XPATH, ".//div[@class='select-search__value']/input"]
    # 2-я страница
    BACK_BUTTON = [By.XPATH, ".//button[text()='Назад']"]
    # Выбор даты доставки:                                                      # Атрибут value
    DATE_DELIVERY_FIELD = [By.XPATH, ".//div[@class='react-datepicker__input-container']/input"]
    # Элементы в календаре для выбора кликом
    WEEK_ELEMENT = [By.XPATH, ".//div[@class='react-datepicker__week']"]
    DAY_ELEMENT = [By.CSS_SELECTOR, ".react-datepicker__day[tabindex='0']"]
    # Выбор срока аренды
    RENT_TIME_FIELD = [By.XPATH, ".//div[@class='Dropdown-control']"]
    RENT_TIME_LIST = [By.XPATH, ".//div[@class='Dropdown-menu']"]
    RENT_TIME_ITEM = [By.XPATH, "(.//div[@class='Dropdown-option'])[{}]"]
    # Поле с выбранным сроком аренды для проверки:                              # text()
    RENT_TIME_VALUE = [By.XPATH, ".//div[@class='Dropdown-placeholder is-selected']"]
    # цвет самоката: 3 и 4 поля ввода:                                          # text()
    BLACK_COLOR_FIELD = [By.XPATH, "(.//input)[3]"]
    GREY_COLOR_FIELD = [By.XPATH, "(.//input)[4]"]
    # комментарий для курьера (5 поле ввода):                                   # Атрибут value
    COMMENT_FIELD = [By.XPATH, "(.//input)[5]"]
    # кнопка Заказать внизу 2 страницы
    ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]
    # Всплывающее окно подтверждения оформления заказа
    ORDER_CONFIRM = By.XPATH, "//div[text()='Хотите оформить заказ?']"
    # кнопка подтверждения заказа Да
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    # Всплывающее окно "Заказ оформлен"
    ORDER_COMPLETED = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]
    # заголовок всплывающего окна Заказ оформлен и кнопка "Посмотреть статус"

