import multiprocessing
from multiprocessing import Pool
import os


def copy(dest_dir, source_dir):
    try:
        os.mkdir(dest_dir)
    except Exception:
        print('文件夹已经存在!!')
    file_list = os.listdir(source_dir)
    for file_name in file_list:
        with open(source_dir + '/' + file_name, 'rb') as source_obj:
            with open(dest_dir + '/' + file_name, 'wb') as file_obj:
                while True:
                    content = source_obj.read(1024)
                    if content:  # 每次读取1kb，为空时退出
                        file_obj.write(content)
                    else:
                        break


if __name__ == '__main__':
    dest_dir = 'C:/Users/DELL/Desktop/TEST'
    source_dir = 'E:/BaiduNetdiskDownload/视频-python进阶/python进阶资料/资料-python/day07资料/02-其他资料/test'
    # copy_work = multiprocessing.Process(target=copy, args=(dest_dir, source_dir))
    # copy_work.start()
    pool = multiprocessing.Pool(processes=3)
    pool.apply_async(copy, (dest_dir, source_dir))
    pool.close()
    pool.join()
