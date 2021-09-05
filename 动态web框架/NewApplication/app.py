from NewApplication import utils, funs
import time


def application(client, recv_data):
    loc = recv_data.find('\r\n')
    file_list = recv_data[:loc].split(' ')  # file_loc = recv_data[5:loc]
    file_loc = file_list[1]
    file_loc_1 = file_loc
    dir_name = 'H:/python进阶/动态web框架/static'

    if file_loc == '/':  # ' '表示空串，而非''
        file_loc = '/index.html'

    file_name = dir_name + file_loc

    """
    动态显示改进内容 比如py文件
    判断后缀  .endswith('py')方法返回bool
    """
    if file_loc_1.endswith('.py'):

        if file_loc_1 in funs.route_dict:  # 查询key是否位于字典当中
            fun = funs.route_dict[file_loc_1]
            response_content = fun().encode()
            response_data = utils.creat_http_response('200 OK', response_content)
        else:
            response_content = 'NO SUCH FILE'.encode()
            response_data = utils.creat_http_response('404 No such file !!', response_content)
    
    else:
        try:
            with open(file_name, 'rb') as file_obj:
                response_content = file_obj.read()
                response_data = utils.creat_http_response('200 OK', response_content)

        except FileNotFoundError:
            response_content = 'NO SUCH FILE'.encode()
            response_data = utils.creat_http_response('404 No such file !!', response_content)
    
    return response_data
