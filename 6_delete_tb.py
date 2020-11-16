import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="databaseName")
cursor = connection.cursor()
dropSql = "DROP TABLE IF EXISTS Artists;"
cursor.execute(dropSql)
