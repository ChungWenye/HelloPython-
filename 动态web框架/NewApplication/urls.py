# from NewApplication import funs
"""
1、路由列表Django(字典固定)

创建路由字典
无需创建函数，导入urls模块后，urls.route_dict[]即可返回值

route_dict = {'/gettime.py':funs.gettime,
		'/index.py':funs.index,
		'/center.py':funs.center}
		
2、装饰器路由Flask(自由添加)

利用装饰器工厂函数把路径添加到字典中
参见funs模块中的route装饰器工厂
"""

route_dict = {}