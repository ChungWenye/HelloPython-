class Test(object):
	def __init__(self,func):
		self.func = func

	def __call__(self,*args,**kwargs):  # call魔术方法能让实例对象直接调用
		print('开始测试')
		print(args)
		print(kwargs)
		self.func()
		# return self.func


# test1 = Test()
# test1()  # 调用类中call方法

@Test  # test = Test(login)
def login():
	print('开始登录')

login(2,a=10)  # 调用类中call方法


