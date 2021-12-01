from framework.page.cart_page import CartPage, DeliveryType, PaymentType
from framework.page.elements.cart_popup import CartPopup
from framework.page.locators.main_page import Sections
from framework.page.main import MainPage
from framework.page.not_available_page import NotAvailablePage
from framework.page.elements.product_element import ProductElement
from framework.page.products_page import ProductsPage


class TestBuyAnime:

    def test_select_criteria(self, main_page, products_page):
        main_page.check_cart_is_empty()
        main_page.open_section_and_check_it_is_selected(Sections.NOTEBOOKS)
        products_page.hover_on_criteria_and_check_dropdown()
        products_page.select_criteria(1)

    def test_select_products(self, cart_popup, not_available_page, products_page, items_in_cart, main_page, cart_page):
        products = products_page.get_all_products_from_row(1)
        for product in products:
            element = ProductElement(product)
            if element.is_available():
                element.check_presence_of_cart_buttons()
                element.add_to_cart()
                cart_popup.check_page_remains_same_after_dismissed()
                items_in_cart += 1
            else:
                element.check_presence_of_notify_button()
                element.notify()
                not_available_page.check_subscribe_on_empty_field()
                not_available_page.check_email_field_to_be_valid()
                not_available_page.back()
        main_page.check_cart_has_products(items_in_cart)
        main_page.go_to_cart()
        cart_page.validate_number_of_products(items_in_cart)

    def test_buy_anime(
            self,
            main_page: MainPage,
            products_page: ProductsPage,
            not_available_page: NotAvailablePage,
            cart_popup: CartPopup,
            cart_page: CartPage,
            items_in_cart,
    ):

        cart_page.validate_city('New York')
        cart_page.validate_phone('3802434234234')
        cart_page.validate_email('foo@bar.io')
        cart_page.validate_name('Ivan')
        cart_page.validate_surname('Petrovych')
        cart_page.select_delivery_type(DeliveryType.POST)
        cart_page.select_payment_type(PaymentType.PRE_PAYMENT)
