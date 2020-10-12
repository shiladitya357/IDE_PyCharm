import sqlite3

# connect
connection = sqlite3.connect("credentials.db")
# get cursor
cursor = connection.cursor()
# execute queries
cursor.execute("drop table auth")
cursor.execute("create table auth(userid text, password text, role txt)")
cursor.execute("insert into auth values('admin','admin123','root')")
users = [('shila','password','developer'),
         ('shila1','password1','developer1')]

cursor.executemany("insert into auth values(?,?,?)",users)
cursor.execute("select * from auth")
print(cursor.fetchall())
# commit
connection.commit()
# close
connection.close()
