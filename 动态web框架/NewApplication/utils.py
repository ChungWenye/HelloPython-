def creat_http_response(status, response_content):
    response_line = "HTTP/1.1 %s\r\n" % status
    response_header = "Server:ChungWS/1.1\r\n"
    response_blank = "\r\n"
    response_data = (response_line + response_header + response_blank).encode() + response_content
    return response_data
