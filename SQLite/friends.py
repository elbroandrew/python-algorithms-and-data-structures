import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()
c.execute("SELECT * FROM friends")

print(c.fetchall())

conn.commit()
conn.close()
