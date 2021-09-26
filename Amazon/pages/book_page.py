from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):
    def should_be_book_page(self):
        assert self.is_element_present(*BookPageLocators.ARTS_LINK), "Arts & Photography Books is not presented"
        assert self.is_element_present(*BookPageLocators.BIOGRAPH_LINK), "Biographies & Memoirs is not presented"

