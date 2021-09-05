"""
线程1（即主线程）负责发送消息
线程2负责接收消息，连续多次，和1同时进行
守护主线程，保证主线程结束，子线程关闭
"""

"""
函数1：收消息
函数2：发消息
主函数：输入1-3选择函数
"""

import socket
import threading


def send(udp_socket):
    ip = input('请输入发送对方IP')
    port = int(input('请输入发送对方端口'))
    text = input('请输入发送内容')
    udp_socket.sendto(text.encode(), (ip, port))


def recv(udp_socket):
    while True:  # 保证能一直接收，由于采用udp，没有建立连接，不必判断是否为空
        recv_data = udp_socket.recvfrom(1024)
        recv_txt = recv_data[0].decode('gbk')
        print('收到%s的消息%s' % (recv_data[1][0], recv_txt))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('192.168.50.143', 8080))
    udp_thread = threading.Thread(target=recv, args=(udp_socket,))
    threading.Thread.setDaemon(udp_thread, True)  # udp_thread.daemon = True
    udp_thread.start()

    while True:
        print('1、发送消息')
        print('3、推出系统')
        print('***************')
        index = int(input('请输入1-3\n'))
        if index == 1:
            send(udp_socket)
        if index == 3:
            print('退出系统......')
            break


if __name__ == '__main__':
    main()
