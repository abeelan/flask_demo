"""
@Time   : 2021/9/30 下午3:31
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : SQL ORM 模式

https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

https://faker.readthedocs.io/en/master/
"""
import random

from faker import Faker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置 flask 关联的数据库
# sqlite:/// 固定格式
# /tmp/test.db 数据库生成路径
# 这是官方的 demo，本项目不用 sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

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


class User(db.Model):
    """一个类表示一张表"""

    # 设定表名
    __tablename__ = "user"
    # 每个类的属性
    # db.Column 在实例内说明这一列数据的配置
    # 整形，设置主键
    id = db.Column(db.Integer, primary_key=True)
    # db.String(80) 设置字符串最大长度
    # unique 是否可重复，比如手机号
    # nullable 是否可以为空
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120))

    def __repr__(self):
        """重写实例打印信息"""
        return '<User %r>' % self.username

if __name__ == '__main__':
    """
    # 创建表
    db.create_all()
    # 删除表; 如果表内有数据，先导出
    db.drop_all()
    """

    """ 进行增删改查操作 """

    # 测试数据构造
    faker = Faker(locale='zh-CN')

    def gender():
        gender = ["男", "女"]
        return random.choice(gender)

    """
    # 增
    user = User(id=3, username=faker.name(), email=faker.email(), gender=gender())
    # 把数据对象，添加在 session 中
    db.session.add(user)
    # 所有涉及对数据库的修改操作，最后都需要 commit 一下
    db.session.commit()
    """

    """
    # 批量增
    users = []
    id = 4
    for _ in range(3):
        user = User(id=id, username=faker.name(), email=faker.email(), gender=gender())
        id += 1
        users.append(user)
    print(users)
    db.session.add_all(users)
    db.session.commit()
    """

    """
    # 查全部
    # User 代表查询 user 表所有数据，return -> list[instance, instance, ..]
    result = User.query.all()
    print(result)
    """

    """
    # 按条件查
    
    # 查询第一条数据
    res1 = User.query.filter_by(gender="男").first()
    print(res1)  # 这是一个对象
    print(res1.username, res1.email, res1.gender)
    print("=" * 10)
    # 查询所有数据
    res2 = User.query.filter_by(gender="男").all()
    print(res2)
    print("=" * 10)
    # 查询所有 id 大于 2 的用户
    res3 = User.query.filter(User.id > 2).all()
    print(res3)
    """

    """
    # 删
    User.query.filter_by(id=2).delete()
    db.session.commit()
    """

    """
    # 改
    
    # 方法一
    res = User.query.filter_by(id=3).first()
    print(res)
    res.gender = "未知"
    db.session.commit()
    
    # 方法二
    User.query.filter_by(id=4).update(
        {
            "gender": "未知",
            "email": "test@qa.com"
        }
    )
    db.session.commit()
    """
