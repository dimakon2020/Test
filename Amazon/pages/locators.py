from selenium.webdriver.common.by import By

class MainPageLocators(object):
    CATEGORY_BTN = (By.ID, "searchDropdownBox")
    SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")


class BookPageLocators(object):
    ARTS_LINK = (By.CSS_SELECTOR, ".tile:nth-child(1) .a-color-base")
    BIOGRAPH_LINK = (By.CSS_SELECTOR, ".tile:nth-child(2) .a-color-base")




