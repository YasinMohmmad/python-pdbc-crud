import mysql.connector as sql

con = sql.connect(
    user="root",
    host="localhost",
    password="yasinsql007"
)

print("Connected Successfully")
cur=con.cursor()
cur.execute("show databases")
for db in cur:
    print(db)

con.close()
