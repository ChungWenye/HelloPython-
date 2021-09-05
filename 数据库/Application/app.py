import utils
import show_film


def application(client, recv_data):

    response_content = ''
    film_list = show_film.show()
    for row in film_list:
        response_content += "%d:%s    下载地址:[<a href='%s'>%s</a>] <br>" % (row[0], row[1], row[2],row[2])

    response_data = utils.creat_http_response('200 OK', response_content)
    return response_data
