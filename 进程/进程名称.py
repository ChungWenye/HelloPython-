"""
socket创建
request
拼接文件夹中的html
发送响应头
"""

import socket
import multiprocessing
import threading


def request_handler(client, ip_port):
    print('欢迎新用户%s' % ip_port[0])
    recv_data = client.recv(1024).decode('gbk')

    if not recv_data:
        client.close()
        return

    loc = recv_data.find('HTTP')
    dir_name = 'F:/壁纸/'
    file_loc = recv_data[5:loc]
    if file_loc == ' ':  # ' '表示空串，而非''
        file_loc = '1.png'
    request_line = "HTTP/1.1 200 OK\r\n"
    # request_line = "HTTP/1.1 404 NOT FOUND\r\n"
    request_header = "Server:ChungWS/1.1\r\n"
    request_blank = "\r\n"

    file_name = dir_name + file_loc

    try:
        with open(file_name, 'rb') as file_obj:
            request_content = file_obj.read()

        request_data = (request_line + request_header + request_blank).encode() + request_content
        client.send(request_data)
    except Exception:
        request_line = "HTTP/1.1 404 NOT FOUND\r\n"
        request_header = "Server:ChungWS/1.1\r\n"
        request_blank = "\r\n"
        request_content = 'No such file !!'
        request_data = (request_line + request_header + request_blank + request_content).encode()
        client.send(request_data)
    client.close()


def main():
    web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    web_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    web_socket.bind(('', 8080))
    web_socket.listen(128)
    while True:
        new_client_socket, client_ip_port = web_socket.accept()
        # request_process = threading.Thread(target=request_handler, args=(new_client_socket, client_ip_port))

        request_process = multiprocessing.Process(target=request_handler,
                                                  args=(new_client_socket, client_ip_port))
        request_process.daemon = True
        request_process.start()


if __name__ == '__main__':
    main()
