import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="databaseName")
cursor = connection.cursor()

updateSql = "UPDATE  Artists SET NAME= 'jane', TRACK='johb' WHERE ID = '1' ;"
cursor.execute(updateSql)
connection.commit()
connection.close()

