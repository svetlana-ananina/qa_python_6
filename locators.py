from selenium.webdriver.common.by import By


MAIN_PAGE_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
BASE_PAGE_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]

MAIN_PAGE_FAQ_LIST = [By.CLASS_NAME, "accordion"]
MAIN_PAGE_FAQ_BUTTONS = [By.CLASS_NAME, "accordion__button"]
MAIN_PAGE_FAQ_ITEMS = [By.XPATH, ".//div[@class='accordion__panel']/p"]
MAIN_PAGE_FAQ_ITEM_XPATH = "(.//div[@class='accordion__panel'])[{}]"

MAIN_PAGE_ORDER_BUTTONS = [By.XPATH, ".//button[text()='Заказать']"]
MAIN_PAGE_HEADER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[1]"]
MAIN_PAGE_FOOTER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]

# Страница заказа
# Хедер
ORDER_PAGE_SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
ORDER_PAGE_LOGO_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]

# 1-я страница
ORDER_PAGE_NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
ORDER_PAGE_INPUT_FIELDS = [By.XPATH, ".//input"]
#
ORDER_PAGE_STATION_FIELD = [By.XPATH, ".//div[@class='select-search']"]
ORDER_PAGE_SELECT_STATION_LIST = [By.XPATH, ".//div[@class='select-search__select']"]
#
ORDER_PAGE_SELECT_STATION_XPATH = ".//ul/li/button[@value='{}']"
# Поле с выбранной станции для проверки
ORDER_PAGE_STATION_VALUE = [By.XPATH, ".//div[@class='select-search__value']/input"]

# 2-я страница
ORDER_PAGE_BACK_BUTTON = [By.XPATH, ".//button[text()='Назад']"]

# Выбор даты доставки
ORDER_PAGE_DATE_DELIVERY_FIELD = [By.XPATH, "(.//input)[2]"]
ORDER_PAGE_WEEK_ELEMENT = [By.XPATH, ".//div[@class='react-datepicker__week']"]
ORDER_PAGE_DAY_ELEMENT = [By.CSS_SELECTOR, ".react-datepicker__day[tabindex='0']"]

# Выбор срока аренды
ORDER_PAGE_RENT_TIME_FIELD = [By.XPATH, ".//div[@class='Dropdown-control']"]
ORDER_PAGE_RENT_TIME_LIST = [By.XPATH, ".//div[@class='Dropdown-menu']"]
ORDER_PAGE_RENT_TIME_ITEM = [By.XPATH, ".//div[@class='Dropdown-option']"]

# цвет самоката: 3 и 4 поля ввода
# комментарий для курьера: 5 поле ввода

# кнопка Заказать внизу 2 страницы
ORDER_PAGE_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]

