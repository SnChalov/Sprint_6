from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage


def test_scooter_logo_returns_to_main_page(driver):
    main_page = MainPage(driver)

    main_page.click_order_button(0)

    WebDriverWait(driver, 10).until(
        lambda driver: "/order" in driver.current_url
    )

    assert "/order" in driver.current_url

    main_page.click_scooter_logo()

    WebDriverWait(driver, 10).until(
        lambda driver: driver.current_url
        == "https://qa-scooter.praktikum-services.ru/"
    )

    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


def test_yandex_logo_opens_dzen(driver):
    main_page = MainPage(driver)

    original_window = driver.current_window_handle

    main_page.click_yandex_logo()

    WebDriverWait(driver, 10).until(
        lambda driver: len(driver.window_handles) > 1
    )

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            break

    WebDriverWait(driver, 10).until(
        lambda driver: "dzen.ru" in driver.current_url
    )

    assert "dzen.ru" in driver.current_url