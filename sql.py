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

def run(*x):
    c.execute(*x)
    connection.commit()

def init(file):
    sql_connect(file)

    run("CREATE TABLE IF NOT EXISTS confessions ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "submission TEXT NOT NULL,"
        "verify_id INTEGER NOT NULL,"
        "submission_id INTEGER,"
        "approved INTEGER DEFAULT 0"
    ")")

def confess(confession):
    # TODO - Send message in #confessions-queue

    # TODO - Set this to the message ID after it's sent into the #confessions-queue
    msgid = 1; 

    run("INSERT INTO confessions (submission, verify_id)"
        "VALUES (?,?)", [confession, msgid])


def approve(msg_id):
    # TODO - Send confirmation in #confessions-queue and send confession in #confessions

    run("UPDATE confessions"
        "SET approved = 1"
        "WHERE verify_id=?"
        "LIMIT 1", [msg_id])
    print("approving: ", msg_id)

def deny(msg_id):
    # TODO - set apporved to 2, send confirmation in #confessions-queue

    run("UPDATE confessions"
        "SET approved = 2"
        "WHERE verify_id=?"
        "LIMIT 1", [msg_id])
    print("denying: ", admin_id)