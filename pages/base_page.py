import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @allure.step("Создать объект страницы")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти все элементы")
    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Ввести текст")
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Дождаться URL")
    def wait_for_url(self, url_part):
        WebDriverWait(self.driver, 10).until(
            lambda driver: url_part in driver.current_url
        )

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1
        )

        new_window = next(
            window
            for window in self.driver.window_handles
            if window != original_window
        )

        self.driver.switch_to.window(new_window)

    @allure.step("Нажать на элемент из списка")
    def click_element_from_list(self, locator, number):
        elements = self.find_elements(locator)
        elements[number].click()

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
