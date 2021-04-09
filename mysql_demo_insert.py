# __author__: "yudongyue"
# date: 2021/4/9
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="yudongyue", database="test")
cursor = db.cursor()
sql = "insert into user(u_name,u_age,u_time) values(%s,%s,%s)"
params_1 = ('小王', '10', '19971204')
params_2 = ('小于', '10', '19971204')
params_3 = ('小张', '10', '19971204')
cursor.executemany(sql, [params_1, params_2, params_3])
db.commit()
