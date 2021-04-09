# __author__: "yudongyue"
# date: 2021/4/9
import mysql.connector

# 建立连接
db = mysql.connector.connect(host="localhost", user="root", password="yudongyue", database="test")
# 获取游标
my_cursor = db.cursor()
# 定义sql
sql = "select * from user where u_id=%s"
u_id = (1,)
# 执行sql
my_cursor.execute(sql, u_id)
results = my_cursor.fetchall()
for res in results:
    print(res)
