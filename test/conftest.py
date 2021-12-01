import time

from pytest import fixture

from framework.driver.browser_type import BrowserType
from framework.driver.webdriver import Driver
from framework.page.cart_page import CartPage
from framework.page.elements.cart_popup import CartPopup
from framework.page.main import MainPage
from framework.page.not_available_page import NotAvailablePage
from framework.page.products_page import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@fixture(scope='class')
def driver(request):
    driver = Driver(BrowserType(request.config.option.browser))
    driver.get('https://www.anime-tochka.com')
    yield driver
    time.sleep(2)
    driver.quit()


@fixture(scope='class')
def main_page(driver) -> MainPage:
    return MainPage(driver)


@fixture(scope='class')
def products_page(driver) -> ProductsPage:
    return ProductsPage(driver)


@fixture(scope='class')
def cart_popup(driver) -> CartPopup:
    return CartPopup(driver)


@fixture(scope='class')
def cart_page(driver) -> CartPage:
    return CartPage(driver)


@fixture(scope='class')
def not_available_page(driver) -> NotAvailablePage:
    return NotAvailablePage(driver)


value: int = 0


@fixture(scope='session')
def items_in_cart() -> int:
    return value
