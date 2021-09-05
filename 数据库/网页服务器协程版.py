import socket
# import multiprocessing
# import threading
from Application import app
import gevent
from gevent import monkey
monkey.patch_all()


class WebServer(object):
    def __init__(self):
        web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        web_socket.bind(('', 8080))
        web_socket.listen(128)
        self.web_socket = web_socket

    @staticmethod
    def request_handler(client, ip_port):
        print('欢迎新用户%s' % ip_port[0])
        recv_data = client.recv(1024).decode('gbk')

        if not recv_data:
            client.close()
            return

        response_data = app.application(client, recv_data)
        client.send(response_data)
        client.close()

    def start(self):
        while True:
            new_client_socket, client_ip_port = self.web_socket.accept()
            """
            子进程会拷贝主进程资源，没有释放的对象导致内存泄露，需要外部
            再次close()
            """
            # request_process = multiprocessing.Process(target=self.request_handler,
            #                                           args=(new_client_socket, client_ip_port))
            # request_process.daemon = True
            # request_process.start()
            gevent.spawn(self.request_handler, new_client_socket, client_ip_port)
            """
            由于while True，所以无需join()
            """
            # new_client_socket.close()  # 使引用计数变为0，彻底释放内存（但没看出来有什么用）


if __name__ == '__main__':
    web = WebServer()
    web.start()
