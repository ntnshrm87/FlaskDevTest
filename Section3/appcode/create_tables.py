import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS stores (name text, noOfBooks real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO stores VALUES ('test', 10000)")

connection.commit()

connection.close()

