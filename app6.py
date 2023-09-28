import sqlite3

def get_user(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    user = cursor.fetchone()
    connection.close()

    return user


def get_user(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    user = cursor.fetchone()
    connection.close()

    return user


import hashlib

def hash_password(password):
    salt = "random_salt_here"
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed
