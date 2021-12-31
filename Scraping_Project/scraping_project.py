import sqlite3
import requests
from bs4 import BeautifulSoup

# REQUEST URL
url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.select(".price_color")[0].get_text()
    price = float(price.replace("£", "").replace("Â", ""))
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    print(rating)

# INIT BS4
# EXTRACT DATA
# SAVE TO DB
