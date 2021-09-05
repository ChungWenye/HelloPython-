import multiprocessing
from multiprocessing import Pool
import os


def write(q):
    for i in range(5):
        q.put(i)
        print('已写入%s' % i)


def read(q):
    while True:
        if q.qsize() == 0:
            print('队列已空')
            break
        print(q.get())


def main():
    pool = Pool(processes=2)
    queue = multiprocessing.Manager().Queue()  # 在进程池中必须添加Manager()，
    # 且queue的创建须在pool之后
    result = pool.apply_async(write, (queue,))  # 异步存在读取直接为空的问题
    result.wait()  # 等待write结束后才read
    pool.apply_async(read, (queue,))  # apply_async(func, args)
    pool.close()  # 不再接受新的任务，不表示关闭Pool
    pool.join()  # 主进程等待进程池结束后退出


if __name__ == '__main__':
    main()
