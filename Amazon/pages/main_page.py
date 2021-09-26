from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def go_to_book_page(self):
        book_select = Select(self.browser.find_element(*MainPageLocators.CATEGORY_BTN))
        book_select.select_by_visible_text("Books")
        book_go = self.browser.find_element(*MainPageLocators.SEARCH_BTN)
        book_go.click()

    def should_be_search(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), "Search field is not presented"
        assert self.is_element_present(*MainPageLocators.SEARCH_BTN), "Search button is not presented"

    def should_be_book_page(self):
        assert self.is_element_present(*BookPageLocators.ARTS_LINK), "Arts & Photography Books is not presented"
        assert self.is_element_present(*BookPageLocators.BIOGRAPH_LINK), "Biographies & Memoirs is not presented"


