"""
1、继承threading.Thread
2、重写.run（位于threading.Thread）
3、实例化对象用.start()启动自定义类
"""
import threading


class MyThread(threading.Thread):

    def __init__(self, num):
        super().__init__()  # 先调用父类的init方法
        self.num = num

    def run(self):
        print(self.name, self.num)  # 从父类继承的name属性

    # def start(self):
    #     pass


if __name__ == '__main__':
    th = MyThread(4)
    th.start()  # 从父类继承的start()
