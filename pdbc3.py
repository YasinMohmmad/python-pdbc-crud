import mysql.connector as s
con=s.connect(host="localhost",user="root",password="yasinsql007",database="college")

cur=con.cursor()
# cur.execute("show databases")
# res=cur.fetchall()
# for i in res:
#     print(i)
# con.close()
# cur.execute("insert into students values(5,'chandra','ece')")
# con.commit()



# cur.execute("select distinct * from students") 
# res=cur.fetchall()
# for i in res:
#     print(i)
# con.close()

# user=int(input("enter the id:"))
# cur.execute("select distinct * from students where id=%s",[user])
# res=cur.fetchall()
# print(res)
# data=[(6,"cahal","mech"),(7,"rahul","civil"),(8,"nitish","ds")]
# sql=cur.executemany("insert into students values(%s,%s,%s)",data)
# con.commit()
cur.execute("delete from students where id=%s",[1])
con.commit()
cur.execute("select distinct * from students")
re=cur.fetchall()
for i in re:
    print(i)
con.close()