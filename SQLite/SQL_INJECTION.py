import sqlite3
conn = sqlite3.connect("user.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE users (username TEXT, password TEXT);")
conn.commit()
conn.close()
