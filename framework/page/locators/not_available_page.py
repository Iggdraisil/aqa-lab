from enum import Enum


class NotAvailablePageLocator(str, Enum):
    EMAIL_FIELD = '//*[@id="notify_email"]'
    SUBSCRIBE_BUTTON = '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[2]/form/input[2]'
    ALERT_ELEMENT = '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div'
