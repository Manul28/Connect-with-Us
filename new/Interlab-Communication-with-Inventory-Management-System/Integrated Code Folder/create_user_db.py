import sqlite3

# Create a connection to the database
conn = sqlite3.connect('user_credentials.db')

# Create a cursor to interact with the database
cursor = conn.cursor()

# Create a table to store user credentials
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
