from framework.page.base import Base
from .locators.main_page import MainPageLocators, Sections

from selenium.webdriver.support.expected_conditions import *


class MainPage(Base):

    def wait_to_load(self):
        return self._wait_for_element(MainPageLocators.TOP_BAR)

    def section(self, section: Sections):
        return self._find_element(MainPageLocators.SECTION_LINK.format(str(section.value)))

    def section_link(self, section: Sections):
        return self._find_element(MainPageLocators.SECTION_LINK.format(str(section.value)))

    @property
    def cart_button(self):
        return self._find_element(MainPageLocators.CART_LINK)

    @property
    def total_products(self):
        return self._find_element(MainPageLocators.TOTAL_PRODUCTS)

    @property
    def total_amount(self):
        return self._find_element(MainPageLocators.TOTAL_AMOUNT)

    def check_cart_is_empty(self):
        # TODO
        assert self.total_products.text == 'Кошик порожній', f'Cart is not empty: {self.total_products.text}'

    def check_cart_has_products(self, number_of_products: int):
        # TODO
        if number_of_products == 0:
            assert self.total_products.text == 'Кошик порожній'
        elif number_of_products == 1:
            assert self.total_products.text == '1 товар'
        else:
            assert self.total_products.text == f'Товарів: {number_of_products}'

    def open_section_and_check_it_is_selected(self, section: Sections):
        self.section(section).click()
        assert self.section(section).value_of_css_property('color') == 'rgb(89, 166, 226)'

    def go_to_cart(self):
        url = self.driver.current_url
        self.driver.execute_script('arguments[0].click()', self.cart_button)
        self._wait.until(url_changes(url))
