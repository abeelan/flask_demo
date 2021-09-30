"""
@Time   : 2021/9/30 上午12:44
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""

import pymysql


db = pymysql.connect(
    host="stuq.ceshiren.com",
    user="hogwarts_python",
    password="hogwarts_python",
    db="hogwarts_python",
    charset="utf8mb4"
)


def test_demo():
    with db.cursor() as cursor:
        sql = "show tables;"
        cursor.execute(sql)
        print(f"exec ==> {sql}")
        print(cursor.fetchall())


