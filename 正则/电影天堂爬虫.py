"""
1、定义函数获取列表页链接 get_movie_links()
    1）定义列表页地址
    2）打开url地址，获取数据
    3）获取数据（解码二进制）
    4）使用正则查找影片内容页地址
2、定义函数获取内容页
3、
"""

import re
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
"""
当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出
urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]错误消息。
"""


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
        print('%s:下载地址%s' % (film_name, film_url))


if __name__ == '__main__':
    main()
