import msql.connector

db= my.sql.connector.connect(host = "localhost", database = "test" , user ="root" password = "November21!")

cursor = connection.cursor(prepared = True)
def update():
	
	sql_update = "UPDATE test SET downloads = downloads + 1 WHERE filename = %s"
	filename = ("test1.txt",)

	cursor.execute(sql_update,filename)
def delete ():
	sql_delete = "DELETE FROM test WHERE filename = %s"
	filename = ("test1.txt",)
	cursor.execute(sql_delete,filename)
	
db.commit()