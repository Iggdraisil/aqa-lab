from enum import Enum


class ProductLocators(str, Enum):
    SORTING_CRITERIA = '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div[2]/a'
    ALL_CRITERIAS_CONTAINER = '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div[1]/div[1]/div/div[3]'
    ALL_CRITERIAS = f'{ALL_CRITERIAS_CONTAINER}/*'
    PRODUCT_ROW = '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div[{}]/div[{}]'
