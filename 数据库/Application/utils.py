def creat_http_response(status, response_content):
    response_line = "HTTP/1.1 %s\r\n" % status
    response_header = "Server:ChungWS/1.1\r\n"
    response_header = "Content-type:text/html;charset=utf-8\r\n"
    # 优先使用HTML，且解码格式是utf8
    response_blank = "\r\n"
    response_data = (response_line + response_header + response_blank + response_content).encode()
    return response_data
