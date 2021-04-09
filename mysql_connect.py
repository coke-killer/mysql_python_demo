# __author__: "yudongyue"
# date: 2021/4/9
import mysql.connector


def get_connection():
    return mysql.connector.connect(host="localhost", user="root", password="yudongyue", database="test")
