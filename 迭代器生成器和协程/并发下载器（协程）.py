import gevent
from urllib import request  # 核心方法：打开网址并返回对应的内容（二进制）
from gevent import monkey
monkey.patch_all()

"""
1、定义下载图片位置
2、利用download_img()函数下载图片
    1）根据url请求网络资源
    2）本地创建文件，用于保存
    3）读取资源并写入
    4）异常捕获!!
"""


def download(url_name, img_name):
    try:
        file_name = 'C:/Users/DELL/Desktop/' + img_name
        response_data = request.urlopen(url_name)
        with open(file_name, 'wb') as file_obj:
            while True:
                file_data = response_data.read(1024)  # 保存在data后需要读取数据
                if not file_data:
                    break
                file_obj.write(file_data)
    except Exception:
        print('%s下载失败' % img_name)
    else:
        print('%s下载成功' % img_name)


if __name__ == '__main__':
    # img_url1 = "http://img.mp.itc.cn/upload/20170716/8e1b835f198242caa85034f6391bc27f.gif"
    img_url1 = "https://quanjing.com/image/frameSet/loading.gif"
    img_url2 = "http://img.mp.sohu.com/upload/20170529/d988a3d940ce40fa98ebb7fd9d822fe2.png"
    img_url3 = "http://image.uczzd.cn/11867042470350090334.gif?id=0&from=export"

    gevent_list = [gevent.spawn(download, img_url1, '1.gif'),
                   gevent.spawn(download, img_url2, '2.png'),
                   gevent.spawn(download, img_url3, ' 3.gif')]

    gevent.joinall(gevent_list)  # 批量join(list)，须传入列表
