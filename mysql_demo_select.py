# __author__: "yudongyue"
# date: 2021/4/9
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="yudongyue", database="test")
cursor = db.cursor()
sql = "select u_id,u_name,u_age from user group by u_name order by u_id desc "
cursor.execute(sql)
fetchall = cursor.fetchall()
for res in fetchall:
    print(res)
