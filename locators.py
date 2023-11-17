from selenium.webdriver.common.by import By


MAIN_PAGE_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
BASE_PAGE_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]

MAIN_PAGE_FAQ_LIST = [By.CLASS_NAME, "accordion"]
MAIN_PAGE_FAQ_BUTTONS = [By.CLASS_NAME, "accordion__button"]
MAIN_PAGE_FAQ_ITEMS = [By.XPATH, ".//div[@class='accordion__panel']/p"]
MAIN_PAGE_FAQ_ITEM_XPATH = "(.//div[@class='accordion__panel'])[{}]"
# $x("(.//div[@class='accordion__panel'])[8]")
# xpath = f"(.//div[@class='accordion__panel'])[{index+1}]"

# $x(".//button[text()='Заказать']")
# $x("(.//button[text()='Заказать'])[2]")
# $x("(.//button[text()='Заказать'])[1]")
MAIN_PAGE_ORDER_BUTTONS = [By.XPATH, ".//button[text()='Заказать']"]
MAIN_PAGE_HEADER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[1]"]
MAIN_PAGE_FOOTER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]

ORDER_PAGE_SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
ORDER_PAGE_LOGO_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]

ORDER_PAGE_NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
ORDER_PAGE_INPUT_FIELDS = [By.TAG_NAME, "input"]

ORDER_PAGE_STATION_FIELD = [By.XPATH, ".//div[@class='select-search']"]
ORDER_PAGE_STATION_LIST = [By.XPATH, ".//div[@class='select-search__select']"]
ORDER_PAGE_STATION_BUTTON = [By.XPATH, ".//ul/li/button[@value='4']"]
ORDER_PAGE_STATION_VALUE = [By.XPATH, ".//div[@class='select-search__value']/input"]

