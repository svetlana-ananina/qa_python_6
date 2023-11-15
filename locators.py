from selenium.webdriver.common.by import By


MAIN_PAGE_COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]
MAIN_PAGE_FAQ_LIST = [By.CLASS_NAME, "accordion"]
MAIN_PAGE_FAQ_BUTTONS = [By.CLASS_NAME, "accordion__button"]
MAIN_PAGE_FAQ_ITEMS = [By.XPATH, ".//div[@class='accordion__panel']/p"]
#MAIN_PAGE_FAQ_ITEMS = [By.XPATH, ".//div[@class='accordion__panel']"]
#MAIN_PAGE_FAQ_ITEM_XPATH = f".//div[@class='accordion__panel'][{index}]"

# text = self.driver.find_element(By.XPATH, ".//div[@class='accordion__item']/div/p").text
# print(f'"{text}"')
# text = self.driver.find_element(By.XPATH, ".//div[@class='accordion__panel']").text
# print(f'"{text}"')
# text = self.driver.find_element(By.XPATH, ".//div[@class='accordion__panel']/p").text
# print(f'"{text}"')

