import sqlite3
import requests
from bs4 import BeautifulSoup

# REQUEST URL
url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"


def scrape_books(url_str: str):
    response = requests.get(url_str)

    # INIT BS4
    soup = BeautifulSoup(response.text, "html.parser")

    # EXTRACT DATA
    books = soup.find_all("article")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    print(all_books)


def get_title(book) -> str:
    return book.find("h3").find("a")["title"]


def get_price(book) -> float:
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book) -> int:
    paragraph = book.select(".star-rating")[0]
    ratings = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]


scrape_books(url)

# SAVE TO DB
