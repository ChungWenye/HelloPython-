import threading
import time


def work():
    global a
    for i in range(5):
        mutex.acquire()  # 上锁在函数内部
        a += 1
        mutex.release()
    print(a)


def work_1():
    global a
    for i in range(5):
        mutex.acquire()  # 互斥锁：两者都需要使用，同一时间只有一个函数在执行，总体来看，交替执行
        a += 1
        mutex.release()
    print(a)



if __name__ == "__main__":
    a = 2
    mutex = threading.Lock()
    work_thread = threading.Thread(target=work)
    work_1_thread = threading.Thread(target=work_1)


    work_thread.start()
    work_1_thread.start()

    time.sleep(1)  # 主进程休眠，保证子进程运行结束
    print(a)
