"""
@Time   : 2021/9/30 上午2:21
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 测试驱动开发
"""

from flask import Flask

app = Flask(__name__)


@app.route("/testcase", methods=["get"])
def get_case():
    """查询接口"""
    app.logger.info("get success")
    return {"error": 0, "message": "get success"}


@app.route("/testcase", methods=["post"])
def post_case():
    """增加接口"""
    app.logger.info("post success")
    return {"error": 0, "message": "post success"}


@app.route("/testcase", methods=["put"])
def put_case():
    """修改接口"""
    app.logger.info("put success")
    return {"error": 0, "message": "put success"}


@app.route("/testcase", methods=["delete"])
def delete_case():
    """删除接口"""
    app.logger.info("delete success")
    return {"error": 0, "message": "delete success"}


if __name__ == '__main__':
    app.run(debug=True)
