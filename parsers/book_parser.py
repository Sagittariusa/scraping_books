import re

from locators.book_locators import BookLocators

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    def __init__(self, parent):
        self.parent = parent

    
    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, {self.rating} stars>'
    

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    def link(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        price_float = float((re.search("£([0-9]+\.[0-9]+)", item_price)).group(1))
        return price_float

    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating = [c for c in classes if 'star-rating' != c]
        rating_number = BookParser.RATINGS.get(rating[0])
        return rating_number