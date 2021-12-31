import sqlite3
conn = sqlite3.connect("user.db")

cursor = conn.cursor()

list_of_users = [
    ("John", "123"),
    ("Sarah", "555"),
    ("Terminator", "800")
]

cursor.executemany("INSERT INTO users VALUES (?, ?)", list_of_users)

conn.commit()
conn.close()
