# __author__: "yudongyue"
# date: 2021/4/9
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="yudongyue", database="test")
cursor = db.cursor()
sql = "update user set u_name=%s,u_age=%s where u_id=1"
param = ("小刘", "1",)
cursor.execute(sql, param)
db.commit()
