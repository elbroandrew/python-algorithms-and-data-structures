import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()

# execute some sql
#c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''insert into friends
#                     values ('Marry', 'Lewis', 7)'''

form_first = "Dana"
query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
c.execute(query)
conn.commit()
conn.close()
