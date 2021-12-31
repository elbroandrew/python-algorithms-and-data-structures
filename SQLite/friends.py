import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()
c.execute("SELECT * FROM friends")
for person in c:
    print(person)

conn.commit()
conn.close()
