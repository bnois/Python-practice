import socket
import time

s_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #�����ͻ���socket����
s_client.connect(('localhost',9001)) #�ͻ��˷�����������
time.sleep(3) #�ȴ����ӽ���

#�������Ӻ�---
login_right=False
while login_right==False:
    print "�������û�����"
    name=raw_input()
    s_client.send(name)#�����û���
    print "���������룺"
    password=raw_input()
    s_client.send(password)#��������
    login_result=s_client.recv(1024)
    print login_result
    if login_result=="��½�ɹ�":
        login_right=True

s_client.close() #���ӹرգ��ͷ���Դ



