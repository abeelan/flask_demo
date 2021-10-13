"""
@Time   : 2021/9/30 下午1:17
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 在 demo 的基础上进行优化（tests/quick_start/demo_tdd.py）

"""
import logging

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
api = Api(app)
# 解决跨域问题
CORS(app, supports_credentials=True)

username = "root"
pwd = "admin"
ip = "localhost"
port = "3306"
database = "hogwarts"
# 设置mysql 链接方法； mysql+pymysql 代表使用的引擎
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决warning问题
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 设置日志级别
app.logger.setLevel(logging.DEBUG)
# 数据库关联 flask
db = SQLAlchemy(app)



def router():
    """路由管理"""
    from apis.testcase import TestcaseService
    from apis.task import TaskService

    # 把服务添加到 app flask 中
    # 第一个参数是添加的接口服务，第二个参数是指定对应接口服务使用的路由
    api.add_resource(TestcaseService, "/testcase")
    api.add_resource(TaskService, "/task")


if __name__ == '__main__':
    router()
    app.run(debug=True)
