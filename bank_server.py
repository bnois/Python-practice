#!--encoding:gbk--
from socket import socket,AF_INET,SOCK_STREAM,timeout

s_server=socket(AF_INET,SOCK_STREAM)  #����������socket
s_server.bind(('localhost',9001)) #��������socket�󶨵���ַ��
s_server.listen(5) #��ʼ����TCP��������

#��ȡ�ļ��е��û���Ϣ
f=file("user_info.txt")
user_info=f.readlines() #���ļ��е�ÿ���û���Ϣ����ȡ����������Ϊһ��Ԫ�ش�����б�user_info��
f.close()

#У���û�����
def get_user_name(n1):
    name_is_right=False  #ʹ�ñ���name_is_right��ʶ�û����Ƿ���ȷ��Ĭ��False
    for user1 in user_info:
        l_user1=user1.split()
        if n1==l_user1[0]: #�ж�������û������ļ��е��Ƿ�һ��
            name_is_right=True  #�û���У��ͨ�����޸ı���name_is_right��ֵΪTrue
            break
    return name_is_right

#У���û�����
def get_user_password(n2,p2):
    password_is_right=False #ʹ�ñ���password_is_right��ʶ�����Ƿ���ȷ��Ĭ��False
    for user2 in user_info:
        l_user2=user2.split()
        if n2==l_user2[0] and p2==l_user2[1]: #�ж��û����Ͷ�Ӧ�������Ƿ����ļ���һ��
            password_is_right=True #����У��ͨ�����޸ı���password_is_right��ֵΪTrue
            break
    return password_is_right

while True:
    connection,address=s_server.accept() #ʹ��accept����������������
                                         #��δ������������ǰ���ڵȴ�״̬
    #�������Ӻ�---
    try:
        connection.settimeout(30)  #���ó�ʱʱ��
        login_right=False
        while login_right==False:
            name=connection.recv(1024)#�����û���
            password=connection.recv(1024)#��������
            if get_user_name(name)==False: #У���û������鿴�û����Ƿ�������ļ���
                connection.send("�û�������!����������")
            elif get_user_password(name,password)==False: #У�����룬�û�����Ӧ�������Ƿ���ȷ
                connection.send("�������!����������")
            else:
                connection.send("��½�ɹ�")
                login_right=True
    except timeout:
        print "time out"
    except:
        print "something wrong"
    connection.close() #�ն˱������������ͷ���Դ
    
s_server.close()


