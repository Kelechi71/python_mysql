import pymysql

#database connection
connection =  pymysql.Connect(host="localhost", user="root", passwd="", database="databaseName")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "Select * from Artists;"

#executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
   print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()