#! /usr/bin/env python
# -*- coding: utf-8 -*-
import socket
s = socket.socket()
host = socket.gethostname()
port = 1286
s.connect((host, port))                 # 需要连接的服务器，端口。本次测试为同一台主机
while True:
    user_input = input("请输入要传输的信息：")
    s.send(str.encode(user_input))      # send方法把信息传输给服务器端，encode方法将信息转化为byte类型
    Data = s.recv(1024)                 # recv方法用于接收数据，后面1024是每次接收数据的最大长度
    print(Data)                         # 打印服务器端传输过来的内容
s.close()                               # 关闭连接
