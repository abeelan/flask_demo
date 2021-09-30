"""
@Time   : 2021/9/29 下午7:47
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   :

# 运行方式 1 添加环境变量
$ export FLASK_APP=demo
$ export FLASK_ENV=development
$ flask run

# 运行方式 2 通过 __name__ == __main__
"""

from flask import Flask, escape, request, session

# 实例化 flask 对象
app = Flask(__name__)
# 生成 cookie 的 key
app.secret_key = "lan"


# 指定路由；每次访问这个路由，都会执行函数的内容
@app.route('/')
def hello():
    # 获取请求 URL 中的参数信息
    name = request.args.get("name", "World!")
    return f"Hello, {escape(name)}"


@app.route('/request_json', methods=["post"])
def request_json():
    # 获取请求体信息
    return request.json


# 通过 methods 参数设置请求方法
@app.route('/login', methods=["get", "post"])
def login():
    res = {
        "method": request.method,
        "url": request.path,
        "args": request.args,
        "form": request.form
    }

    # 设置 cookie
    session["username"] = request.args.get("name")
    return res


if __name__ == '__main__':
    # 调用 app.run 启动后端服务
    # port 指定端口号
    # debug 指定为 true 的话，会热更新，便于调试
    app.run(debug=True, port=8000)