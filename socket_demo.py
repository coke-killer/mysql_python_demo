# __author__: "yudongyue"
# date: 2021/4/9
import socket
import sys

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 设置端口号
port = 9999
server_socket.bind((host, port))
# 设置最大连接数
server_socket.listen(5)
while True:
    # 建立客户端连接
    client_socket, addr = server_socket.accept()
    print("连接地址: %s" % str(addr))
    msg = "欢迎访问菜鸟教程"
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()
