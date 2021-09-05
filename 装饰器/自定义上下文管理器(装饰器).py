from contextlib import contextmanager

@contextmanager  # 上下文管理器装饰器
def OpenFile(file_name, open_method):
	print('正在进入文件')
	file = open(file_name, open_method)
	yield file  
	"""
	yield 将函数分割成两部分
	上半部分是 __enter__
	下一部分是 __exit__
	"""
	print('正在关闭')
	file.close()

with OpenFile("hello.txt", "r") as file:
    # 开始读取文件
    file_data = file.read()
    print(file_data)
