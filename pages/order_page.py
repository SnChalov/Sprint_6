import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

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

    @allure.step("Ввести имя: {name}")
    def enter_name(self, name):
        self.enter_text(self.NAME_INPUT, name)

    @allure.step("Ввести фамилию: {surname}")
    def enter_surname(self, surname):
        self.enter_text(self.SURNAME_INPUT, surname)

    @allure.step("Ввести адрес: {address}")
    def enter_address(self, address):
        self.enter_text(self.ADDRESS_INPUT, address)

    @allure.step("Выбрать станцию метро: {metro}")
    def enter_metro(self, metro):
        metro_input = self.find_element(self.METRO_INPUT)

        metro_input.click()
        metro_input.send_keys(metro)

        metro_option = (
            By.XPATH,
            f"//button[contains(@class, 'select-search__option') "
            f"and .//div[normalize-space()='{metro}']]"
        )

        self.click_element(metro_option)

    @allure.step("Ввести телефон: {phone}")
    def enter_phone(self, phone):
        self.enter_text(self.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)

    @allure.step("Ввести дату доставки: {date}")
    def enter_delivery_date(self, date):
        self.enter_text(self.DELIVERY_DATE_INPUT, date)
        self.click_top_order_button()

    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period):
        self.click_element(self.RENTAL_PERIOD)

        rental_option = (
            By.XPATH,
            f"//div[@class='Dropdown-option' "
            f"and @role='option' "
            f"and normalize-space()='{period}']"
        )

        self.click_element(rental_option)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_scooter_color(self, color):
        if color == "чёрный жемчуг":
            locator = self.BLACK_SCOOTER
        elif color == "серая безысходность":
            locator = self.GREY_SCOOTER
        else:
            raise ValueError(f"Неизвестный цвет самоката: {color}")

        self.click_element(locator)

    @allure.step("Ввести комментарий: {comment}")
    def enter_comment(self, comment):
        self.enter_text(self.COMMENT_INPUT, comment)

    @allure.step("Нажать кнопку 'Назад'")
    def click_back(self):
        self.click_element(self.BACK_BUTTON)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order(self):
        self.click_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Проверить успешное оформление заказа")
    def is_order_successful(self):
        return self.find_element(
            self.ORDER_STATUS_BUTTON
        ).is_displayed()
