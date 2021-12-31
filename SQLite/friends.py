import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()
c.execute("SELECT * FROM friends WHERE first_name IS 'John'")

print(c.fetchone())

conn.commit()
conn.close()
