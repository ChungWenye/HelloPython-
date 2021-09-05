def test(path):
	print(path)
	def func_out(func):
		def func_in():
			print('--开始验证--')
			func()

		return func_in
	return func_out

"""
1)test('login.py'),传入参数  -->返回func_out的引用
2)@ 第一步的结果     		 	-->@func_out() （与原来的装饰器一致）
"""
@test('login.py')
def login():
	print('开始登录')
@test('regsiter.py')
def register():
	print('开始注册')

login()
register()