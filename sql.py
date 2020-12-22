import sqlite3
from sqlite3 import Error

def sql_connect(file):
    try:
		global connection
        connection = sqlite3.connect(file)
    except Error as e:
        print(f"Error '{e}' occurred when connecting to database.sql")

def init():
	sql_connect()
	connection.execute("CREATE TABLE IF NOT EXISTS users ("
		"id INTEGER AUTOINCREMENT"
		"user_hash TEXT PRIMARY KEY,"
		"counter INTEGER,"
	")")

	connection.execute("CREATE TABLE IF NOT EXISTS confessions ("
		"id INTEGER PRIMARY KEY,"
		"author TEXT,"
		"submission TEXT,"
		"verify_id INTEGER,"
		"submission_id INTEGER,"
		"approved INTEGER,"
		"FOREIGN KEY(author) REFERENCES users(userid)"
	")")

def confess(user, confession):
	# TODO - form messages/embeds, add to db, add user if necessary and send them their user id, and send to #confessions-queue

def approve(admin_id):
	# TODO - set approved to 1, send message in #confessions, send confirmation in #confessions-queue

def deny(admin_id):
	# TODO - set apporved to 2, send confirmation in #confessions-queue