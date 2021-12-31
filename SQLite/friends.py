import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()

people = [
    ("Roland", "Amundsen", 5),
    ("Rosa", "Perks", 3),
    ("Neil", "Armstrong", 5),
    ("Henry", "Hudson", 2)
]

c.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

conn.commit()
conn.close()
