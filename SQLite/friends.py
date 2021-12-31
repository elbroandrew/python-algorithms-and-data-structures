import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()

# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''insert into friends
#                     values ('Marry', 'Lewis', 7)'''

# BAD WAY !
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY
data = ("Sarah", "Connor", 25)
query = "INSERT INTO friends VALUES (?, ?, ?)"
c.execute(query, data) # add tuple
conn.commit()
conn.close()
