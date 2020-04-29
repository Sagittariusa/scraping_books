from bs4 import BeautifulSoup

from locators.books_page_locators import BooksPageLocators
from parsers.book_parser import BookParser

class CataloguePage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BooksPageLocators.BOOKS)]