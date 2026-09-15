from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
    
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    def wait_for_url(self, url_part):
        WebDriverWait(self.driver, 10).until(
            lambda driver: url_part in driver.current_url
        )
    
    def get_element_text(self, locator):
        return self.find_element(locator).text
