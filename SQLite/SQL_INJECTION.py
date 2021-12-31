import sqlite3
conn = sqlite3.connect("user.db")

user = input("Please, enter your name...")
password = input("Please, enter your password...")
query = f"SELECT * FROM users WHERE username='{user}' AND password='{password}'"

cursor = conn.cursor()
cursor.execute(query)

result = cursor.fetchone()
if result:
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()
