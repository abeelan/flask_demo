"""
@Time   : 2021/10/13 下午7:36
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : flask-restful 优化 route 装饰器，路由一致，method 方法不同的情况下使用

"""
import json

from flask import request
from flask_restful import Resource

from models.testcase import Data
from server import app, db


class TestcaseService(Resource):
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
            if test_data:
                data = [test_data.as_dict()]
            else:
                return {"error": 40004, "message": "No match data."}
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
        if isinstance(data.nodeId, list):
            data.nodeId = json.dumps(
                case_data.get("nodeId"), ensure_ascii=False
            )

        db.session.add(data)
        db.session.commit()
        db.session.close()

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