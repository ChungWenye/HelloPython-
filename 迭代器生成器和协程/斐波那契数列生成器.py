def fibnacci(index):
    current_index = 0
    a, b = 1, 1
    while current_index < index:  # ①yield的执行开始处
        data = a
        a, b = b, a + b
        current_index += 1
        yield data  # ②yiled保存函数状态，并在此暂停，等待继续运行（此处是返回①）
    else:
        return 'Over'  # return用于终结Generator

    """可以利用.send()方法传参到yield，随后利用该参数判断是否return"""

    # 下面是一个愚蠢的方法
    # while True:
    #     if current_index < index:
    #         data = a
    #         a, b = b, a + b
    #         current_index += 1
    #         yield data
    #     else:
    #         break


if __name__ == '__main__':
    fib = fibnacci(5)
    while True:
        print(next(fib))
