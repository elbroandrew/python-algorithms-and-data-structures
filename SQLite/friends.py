import sqlite3
conn = sqlite3.connect("my_friends.db") # create db
# create cursor object
c = conn.cursor()

# execute some sql
#c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
insert_query = '''insert into friends
                    values ('Marry', 'Lewis', 7)'''
c.execute(insert_query)
conn.commit()
conn.close()
