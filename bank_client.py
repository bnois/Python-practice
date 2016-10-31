import socket
import time

s_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建客户端socket对象
s_client.connect(('localhost',9001)) #客户端发起连接请求
time.sleep(3) #等待连接建立

#建立连接后---
login_right=False
while login_right==False:
    print "请输入用户名："
    name=raw_input()
    s_client.send(name)#发送用户名
    print "请输入密码："
    password=raw_input()
    s_client.send(password)#发送密码
    login_result=s_client.recv(1024)
    print login_result
    if login_result=="登陆成功":
        login_right=True

s_client.close() #连接关闭，释放资源



