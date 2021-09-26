from .pages.main_page import MainPage
from .pages.book_page import BookPage



def test_guest_can_go_to_Book_page(browser):
    link = "https://amazon.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_book_page()
    page.should_be_search()
