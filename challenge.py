# SQLite3 module 
import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
    (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT, last_name TEXT, 
        email_address TEXT)''')
users_to_insert = [('kedar', 'dhoble', 'kedardhoble@gmail.com'),
                   ('keda', 'dhobl', 'kedadhobl@gmail.com'),
                   ('ked', 'dhob', 'keddhob@gmail.com'),
                   ('ke', 'dho', 'kedho@gmail.com')]

cursor.executemany('''INSERT INTO Users(first_name, last_name, email_address) VALUES (?,?,?)''', users_to_insert)
cursor.execute("SELECT * FROM Users")

print(cursor.fetchall())

connection.commit()
connection.close()


# SQLAlchemmy without the expression language 
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///user.db', echo=True)
users_to_insert = [{'first_name': 'kedar', 'last_name': 'dhoble', 'email_address': 'kedardhoble@gmail.com'},
                   {'first_name': 'keda', 'last_name': 'dhobl', 'email_address': 'kedadhobl@gmail.com'},
                   {'first_name': 'ked', 'last_name': 'dhob', 'email_address': 'keddhob@gmail.com'},
                   {'first_name': 'ke', 'last_name': 'dho', 'email_address': 'kedho@gmail.com'}]

with engine.connect() as conn:
    conn.execute(sqlalchemy.text('''CREATE TABLE IF NOT EXISTS Users (user_id 
        INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, 
        email_address TEXT)'''))
    
    conn.execute(sqlalchemy.text('''INSERT INTO Users(first_name, last_name, email_address) VALUES (:first_name, :last_name, :email_address)'''), users_to_insert)

    result = conn.execute(sqlalchemy.text('''SELECT * FROM Users'''))
    for row in result:
        print(row)


# SQLAlchemmy with the expression language 
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///user.db', echo=True)
users_to_insert = [{'first_name': 'kedar', 'last_name': 'dhoble', 'email_address': 'kedardhoble@gmail.com'},
                   {'first_name': 'keda', 'last_name': 'dhobl', 'email_address': 'kedadhobl@gmail.com'},
                   {'first_name': 'ked', 'last_name': 'dhob', 'email_address': 'keddhob@gmail.com'},
                   {'first_name': 'ke', 'last_name': 'dho', 'email_address': 'kedho@gmail.com'}]

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("users",
                               metadata,
                               sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                               sqlalchemy.Column("first_name", sqlalchemy.Integer),
                               sqlalchemy.Column("last_name", sqlalchemy.Integer),
                               sqlalchemy.Column("email_address", sqlalchemy.Integer)
                               )
metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)


