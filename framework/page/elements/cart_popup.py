from enum import Enum

from framework.page.base import Base

from selenium.webdriver.support.expected_conditions import *


class CartPopupLocators(str, Enum):
    CONTINUE = '/html/body/div[7]/div/div[9]/div/a[1]'
    TAKE_TO_CART = '/html/body/div[7]/div/div[9]/div/a[2]'
    DISMISS = '//*[@id="fancybox-close"]'


class CartPopup(Base):
    @property
    def continue_shopping_button(self):
        return self._find_element(CartPopupLocators.CONTINUE)

    @property
    def take_to_cart_button(self):
        return self._find_element(CartPopupLocators.TAKE_TO_CART)

    @property
    def dismiss_button(self):
        return self._find_element(CartPopupLocators.DISMISS)

    def continue_shopping(self):
        return self.continue_shopping_button.click()

    def take_to_cart(self):
        return self.take_to_cart_button.click()

    def dismiss(self):
        self._wait.until(visibility_of_element_located(self._selector_from_xpath(CartPopupLocators.DISMISS)))
        self.dismiss_button.click()
        self._wait.until_not(visibility_of_element_located(self._selector_from_xpath(CartPopupLocators.DISMISS)))

    def check_page_remains_same_after_dismissed(self):
        url = self.driver.current_url
        self.dismiss()
        self._wait.until(url_to_be(url))
