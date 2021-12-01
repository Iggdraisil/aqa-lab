from enum import Enum

from framework.page.base import Base
from framework.page.locators.cart_page_locators import CartPageLocators

from selenium.webdriver.support.expected_conditions import *


class DeliveryType(Enum):
    POST = CartPageLocators.DELIVERY_NOVA_POSHTA
    POST_PRE_PAYMENT = CartPageLocators.DELIVERY_NOVA_POSHTA
    SELF_PICKUP = CartPageLocators.DELIVERY_SELF_PICKUP


class PaymentType(Enum):
    DURING_GET = CartPageLocators.PAYMENT_DURING_TAKEAY
    PRE_PAYMENT = CartPageLocators.PRE_PAYMENT
    CASH = CartPageLocators.PAYMENT_CASH


class CartPage(Base):
    @property
    def email(self):
        return self._find_element(CartPageLocators.EMAIL_FIELD)

    @property
    def name(self):
        return self._find_element(CartPageLocators.NAME_FIELD)

    @property
    def city(self):
        return self._find_element(CartPageLocators.CITY_FIELD)

    @property
    def surname(self):
        return self._find_element(CartPageLocators.SURNAME_FIELD)

    @property
    def phone_number(self):
        return self._find_element(CartPageLocators.PHONE_FIELD)

    def delivery_type(self, delivery_type: DeliveryType):
        return self._find_element(delivery_type.value)

    def select_delivery_type(self, deliver_type: DeliveryType):
        if not isinstance(deliver_type, DeliveryType):
            raise ValueError
        self._action_chain.move_to_element(self.delivery_type(deliver_type))
        self.delivery_type(deliver_type).click()
        self._wait_until_selected(deliver_type.value)

    def payment_type(self, payment_type: PaymentType):
        return self._find_element(payment_type.value)

    def select_payment_type(self, payment_type: PaymentType):
        if not isinstance(payment_type, PaymentType):
            raise ValueError
        self._action_chain.move_to_element(self.payment_type(payment_type))
        self.payment_type(payment_type).click()
        self._wait_until_selected(payment_type.value)

    def validate_email(self, email: str):
        return self._validate_input(CartPageLocators.EMAIL_FIELD, email, 'email was not set')

    def validate_name(self, name: str):
        return self._validate_input(CartPageLocators.NAME_FIELD, name, 'name was not set')

    def validate_surname(self, surname: str):
        return self._validate_input(CartPageLocators.SURNAME_FIELD, surname, 'surname was not set')

    def validate_city(self, city: str):
        return self._validate_input(CartPageLocators.CITY_FIELD, city, 'city was not set')

    def validate_phone(self, phone: str):
        return self._validate_input(CartPageLocators.PHONE_FIELD, phone, 'phone was not set')

    def validate_number_of_products(self, number: int):
        assert number == len(self._find_elements(CartPageLocators.ORDER_PRODUCTS))
