import allure
from pages.main_page import MainPage


class TestLogos:

    @allure.title("Проверка возврата на главную страницу по логотипу Самоката")
    def test_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_order_button(0)
        main_page.wait_for_url("/order")

        main_page.click_scooter_logo()
        main_page.wait_for_url("qa-scooter.praktikum-services.ru/")

        assert (
            main_page.get_current_url()
            == "https://qa-scooter.praktikum-services.ru/"
        )

    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url("dzen.ru")

        assert "dzen.ru" in main_page.get_current_url()
