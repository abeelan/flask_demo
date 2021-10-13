"""
@Time   : 2021/10/13 下午7:37
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
from flask import request
from flask_restful import Resource

from models.task import Task
from server import app, db
from utils.exec_tools import ExecTools


class TaskService(Resource):

    def get(self):
        id = request.args.get("id")
        if id:
            # 查询单条数据
            app.logger.info(f"查询 ID={id} 的测试任务")
            test_data = Task.query.filter_by(id=id).first()
            if test_data:
                data = [test_data.as_dict()]
            else:
                return {"error": 40004, "message": "No match data."}
        else:
            # 查询所有数据信息
            app.logger.info(f"查询所有测试任务")
            tasks = Task.query.all()
            data = [task.as_dict() for task in tasks]

        app.logger.info(f"数据为 ==> \n{data}")
        return {
            "error": 0,
            "message": "get success",
            "data": data
        }


def post(self):
        """
        1. 调用 jenkins 执行测试用例
        2. 将测试数据写入到数据库内
        """
        # 从 post 请求体中获取要执行的测试用例名称 - nodeId
        data = request.json
        nodeId = data.get("nodeId")
        app.logger.info(f"执行的测试用例为：{nodeId}")

        # 传入要执行的测试用例文件名称即可执行，并返回测试报告连接
        report = ExecTools().invoke(nodeId)
        app.logger.info(f"测试结果为：{report}")

        # 写入数据库
        task = Task(remark=nodeId, report=report)
        app.logger.info(f"添加了一条测试任务：{nodeId}, 报告地址为: {report}")
        db.session.add(task)
        db.session.commit()
        db.session.close()

        return {"error": 0, "msg": "ok"}
