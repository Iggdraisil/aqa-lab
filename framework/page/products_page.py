from framework.page.base import Base
from framework.page.locators.products_page import ProductLocators

from selenium.webdriver.support.expected_conditions import *


class ProductsPage(Base):
    @property
    def criteria_button(self):
        return self._find_element(ProductLocators.SORTING_CRITERIA)

    @property
    def all_criteria_container(self):
        return self._find_element(ProductLocators.ALL_CRITERIAS_CONTAINER)

    @property
    def all_criteria(self):
        return self._find_elements(ProductLocators.ALL_CRITERIAS)

    def hover_on_criteria_and_check_dropdown(self):
        self._move_to_element(self.criteria_button)
        assert self.all_criteria_container.is_displayed()

    def select_criteria(self, number: int):
        btn_text = self.criteria_button.text
        self.hover_on_criteria_and_check_dropdown()
        self.all_criteria[number].click()
        assert btn_text != self.criteria_button.text

    def get_all_products_from_row(self, number: int):
        general_query = ProductLocators.PRODUCT_ROW.value.format(2 + (number - 1) * 2, '*')
        for elem in range(len(self._find_elements(general_query))):
            yield self._find_element(ProductLocators.PRODUCT_ROW.value.format(2 + (number - 1) * 2, elem + 1))
