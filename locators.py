from selenium.webdriver.common.by import By


MAIN_PAGE_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
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

ORDER_PAGE_ORDER_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
ORDER_PAGE_SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
ORDER_PAGE_LOGO_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]

