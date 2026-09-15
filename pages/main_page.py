from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage

class MainPage(BasePage):

    ORDER_BUTTONS = (By.XPATH, "//button[text()='Заказать']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "img[alt='Yandex']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")
    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )
    
    def close_cookie_notification(self):
        self.click_element(self.COOKIE_BUTTON)
    
    def click_order_button(self, number):
        buttons = self.driver.find_elements(*self.ORDER_BUTTONS)
        buttons[number].click()
    
    def get_faq_question(self, number):
        return (
            By.ID,
            f"accordion__heading-{number}"
        )

    def click_faq_question(self, number):
        question = self.get_faq_question(number)
    
        self.find_element(question)
    
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            self.find_element(question)
        )
    
        time.sleep(1)
    
        self.click_element(question)
    
    def get_faq_answer(self, number):
        answer = self.find_element(
            (
                By.ID,
                f"accordion__panel-{number}"
            )
        )
    
        return answer.text

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
    