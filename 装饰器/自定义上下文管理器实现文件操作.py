"""
with open()能自动关闭无法正常打开的文件
上下文(context)管理器:
包含了__enter__()和__exit__()方法
"""

class OpenFile(object):
	def __init__(self, file_name, open_method):
		self.file_name = file_name
		self.open_method = open_method

	def __enter__(self):  # 上文方法
		print('正在打开文件')
		file = open(self.file_name, self.open_method)
		self.file = file
		return self.file  # 返回给main中as file 的file

	def __exit__(self, exc_type, exc_val, exc_tb):  # 下文方法
		print('这在关闭文件')
		self.file.close()

with OpenFile('hello.txt','r') as file: # file并不是OpenFile的实例对象
	file_txt = file.read()  # txt用于接受读取内容
	print(file_txt)
