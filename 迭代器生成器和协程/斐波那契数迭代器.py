"""
斐波那契迭代器
1）定义class Iterator
2）__iter__() 和 __next__()
3）a, b = b, a+b
4）返回a值
"""


class Fibnacci(object):
    def __init__(self, index):
        self.index = index
        self.current_index = 0
        self.a, self.b = 1, 1

    """
    返回Fibnacci类本身
    非常聪明的办法，因为类本身就是一个Iterator，这样iter得到的就是Iterator
    """
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.index:
            data = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_index += 1
            return data
        else:
            raise StopIteration


if __name__ == '__main__':
    fib = Fibnacci(100)
    for i in fib:
        print(i, end=' ')

