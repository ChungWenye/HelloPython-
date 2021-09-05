'''
给login增加验证功能
而且不修改源代码
'''


def function_out(func):
	def function_in(*args, **kwargs):  # **kargs用于接收key = value类型的参数
		print('开始验证')
		result = func(*args, **kwargs)  # 调用函数func, func == login
		return result
	return function_in

@function_out  # 底层：login = function_out(login), login指向function_in!!
def login(*args, **kwargs):
	print('开始执行')
	return(args,kwargs)  # 返回装包后的值，拆包不能返回

ret = login(2,a=10)
print(ret)