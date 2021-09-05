"""
class MyList()
1）初始化方法
2）__iter__()对外提供迭代器
3）addItem()用于添加数据

class MyIterator()
1）初始化方法
2）__iter__()
3）__next__()用于获取下一个值

最终创建mylist = MyList()
遍历mylist即可打印数值
"""


class MyList(object):
    def __init__(self):
        self.items = []

    def __iter__(self):  # ①在实例对象中，iter()返回Iterator，所以须在__iter__()中创建Iterator实例
        list_iterator = MyIterator(self.items)  # 向Iterator传参
        return list_iterator

    def additem(self, value):
        self.items.append(value)


class MyIterator(object):
    def __init__(self, items):  # 接收MyList的传参
        self.items = items
        self.current_index = 0  # 用于记录位置

    def __iter__(self):
        pass

    '''
    __next__()作用:
    1、判断下标是否越界，如果越界，则抛出异常
        1）根据下标，获取下标对应的元素值
        2）下标位置+1 (下次继续获取元素)
        3）返回下标对应数据
    
    '''

    def __next__(self):  # ②已经iter()后，再调用next()方法
        if self.current_index < len(self.items):
            data = self.items[self.current_index]
            self.current_index += 1
            return data
        else:  # 避免获取元素个数超过列表长度
            raise StopIteration


if __name__ == '__main__':
    mylist = MyList()
    mylist.additem('张三')
    mylist.additem('李四')
    '''
    遍历的过程： 
    1）iter(mylist)获取mylist对象的迭代器 ->MyList->__iter__()
    2）next(Iterator)获取下一个值
    3）捕获异常
    '''
    for i in mylist:  # 相当于首先iter()获取Iterator后next()获得值
        print(i)

