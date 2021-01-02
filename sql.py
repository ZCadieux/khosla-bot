import sqlite3
from sqlite3 import Error

connection = None
c = None

def sql_connect(file):
    try:
        global connection
        global c
        connection = sqlite3.connect(file)
        c = connection.cursor()
    except Error as e:
        print(f"Error '{e}' occurred when connecting to database.sql")

def init(file):
    sql_connect(file)
    c.execute("CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER AUTOINCREMENT"
        "user_hash TEXT PRIMARY KEY,"
        "counter INTEGER"
    ")")

    c.execute("CREATE TABLE IF NOT EXISTS confessions ("
        "id INTEGER PRIMARY KEY,"
        "author INTEGER,"
        "submission TEXT,"
        "verify_id INTEGER,"
        "submission_id INTEGER,"
        "approved INTEGER,"
        "FOREIGN KEY(author) REFERENCES users(id)"
    ")")

    connection.commit()

def confess(user, confession):
    # TODO - form messages/embeds, add to db, add user if necessary and send them their user id, and send to #confessions-queue
    print("confession: ", user, confession)

def approve(admin_id):
    # TODO - set approved to 1, send message in #confessions, send confirmation in #confessions-queue
    print("approving: ", admin_id)

def deny(admin_id):
    # TODO - set apporved to 2, send confirmation in #confessions-queue
    print("denying: ", admin_id)