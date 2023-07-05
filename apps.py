import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')

famousFilms = [('Pulp Fiction', 'Quentin Tarentino', 1994), 
               ('Taxi Driver', 'Martin Scorsese', 1976),
               ('Moonrise Kingdom', 'Wes Anderson', 2012)]

cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)

cursor.execute("SELECT * FROM Movies")

print(cursor.fetchall())

connection.commit()
connection.close()

import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
    for row in result:
        print(row)


















# import sqlite3

# # Connect to the database (creates a new database if it doesn't exist)
# conn = sqlite3.connect('example.db')

# # Create a cursor object to execute SQL statements
# cursor = conn.cursor()

# # Create a table
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                   (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# # Insert a row
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))

# # Insert multiple rows
# users = [('Jane Smith', 'jane@example.com'),
#          ('Bob Johnson', 'bob@example.com')]
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

# # Commit the changes
# conn.commit()

# # Fetch data
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Close the cursor and the connection
# cursor.close()
# conn.close()

