from Application import utils


def application(client, recv_data):
    loc = recv_data.find('\r\n')
    file_list = recv_data[:loc].split(' ')  # file_loc = recv_data[5:loc]
    file_loc = file_list[1]
    dir_name = 'F:/壁纸'
    if file_loc == '/':  # ' '表示空串，而非''
        file_loc = '/1.png'

    file_name = dir_name + file_loc

    try:
        with open(file_name, 'rb') as file_obj:
            response_content = file_obj.read()
            response_data = utils.creat_http_response('200 OK', response_content)
            client.send(response_data)
    except FileNotFoundError:
        response_content = 'NO SUCH FILE'.encode()
        response_data = utils.creat_http_response('404 No such file !!', response_content)
    return response_data
