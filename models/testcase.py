"""
@Time   : 2021/10/13 下午7:36
@Author : lan
@Mail   : lanzy.nice@gmail.com
@Desc   : 
"""
from server import db


class Data(db.Model):
    # 设定表名
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    nodeId = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "nodeId": self.nodeId,
            "remark": self.remark
        }