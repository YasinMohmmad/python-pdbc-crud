import mysql.connector as s
con=s.connect(host="localhost",user="root",password="yasinsql007",database="college")
cur=con.cursor()
# created a database
# cur.execute("create database college")
# print("database created")
# con.close()
# # created a table
# cur.execute("""CREATE TABLE students(id INT,name VARCHAR(50),branch VARCHAR(30))""")
# print("Table Created")
# con.close()
# # inserted values in table
# sql="""insert into students values(%s,%s,%s)"""
# data=[(2,"raj","ece"),(3,"pandya","cse"),(4,"rohit","aiml")]
# cur.executemany(sql,data)
# con.commit()
# print("data inserted")
# con.close()

sql="""update students set branch=%s where id=%s"""
data=("AI",1)
cur.execute(sql,data)
con.commit()

sql="""delete from students where id=%s"""
data=(2,)
cur.execute(sql,data)
con.commit()

sql="""select distinct(*) from students"""
cur.execute(sql)
# con.commit()

# displayed values in the table
# cur.execute("select * from students")
r=cur.fetchall()
for i,j,k in r.items():
    print(i,j,k)
con.close()


