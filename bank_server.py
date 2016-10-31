#!--encoding:gbk--
from socket import socket,AF_INET,SOCK_STREAM,timeout

s_server=socket(AF_INET,SOCK_STREAM)  #创建服务器socket
s_server.bind(('localhost',9001)) #将服务器socket绑定到地址上
s_server.listen(5) #开始监听TCP连接请求

#读取文件中的用户信息
f=file("user_info.txt")
user_info=f.readlines() #将文件中的每行用户信息都读取出来，并作为一个元素存放在列表user_info中
f.close()

#校验用户姓名
def get_user_name(n1):
    name_is_right=False  #使用变量name_is_right标识用户名是否正确，默认False
    for user1 in user_info:
        l_user1=user1.split()
        if n1==l_user1[0]: #判断输入的用户名和文件中的是否一致
            name_is_right=True  #用户名校验通过，修改变量name_is_right的值为True
            break
    return name_is_right

#校验用户密码
def get_user_password(n2,p2):
    password_is_right=False #使用变量password_is_right标识密码是否正确，默认False
    for user2 in user_info:
        l_user2=user2.split()
        if n2==l_user2[0] and p2==l_user2[1]: #判断用户名和对应的密码是否与文件中一致
            password_is_right=True #密码校验通过，修改变量password_is_right的值为True
            break
    return password_is_right

while True:
    connection,address=s_server.accept() #使用accept方法接收连接请求
                                         #在未接收连接请求前处于等待状态
    #建立连接后---
    try:
        connection.settimeout(30)  #设置超时时间
        login_right=False
        while login_right==False:
            name=connection.recv(1024)#接收用户名
            password=connection.recv(1024)#接收密码
            if get_user_name(name)==False: #校验用户名，查看用户名是否存在于文件中
                connection.send("用户名错误!请重新输入")
            elif get_user_password(name,password)==False: #校验密码，用户名对应的密码是否正确
                connection.send("密码错误!请重新输入")
            else:
                connection.send("登陆成功")
                login_right=True
    except timeout:
        print "time out"
    except:
        print "something wrong"
    connection.close() #终端本次连接请求，释放资源
    
s_server.close()


