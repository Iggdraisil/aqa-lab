from enum import Enum


class CartPageLocators(str, Enum):
    EMAIL_FIELD = '//*[@id="email_field"]'
    NAME_FIELD = '//*[@id="first_name_field"]'
    SURNAME_FIELD = '//*[@id="last_name_field"]'
    CITY_FIELD = '//*[@id="city_field"]'
    PHONE_FIELD = '//*[@id="phone_2_field"]'
    ORDER_PRODUCTS = '//*[@class="order-product"]'
    DELIVERY_NOVA_POSHTA = '//*[@id="shipment_id_1"]'
    DELIVERY_NOVA_POSHTA_PREPAYMENT = '//*[@id="shipment_id_2"]'
    DELIVERY_SELF_PICKUP = '//*[@id="shipment_id_5"]'
    PRE_PAYMENT = '//*[@id="payment_id_1"]'
    PAYMENT_DURING_TAKEAY = '//*[@id="payment_id_2"]'
    PAYMENT_CASH = '//*[@id="payment_id_3"]'
    SUBMIT = '//*[@id="submit_order_done"]'
