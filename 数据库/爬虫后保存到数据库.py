"""
1、定义函数保存数据
2、定义函数上传数据到数据库
3、定义函数检测数据库是否存在，保存成功
"""
from pymysql import connect
import re
from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
"""
当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出
urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]错误消息。
"""


def upload_data(name, url):
    sql = "insert into movie_link values(null, %s, %s)"

    ret = cur.execute(sql, [name, url])
    '''
    创建列表[name,url]，自动保存到%s,%s
    '''
    if ret:
        print('保存成功')
    else:
        print('保存失败')


'''
专门用于判断是否存在重复数据，如果存在，则不插入重复数据
（利用电影的id判断）
'''


def film_exist(name, url):
    sql = "select id from movie_link where film_name=%s and film_link=%s"
    ret = cur.execute(sql, [name, url])
    if ret:
        return True
    else:
        return False


def get_movie_links():
    movie_list_url = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
    response_data_list = request.urlopen(movie_list_url)  # 返回类文件对象
    response_data = response_data_list.read()  # 读取文件
    response_data_txt = response_data.decode('gbk')  # 注意解码格式
    url_list = re.findall('<a href=\"(.*)\" class=\"ulink\">(.*)</a>', response_data_txt)  # 返回列表中为元组
    film_dict = {}
    i = 1
    for url_data, film_name in url_list:  # 拆包
        film_url = 'https://www.ygdy8.net' + url_data
        response_film_list = request.urlopen(film_url)
        response_film = response_film_list.read()
        response_film_txt = response_film.decode('gbk')
        film = re.search('href=\"(magnet.*?)\"', response_film_txt)
        film_dict[film_name] = film.group(1)
        print('已经获取第%s条' % i)
        i += 1
    return film_dict


def main():
    film = get_movie_links()
    for film_name, film_url in film.items():
        if film_exist(film_name, film_url):
            print('%s已经存在，无需插入'%film_name)
            continue
        upload_data(film_name, film_url)


if __name__ == '__main__':
    conn = connect(host='192.168.0.108', user='root', password='3314233', database='movie_db')
    cur = conn.cursor()
    '''
    创建全局对象 连接，游标
    '''
    main()
    conn.commit()
    cur.close()
    conn.close()
