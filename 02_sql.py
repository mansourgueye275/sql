import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

cursor.execute("insert into population values('New York City',\
'NY',8400000 )")
cursor.execute("insert into population values('San Francisco',\
	'CA',800000) ")
conn.commit()

conn.close()
