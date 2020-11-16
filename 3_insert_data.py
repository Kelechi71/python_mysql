import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="databaseName")
cursor = connection.cursor()

# queries for inserting values
insert1 = "INSERT INTO Artists(NAME, TRACK) VALUES('Towang', 'Jazz' );"
insert2 = "INSERT INTO Artists(NAME, TRACK) VALUES('Sadduz', 'Rock' );"
insert3 = "INSERT INTO Artists(NAME, TRACK) VALUES('maek', 'zoko' );"

#executing the quires
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)

#commiting the connection then closing it.
connection.commit()
connection.close()