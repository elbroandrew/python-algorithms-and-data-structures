import sqlite3
import requests
from bs4 import BeautifulSoup

# REQUEST URL
url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
print(books)
# INIT BS4
# EXTRACT DATA
# SAVE TO DB
