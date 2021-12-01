from enum import Enum, auto


class MainPageLocators(str, Enum):
    TOP_BAR = '//*[@id="main-menu"]'
    SECTION = '/html/body/div[2]/div[2]/div/div/div/div/div[1]/aside/div/div/div/ul/li[{}]'
    SECTION_LINK = '/html/body/div[2]/div[2]/div/div/div/div/div[1]/aside/div/div/div/ul/li[{}]/div/a'
    CART_LINK = '/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/a'
    TOTAL_PRODUCTS = '/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]'
    TOTAL_AMOUNT = '/html/body/div[2]/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[5]'


class Sections(int, Enum):
    FIGURINES_BIG = 1
    FIGURINES_SMALL = auto()
    JAPANESE_SWEETS = auto()
    ARTBOOKS = auto()
    POSTERS = auto()
    MANGA = auto()
    COSPLAY = auto()
    ACCESSORIES = auto()
    NOTEBOOKS = auto()
    KEYCHAINS = auto()
    BADGES = auto()
    MAGNETS = auto()
    STICKERS = auto()
    PASSPORT_CLOSURES = auto()
    BAGS = auto()
    CUPS = auto()
    COLLECTION_ITEMS = auto()
    JAPANESE_MANGA = auto()
    K_POP = auto()
