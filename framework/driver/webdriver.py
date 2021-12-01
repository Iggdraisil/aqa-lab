from dataclasses import dataclass
from typing import Type

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from ..utils.singleton import singleton
from framework.driver.browser_type import BrowserType
from framework.driver.web_driver_factory import factory


@singleton
class Driver(WebDriver):
    def __init__(self, browser_type: BrowserType):
        driver = factory.get_web_driver(browser_type)
        driver.implicitly_wait(1)
        driver.set_window_size(1920, 1080)
        self.driver = driver

    def __getattr__(self, item):
        return getattr(self.driver, item)
