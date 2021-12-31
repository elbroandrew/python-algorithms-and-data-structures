import sqlite3
conn = sqlite3.connect("user.db")

user = input("Please, enter your name...")
password = input("Please, enter your password...")
query = f"SELECT * FROM users WHERE username='{user}' AND password='' OR 1=1 --'" # так  делать нельзя, через тюпл желательно в execute, там санитайз срабатывает.
# Как решить:
cursor = conn.cursor()
query2 = f"SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query2, (user, password))

result = cursor.fetchone()
if result:
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()
