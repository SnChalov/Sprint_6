from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MainPage:

    ORDER_BUTTONS = (By.XPATH, "//button[text()='Заказать']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "img[alt='Yandex']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")
    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    def __init__(self, driver):
        self.driver = driver

    def close_cookie_notification(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COOKIE_BUTTON)
        ).click()

    def click_order_button(self, number):
        """Нажимает на кнопку 'Заказать'.
        
        number = 0 — верхняя кнопка.
        number = 1 — нижняя кнопка.
        """
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.ORDER_BUTTONS)
        )
        buttons[number].click()

    def get_faq_question(self, number):
        return (
            By.ID,
            f"accordion__heading-{number}"
        )

    def click_faq_question(self, number):
        question = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.get_faq_question(number)
            )
        )
    
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            question
        )
    
        time.sleep(1)
    
        question.click()

    def get_faq_answer(self, number):
        answer = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.ID,
                    f"accordion__panel-{number}"
                )
            )
        )
        return answer.text

    def click_scooter_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SCOOTER_LOGO)
        ).click()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.YANDEX_LOGO)
        ).click()
