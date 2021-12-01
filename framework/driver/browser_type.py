from enum import Enum, unique, auto


@unique
class BrowserType(Enum):
    FIREFOX = 'firefox'
    CHROME = 'chrome'
    INTERNET_EXPLORER = 'ie'
    EDGE = 'edge'
    SAFARI = 'safari'
    OPERA = 'opera'
