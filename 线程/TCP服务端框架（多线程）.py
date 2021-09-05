"""
1、多客户端连接
2、不同客户端同时收发
3、主线程结束，子线程结束

1、创建socket
2、绑定ip和端口
3、设置地址复用
4、设置监听
5、等待并返回客户端连接
"""

import socket
import threading


def recv(client, iport):
    while True:
        recv_data = client.recv(1024)
        if not recv_data:  # 用于判断是否需要断开
            break
        recv_txt = recv_data.decode('gbk')
        print('收到%s的信息%s' % (iport[0], recv_txt))
    client.close()


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_socket.bind(('', 8081))  # 设置REUSADDR必须在bind前
    tcp_socket.listen(128)

    while True:
        new_client, ip_port = tcp_socket.accept()
        print('新用户%s上线' % ip_port[0])
        recv_thread = threading.Thread(target=recv, args=(new_client, ip_port))
        recv_thread.deamon = True  # 守护主线程
        recv_thread.start()

    tcp_socket.close()


if __name__ == '__main__':
    main()
