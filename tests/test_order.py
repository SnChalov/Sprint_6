import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.mark.parametrize(
    "order_button, name, surname, address, metro, phone, date, period, color, comment",
    [
        (
            0,
            "Фёдор",
            "Чалов",
            "Москва, ул. Тверская, д. 1",
            "Бульвар Рокоссовского",
            "89991234567",
            "17.09.2026",
            "сутки",
            "чёрный жемчуг",
            "Позвонить за час до доставки"
        ),
        (
            1,
            "Иван",
            "Петров",
            "Москва, ул. Арбат, д. 10",
            "Красносельская",
            "89997654321",
            "18.09.2026",
            "двое суток",
            "серая безысходность",
            "Оставить самокат у двери"
        ),
    ]
)
def test_order(
    driver,
    order_button,
    name,
    surname,
    address,
    metro,
    phone,
    date,
    period,
    color,
    comment
):
    main_page = MainPage(driver)

    main_page.close_cookie_notification()

    main_page.click_order_button(order_button)

    WebDriverWait(driver, 10).until(
        lambda driver: "/order" in driver.current_url
    )

    order_page = OrderPage(driver)

    order_page.enter_name(name)
    order_page.enter_surname(surname)
    order_page.enter_address(address)
    order_page.enter_metro(metro)
    order_page.enter_phone(phone)

    order_page.click_next()

    order_page.enter_delivery_date(date)
    order_page.select_rental_period(period)
    order_page.select_scooter_color(color)
    order_page.enter_comment(comment)

    order_page.click_order()
    
    order_page.confirm_order()
    
    assert order_page.is_order_successful()
    