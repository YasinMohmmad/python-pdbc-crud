# curd operations

# accesing the database
import mysql.connector as s
con=s.connect(host="localhost",user="root",password="yasinsql007",database="college")
cur=con.cursor()

try:
    # user input options on database
    while True:
        print("="*50)
        print("\t STUDENT MANAGEMENT SYSTEM\t")
        print("="*50)
        print("1.INSERT")
        print("2.SELECT")
        print("3.UPDATE")
        print("4.DELETE")
        print("5.EXIT")

        ch=int(input("SELECT THE NUMBER TO PERFORM THE OPERATION:"))

        # INSERT
        if ch==1:
            id=int(input("enter the student id:"))
            name=input("enter the name:")
            branch=input("enter the branch of the student:")
            sql="""insert into students values(%s,%s,%s)"""
            data=(id,name,branch)
            cur.execute(sql,data)
            con.commit()
            print("DATA INSERTED SUCCESSFULLY!")

        #select    
        elif ch==2:
            cur.execute("select * from students")
            res=cur.fetchall()
            print("id\tname\tbranch")
            for i in res:
                print(i[0],"\t",i[1],"\t",i[2])

        #update
        elif ch==3:
            id=int(input("enter the id to update:"))
            name=input("enter new name:")
            branch=input("enter new branch:")
            sql="""update students set name=%s,branch=%s where id=%s"""
            data=(name,branch,id)
            cur.execute(sql,data)
            con.commit()
            print("DATABASE UPDATED SUCCESFULLY!")

        #DELETE
        elif ch==4:
            id=int(input("enter the id to delete:"))
            sql="""delete from students where id=%s"""
            data=(id,)
            cur.execute(sql,data)
            con.commit()
            print("DATA DELETED SUCCESSFULLY!")

        # EXIT
        elif ch==5:
            print("APPLICATION CLOSED")
            break
        else:
            print("INVALID CHOICE")
except Exception as e:
    print("error: ",e)
con.close()



