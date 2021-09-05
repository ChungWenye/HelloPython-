import time
import pymysql
import re

route_dict = {}


def route(file_path):
    def outer(func):
        route_dict[file_path] = func  # 写在此处的含义:调用之前就能

        def inner():
            func()
            """
			route_dict[file_path] = func  写在此处则为空字典:
			需要funs(),即调用时才能执行写入字典
			"""

        return inner

    return outer


@route('/index.py')
def index():
    with open('H:/python进阶/动态web框架/templates/index.html', encoding='utf') as file:
        content = file.read()
    con = pymysql.connect(host='192.168.0.105', user='root', password='3314233', database='stock_db')
    cur = con.cursor()

    sql = "select * from info"
    cur.execute(sql)
    con.commit()
    data_base = cur.fetchall()
    data = ""
    for data_line in data_base:
        html_str = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
        </tr>
        """ % data_line
        data += html_str
    # html代码含义:<tr>表示一行 <td>表示一列  "button"按钮键
    cur.close()
    con.close()
    content = re.sub('{%content%}', data, content)
    # 利用正则，将其替换为数据并返回字符串
    return content


@route('/gettime.py')
def gettime():
    return time.ctime()


@route('/center.py')
def center():  # 个人中心

    conn = pymysql.connect(host='192.168.0.105', user='root', password='3314233', database='stock_db')
    cur = conn.cursor()
    sql = 'select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info i, focus f where i.id = f.id'
    cur.execute(sql)
    data_base = cur.fetchall()

    data = ""
    for data_line in data_base:
        html_str = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
            <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
        </tr>
        """ % data_line
        data += html_str
    cur.close()
    conn.close()
    with open('H:/python进阶/动态web框架/templates/center.html', encoding='utf') as file:
        content = file.read()
    content = re.sub('{%content%}', data, content)

    return content

# route_dict = {'/gettime.py':gettime,
# 		'/index.py':index,
# 		'/center.py':center}
