"""
1、准备两个进程，一写一读
2、创建队列，通过队列传递数据
"""
import multiprocessing
from multiprocessing import Queue
import time


def write(q):
    for i in range(100):
        q.put(i)
        print('已写入%s'%i)


def read(q):
    while True:
        if q.qsize() == 0:
            print('队列已空')
            break
        print(q.get())


def main():
    queue = Queue()
    read_process = multiprocessing.Process(target=read, args=(queue,))
    write_process = multiprocessing.Process(target=write, args=(queue,))

    write_process.start()
    write_process.join()  # 设置优先执行

    read_process.start()


if __name__ == '__main__':
    main()
