import sqlite3

def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
	conn.commit()
	conn.close()

def insert(title, author, year, isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	conn.commit()
	conn.close()
	return rows

def search(title="", author="", year="", isbn=""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?", (title, author, year, isbn))
	rows=cur.fetchall()
	conn.commit()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(id, title="", author="", year="", isbn=""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET Title=?, Author=?, Year=?, ISBN=? WHERE id=?", (title, author, year, isbn, id))
	conn.commit()
	conn.close()

connect()
