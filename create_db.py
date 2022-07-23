import sqlite3 as sql

# Connect to SQLite
con = sql.connect('db_web.db')

# Create a Connection
cur = con.cursor()

# Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

# Create users table  in db_web database
sql = '''
CREATE TABLE "users" (
"UID" INTEGER PRIMARY KEY AUTOINCREMENT,
"UNAME"	TEXT,
"CONTACT" TEXT
)
'''
cur.execute(sql)

# Commit changes
con.commit()

# Close the connection
con.close()
