from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:


    NAME_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Станция метро']"
    )

    PHONE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    DELIVERY_DATE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']"
    )

    RENTAL_PERIOD = (
        By.CSS_SELECTOR,
        ".Dropdown-control"
    )

    BLACK_SCOOTER = (
        By.ID,
        "black"
    )

    GREY_SCOOTER = (
        By.ID,
        "grey"
    )

    COMMENT_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера']"
    )

    BACK_BUTTON = (
        By.XPATH,
        "//button[text()='Назад']"
    )

    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button__ra12g') "
        "and not(contains(@class, 'Button_Middle__1CSJM')) "
        "and text()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button__ra12g') "
        "and contains(@class, 'Button_Middle__1CSJM') "
        "and text()='Заказать']"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    ORDER_STATUS_BUTTON = (
        By.XPATH,
        "//button[text()='Посмотреть статус']"
    )

    def __init__(self, driver):
        self.driver = driver


    def enter_name(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        ).send_keys(name)

    def enter_surname(self, surname):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SURNAME_INPUT)
        ).send_keys(surname)

    def enter_address(self, address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ADDRESS_INPUT)
        ).send_keys(address)

    def enter_metro(self, metro):
        metro_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.METRO_INPUT)
        )

        metro_input.click()
        metro_input.send_keys(metro)

        metro_option = (
            By.XPATH,
            f"//button[contains(@class, 'select-search__option') "
            f"and .//div[normalize-space()='{metro}']]"
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(metro_option)
        ).click()

    def enter_phone(self, phone):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PHONE_INPUT)
        ).send_keys(phone)

    def click_next(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        ).click()

    def click_top_order_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TOP_ORDER_BUTTON)
        ).click()

    def enter_delivery_date(self, date):
        date_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DELIVERY_DATE_INPUT)
        )

        date_input.send_keys(date)

        self.click_top_order_button()

    def select_rental_period(self, period):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RENTAL_PERIOD)
        ).click()

        rental_option = (
            By.XPATH,
            f"//div[@class='Dropdown-option' "
            f"and @role='option' "
            f"and normalize-space()='{period}']"
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(rental_option)
        ).click()

    def select_scooter_color(self, color):
        if color == "чёрный жемчуг":
            locator = self.BLACK_SCOOTER
        elif color == "серая безысходность":
            locator = self.GREY_SCOOTER
        else:
            raise ValueError(f"Неизвестный цвет самоката: {color}")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_comment(self, comment):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMMENT_INPUT)
        ).send_keys(comment)

    def click_back(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BACK_BUTTON)
        ).click()

    def click_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTTOM_ORDER_BUTTON)
        ).click()

    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()
    
    
    def is_order_successful(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ORDER_STATUS_BUTTON)
        ).is_displayed()
    