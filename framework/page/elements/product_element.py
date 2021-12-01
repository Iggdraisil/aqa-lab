from enum import Enum

from selenium.webdriver.remote.webelement import WebElement

from framework.driver.webdriver import Driver
from framework.page.base import Base


class ProductElementRelativeLocator(str, Enum):
    LINK = 'div/h2/a'
    NOTIFY_BUTTON = 'div/div[3]/div/form/div[2]/a'
    ADD_TO_CART_BUTTON = 'div/div[3]/div/form/div[2]/span[3]/input'
    QUANTITY_FIELD = 'div/div[3]/div/form/div[2]/span[1]/input'
    AVAILABILITY_FIELD = 'div/div[2]/div[2]/div[1]'


class ProductElement(Base):
    def __init__(self, driver: WebElement):
        super().__init__(driver)

    @property
    def link(self):
        return self._find_element(ProductElementRelativeLocator.LINK)

    @property
    def notify_button(self):
        return self._wait_for_element_to_be_clickable(ProductElementRelativeLocator.NOTIFY_BUTTON)

    @property
    def cart_button(self):
        return self._wait_for_element_to_be_clickable(ProductElementRelativeLocator.ADD_TO_CART_BUTTON)

    @property
    def cart_quantity(self):
        return self._wait_for_element_to_be_clickable(ProductElementRelativeLocator.QUANTITY_FIELD)

    @property
    def availability_field(self):
        return self._find_element(ProductElementRelativeLocator.AVAILABILITY_FIELD)

    def is_available(self) -> bool:
        self._wait_to_locate_text(ProductElementRelativeLocator.AVAILABILITY_FIELD, 'В наявності:')
        return self.availability_field.text != 'В наявності: 0'

    def check_presence_of_notify_button(self):
        self._wait_for_element(ProductElementRelativeLocator.NOTIFY_BUTTON, "Notify button isn't visible")

    def check_presence_of_cart_buttons(self):
        self._wait_for_element(ProductElementRelativeLocator.ADD_TO_CART_BUTTON, "Add to cart button isn't visible")
        self._wait_for_element(ProductElementRelativeLocator.QUANTITY_FIELD, "Quantity button isn't visible")

    def add_to_cart(self):
        self.driver.parent.execute_script('arguments[0].click()', self.cart_button)

    def notify(self):
        self.driver.parent.execute_script('arguments[0].click()', self.notify_button)
