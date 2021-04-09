# __author__: "yudongyue"
# date: 2021/4/9
import mysql_connect

db = mysql_connect.get_connection()
cursor = db.cursor()
sql = "delete from user where u_id=1"
cursor.execute(sql)
db.commit()
