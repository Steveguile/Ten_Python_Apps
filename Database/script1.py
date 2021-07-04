import psycopg2

def create_table():
	conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert(item, quanitity, price):
	conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
	cur=conn.cursor()
	cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quanitity, price))
	conn.commit()
	conn.close()

def view():
	conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
	cur=conn.cursor()
	cur.execute("SELECT * FROM store")
	row=cur.fetchall()
	conn.commit()
	conn.close()

	for item in row:
		print(item)

def delete(item):
	conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
	cur=conn.cursor()
	cur.execute("DELETE FROM store WHERE item=%s", (item,))
	conn.commit()
	conn.close()

def update(item, quantity, price):
	conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
	cur=conn.cursor()
	cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item,))
	conn.commit()
	conn.close()
