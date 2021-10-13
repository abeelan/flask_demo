"""
@Time   : 2021/10/13 下午7:36
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
import datetime

from server import db


class Task(db.Model):
    # 设定表名
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    remark = db.Column(db.String(120))
    report = db.Column(db.String(120))
    # 指定时间格式，如果不传值的话为当前时间
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def as_dict(self):
        """把 python 对象转换为标准的 json 格式，flask 接口才能识别"""
        return {
            "id": self.id,
            "remark": self.remark,
            "report": self.report,
            "create_at": self.create_at
        }


if __name__ == '__main__':
    db.create_all()