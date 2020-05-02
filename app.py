import requests

from pages.all_books_page import CataloguePage

page_content = requests.get('http://books.toscrape.com').content
page = CataloguePage(page_content)

books = page.books