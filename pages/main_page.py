import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    ORDER_BUTTONS = (By.XPATH, "//button[text()='Заказать']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "img[alt='Yandex']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")
    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    @allure.step("Закрыть уведомление о cookies")
    def close_cookie_notification(self):
        self.click_element(self.COOKIE_BUTTON)

    @allure.step("Получить локатор вопроса FAQ №{number}")
    def get_faq_question(self, number):
        return (
            By.ID,
            f"accordion__heading-{number}"
        )

    @allure.step("Открыть вопрос FAQ №{number}")
    def click_faq_question(self, number):
        question = self.get_faq_question(number)
    
        self.scroll_to_element(question)
        self.click_element(question)

    @allure.step("Получить ответ FAQ №{number}")
    def get_faq_answer(self, number):
        answer = self.find_element(
            (
                By.ID,
                f"accordion__panel-{number}"
            )
        )

        return answer.text

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Нажать на кнопку 'Заказать' №{number}")
    def click_order_button(self, number):
        self.click_element_from_list(self.ORDER_BUTTONS, number)
        