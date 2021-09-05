from pymysql import connect


def show():
    conn = connect(host='192.168.0.108', user='root', password='3314233', database='movie_db')
    cur = conn.cursor()
    sql = "select * from movie_link"
    cur.execute(sql)
    result_lis = cur.fetchall()

    conn.commit()
    # for row in result_lis:
    #     response_body += "%d:%s    下载地址[%s] <br>" % (row[0], row[1], row[2])
    # <br>是HTML的换行
    cur.close()
    conn.close()
    return result_lis
