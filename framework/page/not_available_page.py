from framework.page.base import Base
from framework.page.locators.not_available_page import NotAvailablePageLocator

from selenium.webdriver.support.expected_conditions import *


class NotAvailablePage(Base):
    @property
    def email_field(self):
        return self._find_element(NotAvailablePageLocator.EMAIL_FIELD)

    @property
    def subscribe_button(self):
        return self._find_element(NotAvailablePageLocator.SUBSCRIBE_BUTTON)

    def check_subscribe_on_empty_field(self):
        self.email_field.clear()
        self.subscribe_button.click()
        self._wait_for_element(NotAvailablePageLocator.ALERT_ELEMENT, "alert wasn't shown")

    def check_email_field_to_be_valid(self):
        self._validate_input(NotAvailablePageLocator.EMAIL_FIELD, 'oleh@gnu.org', 'text not present in input')
        previous_url = self.driver.current_url
        self.subscribe_button.click()
        self._wait.until(url_changes(previous_url), 'url has not changed')
        self.back()


