from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from framework.driver.webdriver import Driver


class Base:
    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def _wait(self):
        return WebDriverWait(self.driver, 5)

    @staticmethod
    def _selector_from_xpath(xpath: str) -> tuple[By, str]:
        return By.XPATH, xpath

    @property
    def _action_chain(self):
        return ActionChains(self.driver)

    def _find_element(self, xpath: str):
        return self.driver.find_element(By.XPATH, xpath)

    def _find_elements(self, xpath: str):
        return self.driver.find_elements(By.XPATH, xpath)

    def _wait_for_element(self, xpath: str, msg='') -> WebElement:
        return self._wait.until(presence_of_element_located(self._selector_from_xpath(xpath)), msg)

    def _wait_for_element_to_be_clickable(self, xpath: str, msg='') -> WebElement:
        return self._wait.until(element_to_be_clickable(self._selector_from_xpath(xpath)), msg)

    def _wait_for_elements(self, xpath: str, msg=''):
        return self._wait.until(presence_of_all_elements_located(self._selector_from_xpath(xpath)), msg)

    def _wait_to_locate_text(self, xpath: str, text: str, msg=''):
        return self._wait.until(text_to_be_present_in_element(self._selector_from_xpath(xpath), text), msg)

    def _wait_until_selected(self, xpath: str, msg=''):
        return self._wait.until(element_located_selection_state_to_be(self._selector_from_xpath(xpath), True), msg)

    def _wait_to_locate_text_in_value(self, xpath: str, text: str, msg=''):
        return self._wait.until(text_to_be_present_in_element_value((By.XPATH, xpath), text), msg)

    def back(self) -> None:
        self.driver.back()

    def _move_to_element(self, element: WebElement):
        self._action_chain.move_to_element(element).perform()

    def _validate_input(self, xpath: str, keys: str, message=''):
        element = self._find_element(xpath)
        element.clear()
        element.send_keys(keys)
        self._wait_to_locate_text_in_value(xpath, keys, message)
