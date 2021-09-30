"""
@Time   : 2021/9/30 下午1:17
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 在 demo 的基础上进行优化（tests/quick_start/demo_tdd.py）

1. flask-restful 优化 route 装饰器，路由一致，method 方法不同的情况下使用
$ pip install flask-restful

"""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Server(Resource):
    """ 集成 Resource，表示使用 flask_restful
    类代表接口资源，比如访问路径
    每个方法，代表最资源的操作，比如 get、post 等
    """

    def get(self):
        """查询接口"""
        app.logger.info("get success")
        return {"error": 0, "message": "get success"}

    def post(self):
        """增加接口"""
        app.logger.info("post success")
        return {"error": 0, "message": "post success"}

    def put(self):
        """修改接口"""
        app.logger.info("put success")
        return {"error": 0, "message": "put success"}

    def delete(self):
        """删除接口"""
        app.logger.info("delete success")
        return {"error": 0, "message": "delete success"}


if __name__ == '__main__':
    # 把服务添加到 app flask 中
    # 第一个参数是添加的接口服务，第二个参数是指定对应接口服务使用的路由
    api.add_resource(Server, "/server")
    app.run(debug=True)
