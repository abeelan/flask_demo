"""
@Time   : 2021/9/30 下午1:17
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 在 demo 的基础上进行优化（tests/quick_start/demo_tdd.py）

1. flask-restful 优化 route 装饰器，路由一致，method 方法不同的情况下使用
$ pip install flask-restful

"""
import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


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
# 数据库关联 flask
db = SQLAlchemy(app)


class Data(db.Model):
    # 设定表名
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "node_id": self.node_id,
            "remark": self.remark
        }

class Server(Resource):
    """ 集成 Resource，表示使用 flask_restful
    类代表接口资源，比如访问路径
    每个方法，代表最资源的操作，比如 get、post 等
    """
    LINE = "=" * 30

    def get(self):
        """查询接口"""
        app.logger.info(self.LINE)

        id = request.args.get("id")
        if id:
            # 查询单条数据
            app.logger.info(f"查询 ID={id} 的数据行")
            test_data = Data.query.filter_by(id=id).first()
            data = [test_data.as_dict()]
        else:
            # 查询所有数据信息
            app.logger.info(f"查询所有数据行")
            test_data = Data.query.all()
            data = [d.as_dict() for d in test_data]

        app.logger.info(f"数据为 ==> \n{data}")
        app.logger.info(self.LINE)
        return {
            "error": 0,
            "message": "get success",
            "data": data
        }

    def post(self):
        """增加接口"""
        app.logger.info(self.LINE)

        case_data = request.json
        app.logger.info(f"待添加数据为：{case_data}")

        # 从接口中拿到的字典数据进行解包，使用关键字传参传入 Data
        data = Data(**case_data)
        # 如果数据字段存在列表，需要做一次转换
        data.node_id = json.dumps(request.json.get("node_id"))

        db.session.add(data)
        db.session.commit()

        app.logger.info(f"已同步更新到数据库内")
        return {"error": 0, "message": "post success"}

    def put(self):
        """修改接口"""

        # 通过 ID 找到要修改的那条数据，通过 update 修改
        id = request.json.get("id")
        data = Data.query.filter_by(id=id).update(request.json)
        db.session.commit()

        app.logger.info(self.LINE)
        app.logger.info("put success")
        app.logger.info(f"将 ID={data} 的数据修改为：{request.json}")
        app.logger.info(self.LINE)
        return {"error": 0, "message": "put success", "id": id}

    def delete(self):
        """删除接口"""
        app.logger.info(self.LINE)

        id = request.args.get("id")
        if not id:
            return {"error": 40001, "message": "Delete id can't be null."}
        Data.query.filter_by(id=id).delete()
        db.session.commit()

        app.logger.info(f"Delete id={id} success")
        app.logger.info(self.LINE)

        return {"error": 0, "message": f"Delete id={id} success"}


if __name__ == '__main__':
    # 把服务添加到 app flask 中
    # 第一个参数是添加的接口服务，第二个参数是指定对应接口服务使用的路由
    api.add_resource(Server, "/server")
    app.run(debug=True)

    db.create_all()
