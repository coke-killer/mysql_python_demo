# __author__: "yudongyue"
# date: 2021/4/8
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user='root',
    password="yudongyue"
)
print(my_db)
my_db_cursor = my_db.cursor()
# my_db_cursor.execute("SHOW DATABASES")
# for x in my_db_cursor:
#     print(x)
my_db_cursor.execute("use test")
my_db_cursor.execute("select * from user ")
x = my_db_cursor.fetchall()
for y in x:
    print(y)
