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
form_first = "John"
query = f"INSERT INTO friends (first_name) VALUES (?)"

c.execute(query, (form_first,) ) # add tuple
conn.commit()
conn.close()
