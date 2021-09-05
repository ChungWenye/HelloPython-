import threading


def get_value(index):
    mutex.acquire()  # 🔒
    data_list = [1, 2, 3, 4, 5]
    if index >= len(data_list):
        mutex.release()  # 🔓
        return  # 终止函数运行
    print(data_list[index])
    mutex.release()


if __name__ == "__main__":
    mutex = threading.Lock()
    for i in range(10):
        t1 = threading.Thread(target=get_value, args=(i,))
        t1.start()
